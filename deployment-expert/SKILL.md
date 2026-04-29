---
name: deployment-expert
description: Practical release-readiness workflow for software repositories. Use when shipping meaningful features, fixes, refactors, dashboards, schedule logic, imports, or operationally important changes that should be checked, scoped, and made recoverable before being treated as ready.
---

# Deployment Expert

Use this skill to move changes from built to ready safely.

This skill is for the stage after implementation, testing, and validation, when the question becomes: is this safe enough to release or rely on?

## Read only what you need
- `references/release-workflow.md` for the standard release workflow, release checklist, and rollback thinking
- Use repo docs such as `AGENTS.md`, `AGENTS.md`, `ORCHESTRATOR.md`, `TESTING.md`, or deployment notes when they exist

## When to use this skill
Use this skill when:
- a feature is built and may be ready to ship
- a fix could affect existing behavior
- a release touches calculations, scheduling logic, imports, or operational outputs
- the change may affect other users or workflows
- you need to decide whether something is only built, review-ready, or operationally ready
- you need a release checklist, rollback path, or short release note

## Workflow

1. Define the change boundary
- What changed?
- What did not change?
- What is the likely release risk?

2. Check readiness inputs
- What was tested?
- What was validated?
- What regression risk remains?

3. Run a release checklist
- main flow check
- one realistic case
- one regression check
- one sanity check for the final output
- anything stakeholder-facing that needs clarity

4. Check rollback or recovery
- What is the last known good state?
- How would you undo or contain this change if it fails?
- If rollback is unclear, say so explicitly

5. Leave a short release record
Always state:
- what changed
- risk level
- release status
- rollback path
- remaining concerns

## Core rules
- Do not treat built as the same as ready
- Prefer smaller, understandable releases over large unclear bundles
- Always consider regression risk before release
- If the release matters operationally, the checklist should be explicit
- If rollback is weak, say so clearly
- A polished feature is not automatically safe to rely on

## Output format
When useful, structure your deployment output like this:
- Change summary
- Risk level
- Release checklist
- Regression concerns
- Rollback or recovery path
- Release readiness
- Short release note

## Good prompts this skill should handle
- Is this feature ready to release?
- Give me a release checklist for this change
- What do I still need to verify before shipping this?
- Help me think through rollback for this dashboard update
- Review this change for release-readiness and operational risk
