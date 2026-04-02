---
name: testing-strategy
description: Test writing best practices with arrange-act-assert pattern, mocking strategies, and coverage priorities. Use when writing unit tests, integration tests, or discussing testing approaches.
---

# Testing Strategy

## Test Structure (Arrange-Act-Assert)

```typescript
describe('calculateTripTotal', () => {
  it('sums all activity costs for a trip', () => {
    // Arrange - set up test data
    const activities: Activity[] = [
      createActivity({ cost: 100 }),
      createActivity({ cost: 50 }),
      createActivity({ cost: 25 }),
    ];

    // Act - execute the code under test
    const total = calculateTripTotal(activities);

    // Assert - verify the result
    expect(total).toBe(175);
  });
});
```

## What to Test (Priority Order)

### 1. Pure Functions (High Priority)
Utility functions, calculations, transformers.

```typescript
// utils/dateUtils.ts
describe('formatTripDuration', () => {
  it('returns "1 day" for single day trips', () => {
    expect(formatTripDuration(1)).toBe('1 day');
  });

  it('returns "X days" for multi-day trips', () => {
    expect(formatTripDuration(5)).toBe('5 days');
  });

  it('handles zero days', () => {
    expect(formatTripDuration(0)).toBe('0 days');
  });
});
```

### 2. Business Logic (High Priority)
Validation, state transitions, calculations.

```typescript
describe('validateTrip', () => {
  it('rejects trips without a title', () => {
    const trip = createTrip({ title: '' });
    expect(validateTrip(trip)).toEqual({
      valid: false,
      errors: ['Title is required']
    });
  });

  it('rejects end date before start date', () => {
    const trip = createTrip({
      startDate: '2024-03-15',
      endDate: '2024-03-10'
    });
    expect(validateTrip(trip).errors).toContain('End date must be after start date');
  });
});
```

### 3. Component Behavior (Medium Priority)
User interactions, conditional rendering.

```typescript
describe('TripCard', () => {
  it('displays trip title and destination', () => {
    render(<TripCard trip={mockTrip} />);

    expect(screen.getByText('Paris Adventure')).toBeInTheDocument();
    expect(screen.getByText('Paris, France')).toBeInTheDocument();
  });

  it('calls onEdit when edit button clicked', async () => {
    const onEdit = vi.fn();
    render(<TripCard trip={mockTrip} onEdit={onEdit} />);

    await userEvent.click(screen.getByRole('button', { name: /edit/i }));

    expect(onEdit).toHaveBeenCalledWith(mockTrip.id);
  });

  it('shows archive button only for completed trips', () => {
    const completedTrip = { ...mockTrip, status: 'completed' };
    render(<TripCard trip={completedTrip} />);

    expect(screen.getByRole('button', { name: /archive/i })).toBeInTheDocument();
  });
});
```

### 4. Hooks (Medium Priority)
Custom hooks with React Testing Library.

```typescript
describe('useTrips', () => {
  it('fetches trips on mount', async () => {
    const { result } = renderHook(() => useTrips());

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.trips).toHaveLength(3);
  });

  it('handles fetch errors', async () => {
    server.use(
      rest.get('/api/trips', (req, res, ctx) => res(ctx.status(500)))
    );

    const { result } = renderHook(() => useTrips());

    await waitFor(() => {
      expect(result.current.error).toBe('Failed to load trips');
    });
  });
});
```

### 5. Integration Tests (Lower Priority but High Value)
Full user flows.

```typescript
describe('Trip Creation Flow', () => {
  it('creates a new trip and shows it in the list', async () => {
    render(<App />);

    // Click create button
    await userEvent.click(screen.getByRole('button', { name: /new trip/i }));

    // Fill form
    await userEvent.type(screen.getByLabelText(/title/i), 'Tokyo Trip');
    await userEvent.type(screen.getByLabelText(/destination/i), 'Tokyo, Japan');

    // Submit
    await userEvent.click(screen.getByRole('button', { name: /create/i }));

    // Verify trip appears
    await waitFor(() => {
      expect(screen.getByText('Tokyo Trip')).toBeInTheDocument();
    });
  });
});
```

## Mocking Strategies

### Mock External Services

```typescript
// __mocks__/firebase.ts
export const mockFirestore = {
  collection: vi.fn(),
  doc: vi.fn(),
  getDoc: vi.fn(),
  setDoc: vi.fn(),
};

// In test
vi.mock('@/services/firebase', () => ({
  db: mockFirestore,
}));
```

### Mock API Responses (MSW)

```typescript
import { rest } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.get('/api/trips', (req, res, ctx) => {
    return res(ctx.json(mockTrips));
  }),
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

### Mock Minimal Dependencies

```typescript
// Bad - mocking implementation details
vi.mock('@/stores/tripStore', () => ({
  useTripStore: () => ({
    trips: mockTrips,
    fetchTrips: vi.fn(),
    // ... 20 more methods
  }),
}));

// Good - mock only what's needed
vi.mock('@/stores/tripStore', () => ({
  useTripStore: vi.fn(() => ({
    trips: mockTrips,
  })),
}));
```

## Test Helpers

```typescript
// test/factories.ts
export function createTrip(overrides: Partial<Trip> = {}): Trip {
  return {
    id: 'trip-1' as TripId,
    title: 'Test Trip',
    destination: 'Test City',
    startDate: '2024-03-01',
    endDate: '2024-03-07',
    status: 'planning',
    ...overrides,
  };
}

export function createActivity(overrides: Partial<Activity> = {}): Activity {
  return {
    id: 'activity-1' as ActivityId,
    title: 'Test Activity',
    time: '09:00',
    type: 'activity',
    ...overrides,
  };
}
```

## Naming Conventions

```typescript
describe('ComponentName', () => {
  describe('when condition', () => {
    it('should expected behavior', () => {});
  });
});

// Examples
describe('TripCard', () => {
  describe('when trip is active', () => {
    it('should display a green status badge', () => {});
    it('should show the "View Today" button', () => {});
  });

  describe('when trip is archived', () => {
    it('should display a gray status badge', () => {});
    it('should hide action buttons', () => {});
  });
});
```

## What NOT to Test

- Third-party library internals
- Simple getters/setters
- Framework behavior (React rendering)
- CSS/styling (use visual regression tools)
- Implementation details that may change
