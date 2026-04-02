---
name: firebase-operations
description: Firebase/Firestore CRUD operations, real-time listeners, security patterns, and offline support. Use when implementing Firestore queries, authentication, real-time subscriptions, or Firebase security.
---

# Firebase Operations

## Firestore Document Structure

```typescript
// Collection: trips
// Document ID: TripId
{
  id: string,
  userId: string,  // For security rules
  title: string,
  destination: string,
  startDate: string,  // ISO 8601
  endDate: string,
  status: 'planning' | 'upcoming' | 'active' | 'completed' | 'archived',
  createdAt: Timestamp,
  updatedAt: Timestamp,
  itinerary: { ... }
}
```

## Service Pattern

```typescript
// services/firebase/tripFirestoreService.ts
import {
  collection, doc, getDoc, getDocs, setDoc, updateDoc, deleteDoc,
  query, where, orderBy, onSnapshot, Timestamp, serverTimestamp
} from 'firebase/firestore';
import { db } from '@/config/firebase';

const COLLECTION = 'trips';

export const tripFirestoreService = {
  // Create
  async createTrip(trip: Omit<Trip, 'id'>): Promise<TripId> {
    const tripRef = doc(collection(db, COLLECTION));
    const tripId = tripRef.id as TripId;

    await setDoc(tripRef, {
      ...trip,
      id: tripId,
      createdAt: serverTimestamp(),
      updatedAt: serverTimestamp(),
    });

    return tripId;
  },

  // Read single
  async getTrip(tripId: TripId): Promise<Trip | null> {
    const tripRef = doc(db, COLLECTION, tripId);
    const snapshot = await getDoc(tripRef);

    if (!snapshot.exists()) return null;
    return this.docToTrip(snapshot);
  },

  // Read multiple with query
  async getTripsByUser(userId: string): Promise<Trip[]> {
    const q = query(
      collection(db, COLLECTION),
      where('userId', '==', userId),
      orderBy('startDate', 'desc')
    );

    const snapshot = await getDocs(q);
    return snapshot.docs.map(this.docToTrip);
  },

  // Update
  async updateTrip(tripId: TripId, updates: Partial<Trip>): Promise<void> {
    const tripRef = doc(db, COLLECTION, tripId);
    await updateDoc(tripRef, {
      ...updates,
      updatedAt: serverTimestamp(),
    });
  },

  // Delete
  async deleteTrip(tripId: TripId): Promise<void> {
    const tripRef = doc(db, COLLECTION, tripId);
    await deleteDoc(tripRef);
  },

  // Helper: Convert Firestore doc to Trip
  docToTrip(doc: DocumentSnapshot): Trip {
    const data = doc.data()!;
    return {
      ...data,
      id: doc.id as TripId,
      createdAt: data.createdAt?.toDate?.()?.toISOString() ?? new Date().toISOString(),
      updatedAt: data.updatedAt?.toDate?.()?.toISOString() ?? new Date().toISOString(),
    } as Trip;
  },
};
```

## Real-Time Listeners

```typescript
// Subscribe to collection
subscribeToUserTrips(
  userId: string,
  onUpdate: (trips: Trip[]) => void,
  onError: (error: Error) => void
): () => void {
  const q = query(
    collection(db, COLLECTION),
    where('userId', '==', userId),
    orderBy('updatedAt', 'desc')
  );

  const unsubscribe = onSnapshot(
    q,
    (snapshot) => {
      const trips = snapshot.docs.map(this.docToTrip);
      onUpdate(trips);
    },
    (error) => {
      console.error('Firestore subscription error:', error);
      onError(error);
    }
  );

  return unsubscribe;
}

// Usage in store
const useTripStore = create<TripState>((set) => ({
  trips: [],
  unsubscribe: null,

  startListening: (userId: string) => {
    const unsubscribe = tripFirestoreService.subscribeToUserTrips(
      userId,
      (trips) => set({ trips }),
      (error) => set({ error: error.message })
    );
    set({ unsubscribe });
  },

  stopListening: () => {
    const { unsubscribe } = get();
    if (unsubscribe) {
      unsubscribe();
      set({ unsubscribe: null });
    }
  },
}));
```

## Authentication

