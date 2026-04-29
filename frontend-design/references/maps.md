# Map Interfaces

Use this reference for map-heavy pages, locator tools, spatial dashboards, and any UI where a map and list need to work together.

## Core Principle

Treat the map as a working surface, not as decorative wallpaper. Decide whether the map or the list is primary for the task, then size and order the layout around that choice.

## Common Shells

- Desktop browse flow: map plus results list with filters above or to the left
- Desktop detail flow: map plus sticky detail panel for the selected feature
- Mobile flow: stacked search, filters, map preview, and results list with a fast way to jump back to the map

Do not let filters, legends, popups, and floating controls compete for the same corner.

## Interaction Rules

- Keep selection synchronized across map markers, result cards, and detail panes.
- Make the selected feature visually unmistakable.
- Reserve space for legends, active filters, and a reset control.
- Handle empty, loading, and no-permission states deliberately.
- Use clustering or aggregation when marker density is high.
- Keep popups short; move deeper information into a side panel or drawer.

## Visual Rules

- Keep map chrome quiet so the data and overlays stay legible.
- Use one accent color family for selection and one muted system for secondary layers.
- Ensure markers are readable against both light and dark basemap regions.
- Use cards, legends, and filter panels with enough contrast to read over the map.

## Mobile Notes

- Assume the list becomes more important on small screens.
- Keep the search and filter affordances thumb-reachable.
- Avoid full-screen map experiences that trap the user away from results.

## Quick Check

- Can a user understand what is selected at a glance?
- Can they recover from a filtered or zoomed-in dead end?
- Does the map still feel usable when data volume grows?
