# Patterns

## Dashboard recipe

Use when the user needs a landing page or module selector.

- centered or slightly left-aligned intro block
- grid of white cards
- each card has icon tile, strong title, short description, and directional arrow
- hover raises hierarchy with stronger border and slightly deeper shadow

Short example:

- intro block with a 2-line title and one plain-language subtitle
- 2 to 6 cards in a grid
- each card uses `bg-white`, strong border, rounded corners, and one tinted icon tile
- card CTA is implicit through the whole card click target, not a tiny button

Prompt example:

- `Use $friendly-design-theme to redesign this dashboard with a stronger intro block, clearer module cards, and the same warm operational style as the Transit On-Demand workspace.`

## Editor workspace recipe

Use for planners, builders, and review tools.

- strong title/action row at top
- content inside bordered white workspace shells
- left side for object lists or navigation
- center for core editing surface
- right side for settings, metrics, or review states

Prompt example:

- `Use $friendly-design-theme to restyle this planner/editor so it has a strong header row, compact action trays, bordered white panels, and tinted review cards.`

## Map workspace recipe

Use when the map is the primary working surface.

- left rail: projects, scenarios, filters, or stop list
- center: dominant map card
- right rail: assumptions, KPIs, warnings, detail panel, timetable
- selection sync between list and map
- keep map controls consolidated and visually quiet

Short example:

- header row with project title, compare toggle, save group
- left rail for scenarios and ordered stops
- center card for the map
- right rail for service assumptions, KPI blocks, warnings, and timetable preview
- selected stop highlights in both the rail and the map

Prompt example:

- `Use $friendly-design-theme to redesign this feature as a map-first workspace with a three-pane shell, strong map hierarchy, and right-side KPI/timetable panels.`

## KPI panel recipe

- use 3 to 5 blocks
- each block gets a tint and icon
- keep label, sublabel, and value clear
- do not overload KPI cards with paragraphs

## Compare mode recipe

- toggle in the header, not buried
- compare both visually and numerically
- keep the base option obvious
- use a second accent family for alternate scenarios

## Empty/loading states

- empty state should still look like part of the workspace
- loading state should be lightweight and centered
- do not replace the whole screen with a dead blank area if a map is expected

## Adaptation rule

Copy the family resemblance, not the exact screen:

- dashboards keep the card grammar
- map tools keep the three-pane shell
- form-heavy tools keep the header/action language and card hierarchy
- do not force a map pattern onto a non-map feature