```typescript
// services/firebase/authService.ts
import {
  signInWithPopup, signOut, onAuthStateChanged,
  GoogleAuthProvider, User
} from 'firebase/auth';
import { auth } from '@/config/firebase';

const googleProvider = new GoogleAuthProvider();

export const authService = {
  async signInWithGoogle(): Promise<User> {
    const result = await signInWithPopup(auth, googleProvider);
    return result.user;
  },

  async signOut(): Promise<void> {
    await signOut(auth);
  },

  onAuthStateChanged(callback: (user: User | null) => void): () => void {
    return onAuthStateChanged(auth, callback);
  },

  getCurrentUser(): User | null {
    return auth.currentUser;
  },
};
```

## Security Rules

```javascript
// firestore.rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Helper functions
    function isAuthenticated() {
      return request.auth != null;
    }

    function isOwner(userId) {
      return request.auth.uid == userId;
    }

    function isValidTrip() {
      let data = request.resource.data;
      return data.title is string && data.title.size() > 0
        && data.userId == request.auth.uid
        && data.status in ['planning', 'upcoming', 'active', 'completed', 'archived'];
    }

    // Trips collection
    match /trips/{tripId} {
      allow read: if isAuthenticated() && isOwner(resource.data.userId);
      allow create: if isAuthenticated() && isValidTrip();
      allow update: if isAuthenticated()
        && isOwner(resource.data.userId)
        && request.resource.data.userId == resource.data.userId; // Can't change owner
      allow delete: if isAuthenticated() && isOwner(resource.data.userId);
    }
  }
}
```

## Batch Operations

```typescript
async function batchUpdateActivities(
  tripId: TripId,
  updates: Array<{ activityId: ActivityId; changes: Partial<Activity> }>
): Promise<void> {
  const batch = writeBatch(db);

  for (const { activityId, changes } of updates) {
    const ref = doc(db, `trips/${tripId}/activities`, activityId);
    batch.update(ref, {
      ...changes,
      updatedAt: serverTimestamp(),
    });
  }

  await batch.commit();
}
```

## Transactions

```typescript
async function moveActivityBetweenDays(
  tripId: TripId,
  activityId: ActivityId,
  fromDayId: string,
  toDayId: string
): Promise<void> {
  await runTransaction(db, async (transaction) => {
    const tripRef = doc(db, COLLECTION, tripId);
    const tripDoc = await transaction.get(tripRef);

    if (!tripDoc.exists()) {
      throw new Error('Trip not found');
    }

    const trip = tripDoc.data() as Trip;
    // Perform the move logic...

    transaction.update(tripRef, {
      itinerary: updatedItinerary,
      updatedAt: serverTimestamp(),
    });
  });
}
```

## Offline Support

```typescript
// Enable offline persistence
import { enableIndexedDbPersistence } from 'firebase/firestore';

enableIndexedDbPersistence(db).catch((err) => {
  if (err.code === 'failed-precondition') {
    console.warn('Persistence failed: Multiple tabs open');
  } else if (err.code === 'unimplemented') {
    console.warn('Persistence not available in this browser');
  }
});

// Check pending writes
import { waitForPendingWrites } from 'firebase/firestore';

async function ensureSynced(): Promise<void> {
  await waitForPendingWrites(db);
  console.log('All changes synced to server');
}
```

## Error Handling

```typescript
async function safeFirestoreOperation<T>(
  operation: () => Promise<T>,
  context: string
): Promise<T> {
  try {
    return await operation();
  } catch (error) {
    if (error instanceof FirebaseError) {
      switch (error.code) {
        case 'permission-denied':
          throw new Error('You do not have permission to perform this action');
        case 'not-found':
          throw new Error('The requested resource was not found');
        case 'unavailable':
          throw new Error('Service temporarily unavailable. Please try again.');
        default:
          console.error(`Firestore error in ${context}:`, error);
          throw new Error('An unexpected error occurred');
      }
    }
    throw error;
  }
}
```

## Timestamp Handling

```typescript
// Convert Firestore Timestamp to ISO string
function timestampToISO(timestamp: Timestamp | null): string {
  if (!timestamp) return new Date().toISOString();
  return timestamp.toDate().toISOString();
}

// Convert ISO string to Firestore Timestamp
function isoToTimestamp(isoString: string): Timestamp {
  return Timestamp.fromDate(new Date(isoString));
}

// Server timestamp for creation/updates
import { serverTimestamp } from 'firebase/firestore';

const tripData = {
  ...trip,
  createdAt: serverTimestamp(),
  updatedAt: serverTimestamp(),
};
```
