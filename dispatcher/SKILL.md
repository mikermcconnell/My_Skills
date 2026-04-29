---
name: dispatcher
description: Route a user request to the best specialist skill or sequence of skills. Use when the task is broad, ambiguous, spans multiple specialist workflows, or when the user asks which skill to use, wants the best skill chosen, or needs the work broken into the right sequence.
---

# Dispatcher

Choose the best skill, or sequence of skills, for a request instead of doing all the thinking in an unstructured way.

## Use these references

Read only what you need:
- `references/routing-heuristics.md` for routing logic and common skill families
- `references/common-skill-sequences.md` for useful multi-skill combinations

## Workflow

1. Decide whether the task should be handled directly or routed.
2. If a specialist skill is clearly better, use it.
3. If several skills are relevant, choose a sequence and explain the order briefly.
4. If routing is ambiguous, ask one precise clarifying question instead of many.
5. If no specialist skill clearly helps, proceed without forcing one.

## Core rules

- Prefer the most specific useful skill over a generic one.
- Avoid stacking skills unless each one adds clear value.
- Treat routing as a way to reduce confusion and improve quality, not as ceremony.
- Be explicit when the task has two phases that want different skills.
- If a user names a skill directly, honor that unless it is clearly a bad fit.

## Gotchas

- Don't route to a specialist skill just because a keyword appears.
- Don't choose five skills when one or two will do.
- Don't ask the user to pick among skills unless that choice materially matters.
- Don't keep control of the work if a better specialist skill clearly exists.
- Don't force routing when the task is already clear and straightforward.
