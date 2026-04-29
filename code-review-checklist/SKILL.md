---
name: code-review-checklist
description: Review pull requests, diffs, or code changes with a risk-based checklist that prioritizes correctness, regressions, security, performance, and maintainability. Use when doing code review, PR review, code audit, or when the user wants high-signal review comments instead of generic feedback.
---

# Code Review Checklist

Use this skill to produce code reviews that are practical, evidence-based, and focused on real risk.

## Workflow

1. Understand the change before judging it.
   - Identify what changed, why it changed, and which files carry the real risk.
   - Use repo docs, surrounding code, tests, and changed-file context before making strong claims.
2. Review in this order unless the task clearly calls for something else.
   - correctness and regression risk
   - security and data exposure
   - data integrity and state consistency
   - performance and scalability
   - maintainability and clarity
   - tests, observability, and rollout safety
3. Prioritize findings by user and business impact.
   - Start with bugs, unsafe behavior, broken assumptions, and hard-to-reverse changes.
   - Do not lead with style nits if there are correctness or safety risks.
4. Write evidence-based comments.
   - Point to the specific behavior, file, or code path that causes the concern.
   - Explain the consequence and suggest a fix or a question when possible.
5. Be selective.
   - Do not pad the review with obvious lint-level remarks unless they materially affect readability or risk.

## Core review checks

### 1. Correctness and regressions

- [ ] The change appears to do what it claims to do
- [ ] Edge cases, failure paths, and empty states are handled
- [ ] Existing behavior is not accidentally broken
- [ ] Business rules and domain constraints are preserved
- [ ] Renames, refactors, and moved logic did not change behavior unintentionally
- [ ] Time, date, locale, timezone, and ordering logic are handled safely where relevant
- [ ] Concurrency, async ordering, retries, or race conditions are considered where relevant

### 2. Security and privacy

- [ ] No hardcoded secrets, API keys, tokens, or credentials
- [ ] User input is validated, sanitized, and bounded appropriately
- [ ] Authn and authz checks still protect the intended resources
- [ ] Sensitive data is not exposed in logs, errors, client payloads, or analytics
- [ ] Queries, commands, templates, and file handling are safe from injection-style issues
- [ ] External calls use safe protocols and reasonable trust boundaries

### 3. Data integrity and state safety

- [ ] Writes preserve valid state and do not leave partial corruption on failure
- [ ] Schema changes, migrations, and defaults are backward compatible or explicitly managed
- [ ] Idempotency, deduplication, and transaction boundaries are appropriate where needed
- [ ] Cache invalidation, derived state, and synchronization logic are coherent

### 4. Performance and scalability

- [ ] No obvious N+1, repeated expensive work, or unnecessary network chatter
- [ ] Large lists, heavy queries, and expensive rendering paths are handled appropriately
- [ ] Memory, bundle size, and startup/runtime cost are reasonable for the change size
- [ ] New polling, retries, or background work are justified and bounded

### 5. Maintainability and clarity

- [ ] The design matches project conventions and surrounding architecture
- [ ] Names, boundaries, and responsibilities are clear
- [ ] The change avoids duplicate logic and hidden coupling
- [ ] Complex logic is explained at the right level when the code alone is not obvious
- [ ] Dead code, commented-out code, and accidental debug leftovers are removed

### 6. Tests, observability, and rollout safety

- [ ] Important new behavior or bug fixes are covered by tests when appropriate
- [ ] Tests meaningfully exercise the risk, not just the happy path
- [ ] Logging, metrics, or error context are sufficient to debug failures where needed
- [ ] Feature flags, migrations, config changes, and deployment sequencing are safe where relevant

### 7. Stack-specific checks when applicable

Only apply these when the technology is actually in scope.

#### TypeScript

- [ ] Types are specific enough to prevent misuse
- [ ] `any` is avoided unless there is a clear reason
- [ ] Nullability and optional values are handled deliberately

#### React

- [ ] Hooks follow the rules and dependency handling is intentional
- [ ] Effects, subscriptions, and timers clean up correctly
- [ ] Rendering work and state placement are appropriate for the component
- [ ] Accessibility and keyboard behavior are preserved in interactive UI

## Comment quality rules

Good review comments usually include:
- what the issue is
- why it matters
- how severe it is
- a suggested fix or a focused question

Avoid:
- speculative claims without evidence
- generic praise that does not help the author
- style-only comments when higher-risk issues exist
- demanding rewrites without explaining the tradeoff

## Review response format

```markdown
## Summary
Short overview of what changed and the overall risk level.

## Strengths
- What is solid or well-handled

## Findings
### Critical
- Issues that can cause broken behavior, unsafe access, data loss, or high-risk regressions

### Important
- Issues that should be fixed for maintainability, performance, or incomplete handling

### Minor
- Lower-priority improvements, polish, or follow-up suggestions

## Questions
- Focused clarifications that affect confidence in the review
```

## Default behavior

If context is limited, say what you inspected and lower confidence where needed.
Prefer a small number of high-signal findings over a long checklist dump.
