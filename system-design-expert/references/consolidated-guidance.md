# Consolidated interface design guidance

Read this when a design introduces or changes an API, shared contract, module boundary, event, or stored schema.

- Identify consumers and compatibility requirements before changing the interface.
- Prefer the smallest stable contract; keep implementation details private.
- Define input validation, error shapes, pagination, timeouts, retries, and idempotency where relevant.
- Make naming and optional-versus-required fields consistent.
- Plan versioning and migration before breaking an existing consumer.
- Add contract tests at trust boundaries.
