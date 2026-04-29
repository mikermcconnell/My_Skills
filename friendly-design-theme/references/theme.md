# Theme

## Visual thesis

This theme should feel:

- warm rather than sterile
- operational rather than marketing-driven
- polished rather than flashy
- dense enough for working users, but still easy to scan

The closest reference is the Transit On-Demand workspace in Scheduler 4.

## Reference images

Use these only when visual precision matters:

- `assets/transit-ondemand-workspace.png`
- `assets/transit-ondemand-fullpage.png`
- `assets/transit-ondemand-header-actions.png`
- `assets/transit-ondemand-kpis.png`
- `assets/budgetme-desktop.png`
- `assets/budgetme-hero-crop.png`

Interpretation:

- Transit On-Demand images are the primary reference for workspace shell, card hierarchy, and control styling.
- BudgetMe is a secondary reference for warmth, friendliness, and polished consumer-facing softness.

## Core visual traits

- soft gray workspace background
- white cards with strong borders
- `rounded-2xl` and `rounded-3xl` surfaces
- compact control clusters in pale gray trays
- bold headings and visible section labels
- tinted KPI/status cards in blue, green, amber, and violet
- strong selected-state styling

## Color roles

- Blue: active selection, linked actions, map-linked emphasis
- Green: feasible, saved, complete, positive outcomes
- Amber: warnings, constraints, review attention
- Violet/Indigo: compare mode, scenario thinking, planning intelligence
- Gray: framing, structure, inactive controls

## Layout density

- Prefer compact but comfortable spacing
- Keep panels visually separated with borders, not large empty space
- Favor visible section headers over minimalist ambiguity
- Keep primary actions grouped and easy to locate

## Tailwind direction

Common treatments:

- workspace: `bg-[#F7F7F7]` or `bg-gray-50`
- primary card: `bg-white rounded-3xl border-2 border-gray-200 shadow-sm`
- control tray: `bg-gray-50 rounded-lg border border-gray-100 p-1`
- active segmented control: `bg-white shadow-sm text-brand-blue`
- KPI block: `rounded-2xl border-2 p-3` with tinted background

## Typography

- strong page title
- short descriptive subtitle
- section labels in uppercase tracking
- metric numbers bold and easy to compare
- small helper text only where it improves decisions

## Interaction cues

- selected items must be unmistakable
- hover states should clarify clickability without being noisy
- active pills and tabs should feel tactile
- save / duplicate / export actions should live in compact action groups

## Anti-patterns

- default startup-app look with low-contrast gray-on-white everywhere
- oversized hero layouts on working screens
- borderless cards
- weak selected states
- map and side panels competing equally for attention on map-first tasks
