---
name: bttp-test-detours
description: Create realistic Barrie Transit Trip Planner (BTTP) test detours and simulated detour presets. Use when asked for a sample detour, test detour, simulated detour, detour preset, auto-detour fixture, logical detour path, or BTTP detour edge case, especially when avoiding out-and-back paths, tiny-span long paths, same-stop closures, route-overlap paths, stale likely paths, or unrealistic synthetic detours.
---

# BTTP Test Detours

Create runnable BTTP test detours that are useful for app validation and do not mislead riders in local/dev environments.

## Core Workflow

1. Ground in the BTTP repo.
   - Read `AGENTS.md`, `README.md`, `docs/API-PROXY-OPERATIONS.md`, `docs/AUTO-DETOUR-DETECTION.md`, and `docs/AUTO-DETOUR-VALIDATION-MATRIX.md` as relevant.
   - Inspect current simulation code before editing: `api-proxy/services/detourSimulation.js` and `api-proxy/__tests__/detourSimulation.test.js`.

2. Choose the right artifact.
   - For a runnable sample, add or use a simulation preset. Read `references/bttp-simulation-workflow.md`.
   - For expected-behavior checks, add ground truth or regression coverage only when needed.
   - Do not create route-specific production detour logic.

3. Design the detour path.
   - Start with route, direction, closure, entry, exit, and bypass streets.
   - Synthetic paths are allowed, but must be plausible on Barrie streets.
   - Treat every regular test detour as a simple local road-closure workaround: the bus should leave the route near the closure, use nearby parallel/connector streets, and rejoin shortly downstream.
   - Treat entry and exit as service-boundary anchors, not always mandatory driving waypoints. Do not add an unrealistic turn just to touch the artificial endpoint if the bus has already resumed regular service.
   - Do not blindly mirror paired route variants. If one variant naturally continues on the rejoin street, model that continuation instead of forcing the opposite direction's endpoint.
   - Reject big swings, scenic loops, route-family tangles, or paths that make riders ask why the bus went there.
   - Apply `references/logical-detour-criteria.md` before writing code.

4. Guard against known BTTP failures.
   - Read `references/edge-case-library.md` when the route is a loop, downtown route, short detour, road-matched detour, or route-family case.
   - Prefer hiding a likely path over publishing a misleading path.

5. Implement and verify.
   - Add/update preset geometry, metadata, route IDs, aliases, and tests.
   - Run targeted API tests, then broader related tests when geometry, publishing, or frontend display behavior changes.
   - If the user wants visual confidence, publish locally and inspect the web/native map.

## Minimum Quality Bar

A test detour is acceptable only when:

- entry and exit are distinct and ordered for the route direction;
- entry and exit sit close to the closed segment and explain a local bypass;
- the likely path follows what the bus would actually drive and may stop at a natural service rejoin instead of forcing a closure endpoint touch;
- paired or sibling variants have route-specific path ordering and service rejoin behavior, not a copied mirror when operations differ;
- the alternate path bypasses the closed segment instead of retracing it;
- the alternate path does not swing far outside the closure area or cross unrelated route corridors;
- `skippedSegmentPolyline`, `inferredDetourPolyline`, `likelyDetourPolyline`, and `segments[]` agree;
- route-specific metadata marks it as simulated/test-only;
- tests prove it stays logical and rider-renderable.

## Output Expectations

When creating or updating a preset, report:

- preset name and routes covered;
- closure and bypass streets;
- files changed;
- tests run;
- any remaining visual/manual check needed.
