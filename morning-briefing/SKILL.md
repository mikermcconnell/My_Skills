---
name: morning-briefing
description: Generate a structured daily briefing from priorities, calendar context, and pending work. Use when the user wants a morning brief, daily priorities, a start-of-day overview, or asks what they should focus on today.
---

# Morning Briefing

Create a concise start-of-day brief that turns today's context into clear priorities, watch-outs, and sensible next moves.

## Context expectations

Use available calendar, task, and priority context when present.
If key context is missing, say so and build the best brief possible from what is available.

## Use these references

Read only what you need:
- `references/daily-brief-template.md` for the output shape
- `references/priority-selection-rules.md` for how to choose what matters most today

## Workflow

1. Gather today's meetings, deadlines, priorities, and pending items.
2. Identify the top priorities for the day.
3. Flag collisions, risks, and things likely to slip.
4. Suggest useful quick wins and preparation tasks.
5. Produce a brief the user can scan in under a minute.

## Core rules

- Prioritize the day, don't just summarize it.
- Distinguish urgent, important, and nice-to-do.
- Flag stale context or missing inputs when it affects confidence.
- Keep the brief practical and action-oriented.
- Favor clarity over completeness.

## Gotchas

- Don't repeat yesterday's plan with superficial edits.
- Don't confuse a busy calendar with a good priority list.
- Don't hide deadlines or risky items below filler.
- Don't invent calendar events or commitments you cannot verify.
- Don't let the brief become a generic productivity sermon.
