# BTTP Simulation Workflow

Use this when adding or changing a runnable BTTP simulated detour preset.

## Files to Inspect

- `api-proxy/services/detourSimulation.js`
- `api-proxy/__tests__/detourSimulation.test.js`
- `api-proxy/routes/detourRoutes.js` only when endpoint behavior changes
- `docs/detour-ground-truth/` only when adding validation fixtures

## Preset Pattern

In `detourSimulation.js`:

- Add a preset constant, route defaults, and aliases.
- Add a route ID resolver if the preset can cover multiple route variants.
- Add a geometry builder with named coordinate constants.
- Return top-level geometry and matching `segments[]` geometry.
- Set `testPreset`, `simulated: true`, and `source: 'dev-detour-simulation'` through the existing document creation path.
- Use clear `title`, `description`, `detourPathLabel`, `likelyDetourRoadNames`, `confidence`, and `vehicleCount`.
- Write to the active detour collection through existing storage config helpers.

## Geometry Builder Checklist

The builder should produce:

- `shapeId`
- `entryPoint`
- `exitPoint`
- `serviceRejoinPoint` when the bus naturally resumes service somewhere different from the artificial closure endpoint
- `skippedSegmentPolyline`
- `inferredDetourPolyline`
- `likelyDetourPolyline`
- `likelyDetourRoadNames`
- `roadMatchConfidence`
- `roadMatchSource`
- `detourPathLabel`
- `confidence`
- `evidencePointCount`
- `lastEvidenceAt`
- `segments[]` with matching segment-scoped fields

Use named intersection variables instead of raw anonymous arrays so reviewers can see the route logic.


## Road Matching Rule

Hand-authored simulation presets are sparse waypoints, not dense GPS traces. When road matching is enabled, presets should prefer OSRM route snapping first and still apply the same safety gates for closed-segment overlap, endpoint mismatch, backtracking, and service rejoin behavior. Live detector GPS traces should normally keep OSRM match-first behavior.

## Endpoint Usage

Simulation is development-only:

- `DETOUR_SIMULATION_ENABLED=true`
- not `NODE_ENV=production`
- publish with `POST /api/detour-simulate`
- clear with `POST /api/detour-simulate/clear`

Prefer preset requests such as:

```json
{ "preset": "preset-name", "durationMinutes": 30 }
```

For V2, the existing storage config should write to `activeDetourEventsV2` using `simulated:<routeId>` document IDs.

## Test Expectations

Add or update tests that prove:

- the preset writes the intended route document(s);
- route variants have correct opposite-direction ordering;
- route variants have correct service rejoin behavior, including tests that prevent endpoint-only turns;
- likely path road names match the intended bypass;
- top-level and segment geometry are present;
- the geometry does not collapse into an out-and-back or tiny-span path.

Run:

```powershell
npm --prefix api-proxy test -- detourSimulation.test.js
```

Also run related tests when relevant:

- `detourRoadMatcher.test.js` for road-match/overlap behavior;
- `segmentValidity.test.js` for invalid geometry gates;
- `detourPublisher.test.js` for stale path preservation or publish fields;
- frontend detour overlay tests when client rendering rules change.

## Documentation Rule

Update BTTP detour docs only when behavior changes. A new local simulation preset usually needs tests, not source-of-truth documentation.
