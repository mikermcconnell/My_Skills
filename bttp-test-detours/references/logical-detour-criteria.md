# Logical Detour Criteria

Use these rules before adding a BTTP simulated detour preset or fixture.

## Required Shape

A logical test detour has:

- a closed regular-route segment with two or more points;
- an entry point where the bus leaves the regular route;
- a downstream exit point where the bus rejoins the regular route;
- a bypass path that follows plausible streets in travel order;
- a simple local closure story: "this road is closed, so the bus uses these nearby streets";
- one continuous rider-facing path from entry to the natural service rejoin point, or to the exit point when those are the same.

Entry and exit points are service-boundary anchors. They describe the affected regular-route span, but they are not always mandatory bus-driving waypoints. If the bus naturally resumes regular service before the artificial closure endpoint, the likely path should stop or continue at that natural rejoin instead of adding a turn only to touch the endpoint.

For route variants, "opposite direction" is not enough by itself. Check the operating pattern. If a variant would continue straight on the rejoin street during the detour, the likely path must continue straight; do not mirror a sibling path and create a fake turn onto the closed or skipped street.

## Local Workaround Rule

For normal/regular detour presets, the path must look like an operator's local workaround for a road closure.

Before publishing, verify:

- the entry and exit are near the closed segment, not several neighbourhoods away;
- the bypass uses nearby parallel or connector streets;
- the detour path stays in the same local corridor as the closure;
- the path shows what the bus would actually drive, not a geometry-cleanup move to hit an endpoint;
- the last movement is operationally sensible and is not only there to make the geometry reach a route anchor;
- the path does not cross or borrow unrelated route corridors unless that is the intentional test case;
- the map view makes the closure and workaround obvious without explanation.

If the route swings far away, loops through an unrelated area, or visually tangles with other route lines, reject it and choose a smaller/local closure instead.

## Reject These Paths

Do not publish a rider-facing likely path when any of these are true:

- **Out-and-back:** the path leaves the route, turns around, and returns to the same area without bypassing a closure.
- **Same-stop closure:** entry and exit are effectively the same stop or intersection, with no real skipped route span.
- **Tiny span, long path:** the closed span is tiny but the alternate path is long, especially with no skipped segment.
- **Closed-route overlap:** the likely path materially reuses the skipped/closed segment.
- **Unanchored path:** no credible entry, exit, skipped segment, or affected route context exists.
- **Non-local workaround:** the bypass travels far outside the closure area, crosses unrelated route corridors, or looks like a scenic loop rather than a local road closure detour.
- **Route-corridor tangle:** the detour line becomes visually confused with unrelated route geometry, making it unclear which route is detoured.
- **Forced endpoint touch:** the path adds an unnecessary turn or connector only to reach the artificial detour endpoint after the bus has already resumed regular service.
- **Mirrored variant error:** a paired route variant copies the sibling direction and creates a turn the bus would not make in service.
- **Loop confusion:** a loop route rejoins near the start because the wrong pass of the loop was selected.
- **Stale preservation:** old trusted geometry is kept even after newer GPS or synthetic evidence points to a different corridor.

## Synthetic Path Rules

Synthetic detours are allowed for local testing when they are intentionally test-only.

- Prefer real intersections and road names over arbitrary offsets.
- Use a simple bypass around a realistic closure.
- Prefer short rectangular or nearby-parallel bypasses over long multi-neighbourhood paths.
- Do not use a road just because it connects; use it only if it explains the closure cleanly to a rider.
- Keep waypoint order in the same direction the route travels.
- Do not force the first or last waypoint to be the closure endpoint when the operational service rejoin/start is nearby on the regular route.
- For paired directions such as `12A`/`12B`, build each route separately. Mirror only when the operating pattern truly mirrors.
- Do not use generic perpendicular offsets if they create impossible geometry or force road matching into an out-and-back route.

## Rider-Facing Field Rules

For a runnable preset:

- Set `vehicleCount` high enough to behave like a confirmed detour in local testing, normally `2`.
- Set confidence and road-match metadata honestly, usually `high` for hand-authored presets and `dev-simulation` or preset-specific source names.
- Mirror top-level geometry into `segments[0]`.
- Keep `canShowDetourPath` implicit only if existing code already does so safely; otherwise set it deliberately when adding new behavior.
- Suppress or omit likely path fields if the detour is intentionally geometryless.

## Final Check

Before finishing, answer yes to all:

- Would a rider understand why the bus leaves and rejoins the route?
- Does the map show a simple local workaround, not a big swing or confusing route tangle?
- Does the path avoid the closed route section?
- Is the direction correct for this route variant?
- Does the final turn match what a bus would actually do, especially near the rejoin point?
- Would this catch the failure the user cares about?
- Is it clearly marked as simulated/test-only?
