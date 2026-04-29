# Web Pages

Use this reference for landing pages, editorial pages, dashboards, and general product surfaces.

## Starting Point

Decide what the page must do in the first five seconds. Typical priorities:

- persuade
- orient
- compare
- browse
- convert

Build the page so the first viewport makes that priority obvious.

## Visual Direction

Choose and enforce a direction early:

- tone: editorial, civic, playful, premium, practical, etc.
- palette: one dominant base, one accent, one highlight at most
- typography: one expressive display face and one highly readable body face
- density: roomy and magazine-like, or compact and tool-like
- motion: staggered reveals, section transitions, or no motion at all

If the repo already has a design system, strengthen it instead of replacing it.

## Layout Patterns

Use the layout that matches the job:

- Landing page: strong hero, social proof or context, feature blocks, single clear conversion path
- Dashboard: summary rail first, filters second, dense but legible cards or tables, stable layout under loading
- Editorial page: stronger hierarchy, wider reading rhythm, imagery that supports narrative rather than decoration

Avoid assembling pages from generic hero plus three cards plus CTA patterns unless that structure is actually justified.

## Implementation Notes

- Start with CSS custom properties for color, spacing, radii, shadows, and type scale.
- Rework component clusters, not isolated one-off rules.
- Design hover, focus, empty, and loading states if those states are visible to users.
- Keep image treatments intentional: crop consistently and reserve space when images are optional.
- Prefer semantic HTML before adding wrappers solely for styling.

## Quick Check

- Is the primary action visible without hunting?
- Does the typography create a real hierarchy?
- Does the page still read well on mobile?
- Do spacing and card styles feel like one system?
