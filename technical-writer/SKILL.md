---
name: technical-writer
description: Draft or improve developer-facing documentation including READMEs, setup guides, API docs, tutorials, migration notes, and docs-as-code structure. Use when the user needs code explained for other developers, technical docs written or rewritten, onboarding clarified, workflows documented, or migration or release notes produced.
---

# Technical Writer

Use this skill when the audience is another engineer, operator, or technical user who needs clarity fast.

## Workflow

1. Identify the reader and job-to-be-done.
   Distinguish:
   - evaluator deciding whether to use the thing
   - new contributor trying to run it
   - integrator calling an API
   - operator handling deployment or migration

2. Write for fastest successful action.
   Start with:
   - what this is
   - why it exists
   - shortest path to success

3. Separate concepts from procedures.
   Keep explanations, setup steps, API details, and troubleshooting in distinct sections.

4. Prefer concrete examples over abstract description.
   Use realistic commands, payloads, inputs, and expected outputs.

5. Verify against the code when possible.
   Do not document behavior that the repo does not actually implement.

## Rules

- Optimize for scanning and successful execution.
- Use active voice and direct wording.
- Keep prerequisite assumptions explicit.
- Do not bury the quick start under theory.
- Treat stale or inaccurate docs as defects.
- When documenting changes, call out what broke and what users need to do differently.

## Gotchas

- Don't document behavior you did not verify.
- Don't bury the quick start under architecture explanation.
- Don't mix tutorial, reference, and troubleshooting into one undifferentiated blob.
- Don't leave prerequisites, versions, or environment assumptions implicit.
- Don't use toy examples when a realistic example would prevent confusion.

## Common Output Shapes

- README:
  - what it is
  - why it matters
  - quick start
  - main workflows
  - config/reference
  - troubleshooting

- Tutorial:
  - what the user will build
  - prerequisites
  - step-by-step flow
  - verification points
  - next steps

- Migration guide:
  - who is affected
  - breaking changes
  - before/after examples
  - step-by-step upgrade path
  - rollback notes

- API documentation:
  - purpose
  - auth/prereqs
  - request shape
  - response shape
  - errors
  - working examples

## Checklist

- Who is this for?
- Can the first successful step be found in seconds?
- Do the examples match reality?
- Are failure cases and prerequisites explicit?
- Is the structure separated cleanly enough to skim?
