# Consolidated test design guidance

Read this when adding behavior or choosing test coverage.

- Start with a failing test when the expected behavior can be expressed reliably.
- Use arrange–act–assert and name the behavior, not the implementation.
- Prefer observable outputs and real boundaries over private-method assertions.
- Mock unstable or expensive boundaries, not the unit's essential behavior.
- Cover the happy path, meaningful edge cases, and the reported regression.
- Keep tests deterministic and prove they fail for the intended reason before trusting them.
