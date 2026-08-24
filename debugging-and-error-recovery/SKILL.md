---
name: debugging-and-error-recovery
description: Diagnose and fix reproducible software failures through evidence, localization, root-cause repair, regression protection, and end-to-end verification. Use when tests fail, builds break, runtime behavior is wrong, error handling is unsafe, an app crashes, or a previous fix did not hold.
---

# Debugging and error recovery

## Workflow

1. Reproduce the failure with the smallest reliable command or user flow.
2. Record the expected result, actual result, environment, and exact error.
3. Localize the first incorrect boundary rather than the loudest downstream symptom.
4. Reduce the case until one hypothesis can explain the evidence.
5. Fix the root cause without broad exception swallowing or unrelated refactoring.
6. Add a regression test that fails for the original reason.
7. Run the narrow test, relevant suite, build or type check, and real user flow as appropriate.

## Decision rules

- If reproduction is inconsistent, improve diagnostics before guessing.
- If a dependency or framework behavior is uncertain, verify it from an authoritative source.
- If the fix changes persisted data, authentication, permissions, or deployment behavior, add migration, security, and rollback review.
- Preserve narrow known-error guards and protected repository behavior.

## Error handling

Read [references/consolidated-guidance.md](references/consolidated-guidance.md) when changing error boundaries, logging, recovery, or user-facing failure messages.

## Deeper reference

Read [references/legacy-skill-2026-07.md](references/legacy-skill-2026-07.md) only when a detailed failure-specific checklist is needed.
