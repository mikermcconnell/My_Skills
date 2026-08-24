# Consolidated feature delivery guidance

Read this for non-trivial work that needs requirements, sequencing, source verification, or migration planning.

1. Define the user outcome, constraints, acceptance checks, and protected behavior.
2. Verify unfamiliar framework or API decisions against authoritative sources.
3. Break work into independently verifiable slices; keep one slice active at a time.
4. Implement the smallest end-to-end slice and test it before expanding.
5. When replacing behavior, define compatibility, migration, rollback, and removal timing.
6. Update durable documentation only when the source of truth actually changed.
