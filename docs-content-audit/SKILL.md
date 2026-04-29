---
name: docs-content-audit
description: Audit repository Markdown and agent-facing documentation for best-practice context hygiene, load order, portability, drift, contradictions, and durable-vs-archive separation. Use when reviewing README, AGENTS.md, context index files, product vision, architecture docs, schema docs, plan folders, or any request to assess whether docs are current, agent-friendly, or at best-practice level, and when cleaning up those docs afterward.
---

# Docs Content Audit

Use this skill to review a repository's Markdown and agent-facing context as an operating system for future agents, not just as prose.

## Workflow

1. Start with the doc entrypoints.
   Identify `AGENTS.md`, README, context index files, locked-logic or rules docs, product vision, architecture, and schema docs before reading lower-value material.

2. Verify the context hierarchy.
   Check whether the repo has one clear top-level agent contract.
   Confirm the read order is explicit and consistent across entrypoints.
   Flag split authority when multiple files appear to be competing instruction sources.

3. Check durable versus archival boundaries.
   Confirm that plan/history/archive folders are clearly marked as non-default context.
   Flag durable docs that still contain roadmap churn, status notes, dated handoffs, or tool-specific execution noise.

4. Check portability.
   Prefer repo-agnostic guidance in durable docs.
   Flag tool-specific instructions when they sit in the default context path instead of a tool-specific supplement.

5. Check reality drift.
   Compare product vision and architecture claims against the actual repo layout and implementation surface.
   Look for stale backend claims, removed modules that are still documented, missing major subsystems, and incorrect file references.

6. Check agent usability.
   Ask whether a fresh agent could answer:
   - what to read first
   - what not to trust by default
   - what behavior is locked
   - where current source of truth lives
   - which docs are durable versus historical

7. Report findings by severity.
   Lead with correctness and authority problems first, then portability and maintainability issues, then polish.

8. If asked to clean up, edit in this order:
   - top-level agent contract and load order
   - contradictions in durable docs
   - durable-vs-archive boundaries
   - stale metadata, status noise, and unnecessary churn

## Decision Rules

- Treat contradictory architecture guidance as a high-severity issue.
- Treat split agent entrypoints as an important issue unless the layering is explicit.
- Prefer one durable source of truth per concern.
- Keep Tier 1 docs concise and stable.
- Move tool-specific workflow to tool-specific supplements when possible.
- Do not rewrite every doc. Fix the leverage points first.

## Typical Files

- `AGENTS.md`
- `README.md`
- `docs/CONTEXT_INDEX.md`
- `docs/rules/*.md`
- `docs/PRODUCT_VISION.md`
- `docs/ARCHITECTURE.md`
- `docs/SCHEMA.md`
- `docs/plans/README.md`
- `docs/archive/README.md`

## Cleanup Standard

After cleanup, the repo should have:

- one clear top-level agent entrypoint
- an explicit load order
- durable docs that describe current reality
- archive/plan folders clearly demoted from default context
- minimal tool-specific leakage in durable context

## Output Standard

For reviews:
- list findings first, ordered by severity
- cite exact files and lines when possible
- state whether the repo is at best-practice level or not

For cleanup:
- state what hierarchy or contradiction you are fixing before editing
- summarize the new agent-context model after edits
- note any remaining drift that was intentionally left for later
