# Strict Typing Patterns

## Avoiding any

- Prefer `unknown` for dynamic values.
- Narrow unknown values with type guards.
- Constrain generics when the function depends on known fields.

## Branded types

Use branded types for IDs or special strings when mixing them would be dangerous.
Typical cases:
- TripId vs ActivityId
- UserId vs OrganizationId

## Null safety

Use:
- optional chaining for safe access
- nullish coalescing for real defaults
- explicit checks when absence changes behavior

## Interface vs type

- interfaces work well for extendable object shapes
- types work well for unions, intersections, mapped types, and aliases

## Discriminated unions

Prefer them when a value has distinct valid states with different fields.

## Utility types

Useful patterns include:
- Pick
- Omit
- Partial
- Record
- ReturnType
