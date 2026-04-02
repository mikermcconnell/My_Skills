---
name: refactoring-safely
description: Safe refactoring patterns with verification steps. Use when restructuring code, extracting functions, renaming, or reorganizing without changing behavior.
---

# Safe Refactoring Patterns

## Core Principles

1. **Behavior preservation**: Refactoring changes structure, not behavior
2. **Small steps**: One change at a time, verify between steps
3. **Tests first**: Ensure tests pass before and after
4. **Reversibility**: Each step should be easily undoable

## Pre-Refactoring Checklist

- [ ] Existing tests pass
- [ ] Understand current behavior fully
- [ ] Identify all callers/usages
- [ ] Plan the refactoring steps
- [ ] Commit current state (clean starting point)

## Common Refactoring Patterns

### Extract Function

**When**: Code block does one logical thing and is reusable or complex.

```typescript
// Before
function processOrder(order: Order) {
  // validate order
  if (!order.items.length) throw new Error('Empty order');
  if (!order.customerId) throw new Error('No customer');
  // ... more validation

  // calculate total
  const subtotal = order.items.reduce((sum, item) => sum + item.price, 0);
  const tax = subtotal * 0.1;
  const total = subtotal + tax;
  // ... rest
}

// After
function validateOrder(order: Order): void {
  if (!order.items.length) throw new Error('Empty order');
  if (!order.customerId) throw new Error('No customer');
}

function calculateOrderTotal(items: OrderItem[]): number {
  const subtotal = items.reduce((sum, item) => sum + item.price, 0);
  const tax = subtotal * 0.1;
  return subtotal + tax;
}

function processOrder(order: Order) {
  validateOrder(order);
  const total = calculateOrderTotal(order.items);
  // ... rest
}
```

### Extract Component (React)

**When**: UI section is self-contained, reusable, or component is too large.

```typescript
// Before: 300-line component with embedded list rendering

// After: Extract the list item
function ActivityCard({ activity, onEdit }: ActivityCardProps) {
  return (/* ... */);
}

// Parent becomes cleaner
function ActivityList({ activities }: Props) {
  return activities.map(a => <ActivityCard key={a.id} activity={a} />);
}
```

### Extract Hook

**When**: Component has complex state logic that can be reused.

```typescript
// Before: Complex state in component
function TripPlanner() {
  const [trips, setTrips] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetchTrips().then(setTrips).catch(setError).finally(() => setLoading(false));
  }, []);
  // ...
}

// After: Extract to hook
function useTrips() {
  const [trips, setTrips] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetchTrips().then(setTrips).catch(setError).finally(() => setLoading(false));
  }, []);

  return { trips, loading, error };
}

function TripPlanner() {
  const { trips, loading, error } = useTrips();
  // ...
}
```

### Rename Symbol

**When**: Name doesn't reflect purpose or is misleading.

**Steps**:
1. Use IDE rename (F2 in VS Code) to catch all references
2. Update comments and documentation
3. Check string references (dynamic access, tests)
4. Verify no runtime errors

### Move to Module

**When**: Function/type belongs with related code.

**Steps**:
1. Create the destination file if needed
2. Copy the code to new location
3. Add export statement
4. Update imports in old location to re-export (temporary)
5. Find and update all external imports
6. Remove re-export from old location
7. Verify no circular dependencies

## Verification Steps

After each refactoring step:

1. **TypeScript**: `npm run type-check` - no new errors
2. **Tests**: `npm test` - all pass
3. **Lint**: `npm run lint` - no new warnings
4. **Manual**: Quick smoke test of affected feature
5. **Commit**: Small commit with clear message

## Red Flags During Refactoring

- Changing behavior "while we're at it" - don't mix refactoring and features
- Skipping verification steps - always verify
- Large refactors without commits - commit frequently
- Ignoring failing tests - fix before continuing
- Assuming IDE rename caught everything - verify manually

## Rollback Strategy

If something breaks:
1. `git stash` current changes
2. `git checkout .` to clean working directory
3. Analyze what went wrong
4. Plan smaller steps
5. Try again
