---
name: friendly-design-theme
description: Use when the user wants the warm, polished Scheduler 4 / Transit On-Demand visual language, either as a full theme or layered onto another front-end skill. Triggers include "Friendly design theme", "use the Shuttle Planner theme", "copy the Transit On-Demand workspace design", "same theme as On Demand", "friendly workspace UI", or any request to apply this specific rounded, high-contrast operational design system.
---

# Friendly Design Theme

Use this skill to apply the visual system established by the Transit On-Demand workspace in Scheduler 4 across other apps and features.

## Use This Skill When

- the user explicitly names `Friendly design theme`
- the user asks to copy the Transit On-Demand workspace look
- the user wants the Shuttle Planner / Planning Data theme reused elsewhere
- the task is a dashboard, editor, planner, or map workspace that should feel warm, polished, and operational instead of generic

## Workflow

1. Inspect the existing app first. Preserve product structure and only apply this theme where it fits.
2. If the repo contains the original reference implementation, inspect it before editing.
3. Read `references/theme.md` for the visual system.
4. Read `references/patterns.md` for layout recipes that match the task.
5. If the user wants a close visual match, inspect the screenshots in `assets/` before editing.
6. Apply the theme to the task at hand. Copy the feel and hierarchy, not irrelevant screen structure.
7. Keep the UI practical: high readability, strong actions, obvious selection state, and fast scanability.

## How To Maintain This Theme

- Keep this skill separate from general front-end skills. It is a named house style, not a catch-all design skill.
- Layer it with `ux-architect` for structure, `ui-designer` for polish, `frontend-developer` for implementation, and `whimsy-injector` for personality when needed.
- Reach for this skill only when the user wants this exact family resemblance, not for every redesign.

## Core Rules

- Favor bright workspaces with soft gray framing and white cards.
- Use rounded corners generously, but keep borders visible and crisp.
- Make primary actions obvious in the first viewport.
- Use tinted KPI cards and status blocks to create hierarchy.
- Keep map chrome quiet when working on map-first screens.
- Reuse the same card and action language across dashboards, editors, and planners.

## Do Not Do This

- Do not fall back to generic SaaS styling.
- Do not use flat white pages with weak hierarchy.
- Do not scatter floating controls around the map.
- Do not overuse gradients, glassmorphism, or decorative motion.
- Do not copy the exact Transit On-Demand layout when the task needs a different structure.

## Pattern Selection

- For overall visual direction and tokens: read `references/theme.md`
- For dashboard, editor, and map workspace layouts: read `references/patterns.md`
- For visual reference images: inspect `assets/budgetme-desktop.png`, `assets/budgetme-hero-crop.png`, `assets/transit-ondemand-workspace.png`, `assets/transit-ondemand-fullpage.png`, `assets/transit-ondemand-header-actions.png`, and `assets/transit-ondemand-kpis.png`
