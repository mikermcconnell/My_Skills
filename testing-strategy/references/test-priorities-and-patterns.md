# Test Priorities and Patterns

## Arrange-Act-Assert

Use a clear structure:
- Arrange the data and dependencies
- Act by executing the target behavior
- Assert the outcome that matters

## What to test first

Prioritize:
1. pure functions
2. business logic and validation
3. component behavior and user interaction
4. hooks or stateful units
5. integration flows

## Naming guidance

Good test names describe the outcome and condition clearly.
Examples:
- returns "1 day" for single-day trips
- shows archive button only for completed trips
- rejects end date before start date

## What not to test

Avoid spending time on:
- trivial getters/setters
- framework internals
- styling details that don't affect behavior
- duplicate tests for the same rule in every layer
