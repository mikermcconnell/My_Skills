---
name: error-handling-patterns
description: Consistent error handling with user-friendly messages, logging, and graceful degradation. Use when implementing try-catch blocks, error boundaries, or API error handling.
---

# Error Handling Patterns

## Core Principles

1. **Fail gracefully**: Never show raw errors to users
2. **Log for debugging**: Capture context for developers
3. **Preserve state**: Don't corrupt data on failure
4. **Provide recovery**: Help users understand next steps

## Async/Await Pattern

```typescript
async function fetchTrips(userId: string): Promise<Trip[]> {
  try {
    const response = await api.get(`/trips?userId=${userId}`);
    return response.data;
  } catch (error) {
    // Log with context
    console.error('Failed to fetch trips:', { userId, error });

    // Rethrow with user-friendly message or handle
    if (error instanceof NetworkError) {
      throw new Error('Unable to load trips. Please check your connection.');
    }
    throw new Error('Something went wrong loading your trips.');
  }
}
```

## Service Layer Pattern

```typescript
// In service file - handle API-specific errors
export const tripService = {
  async getTrip(tripId: TripId): Promise<Trip> {
    try {
      const doc = await getDoc(doc(db, 'trips', tripId));
      if (!doc.exists()) {
        throw new NotFoundError(`Trip ${tripId} not found`);
      }
      return docToTrip(doc);
    } catch (error) {
      if (error instanceof NotFoundError) throw error;

      console.error('Firestore getTrip failed:', { tripId, error });
      throw new ServiceError('Failed to load trip', { cause: error });
    }
  }
};
```

## Store Pattern (Zustand)

```typescript
interface TripState {
  trips: Trip[];
  loading: boolean;
  error: string | null;

  fetchTrips: () => Promise<void>;
}

export const useTripStore = create<TripState>((set, get) => ({
  trips: [],
  loading: false,
  error: null,

  fetchTrips: async () => {
    set({ loading: true, error: null });

    try {
      const trips = await tripService.getTrips();
      set({ trips, loading: false });
    } catch (error) {
      const message = error instanceof Error
        ? error.message
        : 'Failed to load trips';

      set({ error: message, loading: false });
      // Don't clear existing trips - show stale data with error
    }
  },
}));
```

## Component Pattern

```typescript
function TripList() {
  const { trips, loading, error, fetchTrips } = useTripStore();

  if (loading && !trips.length) {
    return <LoadingSpinner />;
  }

  return (
    <div>
      {error && (
        <ErrorBanner
          message={error}
          action={{ label: 'Retry', onClick: fetchTrips }}
        />
      )}

      {trips.map(trip => <TripCard key={trip.id} trip={trip} />)}

      {!trips.length && !error && (
        <EmptyState message="No trips yet" />
      )}
    </div>
  );
}
```

## React Error Boundary

```typescript
interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
}

class ErrorBoundary extends Component<Props, ErrorBoundaryState> {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Component error:', error, errorInfo);
    // Send to error tracking service
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || <DefaultErrorUI />;
    }
    return this.props.children;
  }
}
```

## Custom Error Classes

```typescript
// Base error with additional context
class AppError extends Error {
  constructor(
    message: string,
    public code: string,
    public context?: Record<string, unknown>
  ) {
    super(message);
    this.name = 'AppError';
  }
}

// Specific error types
class NotFoundError extends AppError {
  constructor(resource: string) {
    super(`${resource} not found`, 'NOT_FOUND');
  }
}

class ValidationError extends AppError {
  constructor(field: string, issue: string) {
    super(`Invalid ${field}: ${issue}`, 'VALIDATION_ERROR', { field });
  }
}

class NetworkError extends AppError {
  constructor() {
    super('Network connection failed', 'NETWORK_ERROR');
  }
}
```

## Error Messages

### Do
- "Unable to save changes. Please try again."
- "Trip not found. It may have been deleted."
- "Connection lost. Changes will sync when you're back online."

### Don't
- "Error: ECONNREFUSED 127.0.0.1:5000"
- "Uncaught TypeError: Cannot read property 'id' of undefined"
- "Something went wrong" (without context)

## Logging Pattern

```typescript
function logError(
  message: string,
  error: unknown,
  context?: Record<string, unknown>
) {
  console.error(message, {
    error: error instanceof Error ? {
      message: error.message,
      name: error.name,
      stack: error.stack,
    } : error,
    context,
    timestamp: new Date().toISOString(),
  });
}

// Usage
try {
  await saveTrip(trip);
} catch (error) {
  logError('Failed to save trip', error, { tripId: trip.id, userId });
  throw new Error('Unable to save trip. Please try again.');
}
```

## Recovery Strategies

1. **Retry with backoff**: For transient network errors
2. **Fallback to cache**: Show stale data with warning
3. **Partial success**: Save what you can, report failures
4. **Offline queue**: Queue for later when offline
5. **User action**: Let user decide (retry, skip, cancel)
