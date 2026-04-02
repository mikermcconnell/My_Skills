---
name: typescript-strict
description: TypeScript strict mode patterns including proper typing, avoiding any, branded types, and null safety. Use when writing TypeScript code, fixing type errors, or reviewing type definitions.
---

# TypeScript Strict Mode Patterns

## Core Rules

1. **No `any`**: Use `unknown` for truly dynamic values
2. **Explicit return types**: For public functions
3. **Null safety**: Handle undefined/null explicitly
4. **Branded types**: For IDs and special strings
5. **Strict null checks**: Always enabled

## Avoiding `any`

### Use `unknown` for Dynamic Values

```typescript
// Bad
function parseJSON(json: string): any {
  return JSON.parse(json);
}

// Good
function parseJSON(json: string): unknown {
  return JSON.parse(json);
}

// Then narrow the type
const data = parseJSON(response);
if (isTrip(data)) {
  // data is Trip here
}
```

### Type Guards

```typescript
function isTrip(value: unknown): value is Trip {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'title' in value &&
    'destination' in value
  );
}

function isActivity(value: unknown): value is Activity {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'time' in value &&
    'type' in value
  );
}
```

### Generic Constraints

```typescript
// Bad - allows any type
function firstItem<T>(arr: T[]): T | undefined {
  return arr[0];
}

// Better - constrain when needed
function findById<T extends { id: string }>(
  items: T[],
  id: string
): T | undefined {
  return items.find(item => item.id === id);
}
```

## Branded Types

Prevent mixing up IDs of different types:

```typescript
// Define branded types
type TripId = string & { readonly __brand: 'TripId' };
type ActivityId = string & { readonly __brand: 'ActivityId' };
type UserId = string & { readonly __brand: 'UserId' };

// Helper functions to create them
function createTripId(id: string): TripId {
  return id as TripId;
}

function createActivityId(id: string): ActivityId {
  return id as ActivityId;
}

// Now this is a compile error:
function getTrip(tripId: TripId): Trip { /* ... */ }

const activityId = createActivityId('act-123');
getTrip(activityId); // Error: ActivityId not assignable to TripId
```

## Null Safety

### Optional Chaining

```typescript
// Bad
const city = trip && trip.destination && trip.destination.city;

// Good
const city = trip?.destination?.city;
```

### Nullish Coalescing

```typescript
// Bad - treats 0 and '' as falsy
const count = value || 10;

// Good - only null/undefined trigger default
const count = value ?? 10;
```

### Non-null Assertion (Use Sparingly)

```typescript
// Only when you're certain
const element = document.getElementById('root')!;

// Better - handle the null case
const element = document.getElementById('root');
if (!element) {
  throw new Error('Root element not found');
}
```

### Explicit Undefined Checks

```typescript
// In function parameters
function updateTrip(tripId: TripId, updates: Partial<Trip>): void {
  if (updates.title !== undefined) {
    // Explicitly set, even if empty string
  }
}
```

## Interface vs Type

```typescript
// Use interface for objects that may be extended
interface Trip {
  id: TripId;
  title: string;
  destination: string;
}

interface TripWithItinerary extends Trip {
  itinerary: Itinerary;
}

// Use type for unions, intersections, mapped types
type TripStatus = 'planning' | 'upcoming' | 'active' | 'completed' | 'archived';

type TripUpdate = Partial<Omit<Trip, 'id'>>;

type ActivityType = 'food' | 'lodging' | 'activity' | 'travel';
```

## Function Types

```typescript
// Explicit return types for public API
export function calculateDuration(start: string, end: string): number {
  // ...
}

// Callback types
type OnTripSelect = (tripId: TripId) => void;
type OnActivityUpdate = (activity: Activity) => Promise<void>;

// Props with callbacks
interface TripCardProps {
  trip: Trip;
  onSelect: OnTripSelect;
  onEdit?: (tripId: TripId) => void;
}
```

## Discriminated Unions

```typescript
type ApiResponse<T> =
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: string };

function handleResponse<T>(response: ApiResponse<T>): void {
  switch (response.status) {
    case 'loading':
      showSpinner();
      break;
    case 'success':
      displayData(response.data); // TypeScript knows data exists
      break;
    case 'error':
      showError(response.error); // TypeScript knows error exists
      break;
  }
}
```

## Utility Types

```typescript
// Pick specific properties
type TripSummary = Pick<Trip, 'id' | 'title' | 'destination'>;

// Omit properties
type NewTrip = Omit<Trip, 'id' | 'createdAt'>;

// Make all properties optional
type TripUpdate = Partial<Trip>;

// Make all properties required
type RequiredTrip = Required<Trip>;

// Read-only
type ImmutableTrip = Readonly<Trip>;

// Record for dictionaries
type TripsByStatus = Record<TripStatus, Trip[]>;
```

## React Component Props

```typescript
interface ComponentProps {
  // Required props
  trip: Trip;

  // Optional props
  className?: string;

  // Event handlers
  onSave: (trip: Trip) => void;
  onClick?: () => void;

  // Children
  children?: React.ReactNode;
}

// With generics
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
  keyExtractor: (item: T) => string;
}
```

## Common Mistakes

```typescript
// Bad: Implicit any in catch
try {
  // ...
} catch (error) {
  console.log(error.message); // error is unknown
}

// Good: Type narrow the error
try {
  // ...
} catch (error) {
  if (error instanceof Error) {
    console.log(error.message);
  }
}

// Bad: Object indexing without guard
const value = obj[key]; // Element implicitly has 'any' type

// Good: Type the index
const value = (obj as Record<string, unknown>)[key];
// Or use Map for dynamic keys
```
