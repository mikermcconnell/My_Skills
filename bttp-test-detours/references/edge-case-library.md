# BTTP Detour Edge Case Library

Use this reference when a requested test detour resembles a known BTTP failure mode.

## Same-Stop Out-and-Back

Risk: a route leaves and returns near the same stop, making the map show a purple loop that is not a real detour.

Guardrail:

- Require distinct entry and exit anchors.
- Require a real closed route span.
- Do not preserve old likely geometry from this kind of segment.

## Tiny-Span Long Path

Risk: a very short closed span produces a long alternate path because the wrong rejoin was selected.

Guardrail:

- Suppress likely/inferred path if the skipped span is tiny and no credible skipped segment exists.
- Prefer active alert without path over misleading geometry.

## Downtown Loop Routes

Risk: loop routes such as downtown variants can pass near the same place more than once, so entry/exit projection can select the wrong side of the loop.

Guardrail:

- Keep route progress in mind.
- Choose the downstream rejoin that creates a plausible closure.
- Avoid matching a later point near the original entry unless that is the actual detour.

## Road-Match Closed Overlap

Risk: OSRM or preserved likely paths reuse the closed segment, telling riders the bus travels through the closure.

Guardrail:

- Check interior likely-path points against the skipped segment.
- If overlap is material, suppress the path and set/expect a clear suppressed reason in implementation work.
- Ensure the client cannot fall back to stale top-level geometry when segment geometry is suppressed.

## Forced Endpoint Touch After Rejoin

Risk: the likely path adds a fake final turn only because the entry/exit anchor was treated as a mandatory driving waypoint.

Guardrail:

- Treat entry/exit anchors as service-boundary markers.
- Let the likely path end where the bus naturally resumes regular service.
- Keep the closed/skipped segment separate from the bus-driven path.
- Accept a modest road-match endpoint mismatch only when the mismatched endpoint is still on the regular-route corridor.

## Stale Published Path

Risk: an old path remains trusted after newer evidence indicates a different corridor.

Guardrail:

- Prefer newer GPS-confirmed or explicitly authored test geometry.
- Prevent preservation of older likely paths when replacing a simulated preset.
- Clear the simulated detour before republishing during manual checks.

## Short Detour With No Skipped Stops

Risk: a valid short detour gets rejected because no stops are skipped, or it imports distant official-notice stops.

Guardrail:

- Allow a short, GPS/logically confirmed detour without skipped stops.
- Keep stop impacts empty when no stop is truly skipped.
- Do not pull in distant notice impacts for a test preset unless that is the scenario being tested.

## Route-Family / Paired Direction Detours

Risk: one route variant's path is copied to a sibling direction with the wrong ordering.

Guardrail:

- Build each direction's waypoint order separately.
- Keep road names directionally correct.
- Check whether each variant naturally continues on the rejoin street instead of turning to touch the closure endpoint.
- Verify each route document independently in tests.

## Variant Rejoin Continuation

Risk: a route variant is forced to turn onto the closed/skipped street after rejoining, even though a real bus would continue straight and resume regular service.

Guardrail:

- Add a service rejoin point when it differs from the artificial closure endpoint.
- Keep `skippedSegmentPolyline` anchored to the closed regular-route span.
- Make `likelyDetourPolyline` follow the bus-driven movement only.
- Add a regression test that the final likely-path point is the service rejoin point, not the artificial exit anchor.

## Non-Local Workaround / Route-Corridor Tangle

Risk: a synthetic preset technically connects valid roads, but the bus appears to swing far away, loop through an unrelated area, or tangle with other route corridors. Riders cannot tell what road is closed or why the bus would use that path.

Guardrail:

- Treat regular presets as small local road-closure workarounds.
- Keep entry and exit near the closed segment.
- Prefer nearby parallel streets and short connectors.
- Reject paths that cross unrelated route corridors, pass through unrelated hubs, or visually look like another route.
- If road matching produces a large loop or endpoint mismatch, use a better local hand-authored path or do not publish a likely path.
