# React and Function Typing

## Function typing

- Give public functions explicit return types when it improves clarity.
- Use named callback types when they are reused.
- Keep parameter and return contracts obvious.

## React props

- Type props at the component boundary.
- Model optional props honestly.
- Keep callback signatures specific.
- Avoid prop types that try to represent impossible states.

## Common mistakes

- using non-null assertions casually
- widening literals unintentionally
- casting dynamic JSON straight into app models
- using a broad object type where a narrow domain type is available
