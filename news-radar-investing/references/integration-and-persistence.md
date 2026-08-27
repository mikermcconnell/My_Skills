# Mike's Integration and Persistence Rules — News Radar V3

Read this when a Radar run needs live TaskTracker, Mind Model, portfolio, underwriting-monitor, Library, or persistence context.

## Read current context

Use live data rather than remembered holdings, stale screenshots, local seeds, or hardcoded thesis wording. Never print credentials.

### TaskTracker and Mind Model

Local repository when available:

`C:\Users\Mike McConnell\Documents\mike_apps\TaskTracker`

1. Read `AGENTS.md` and apply the current `mind-model` skill.
2. Load the API key from `.env.local` without displaying it.
3. Read current production state through supported overview, project, research, thesis, watchlist, and monitor endpoints.
4. Match events to exact-company research, active underwritings, monitors, kill criteria, review dates, sector or thematic projects, thesis mechanisms, forecasts, falsifiers, watchlists, and pending proposals.
5. Treat `UNAUTHORIZED` as unavailable production state. A permitted read-only fallback may be used only when authorized and clearly labelled.
6. Local seed data explains schema; it is not confirmed live state.

### Investing portfolios

Local repository when available:

`C:\Users\Mike McConnell\Documents\mike_apps\Investing`

1. Read `AGENTS.md`, then `CLAUDE.md`.
2. Initialize Firebase only through the supported repository configuration without exposing secrets.
3. Use user-scoped portfolio and position helpers.
4. Preserve portfolio, account, lot, strategy, instrument, share class, and currency separation.
5. Normalize CDRs, Canadian wrappers, options, duplicate underlyings, and direct versus read-through exposure.
6. Use timestamped price and FX data for value, weight, P/L, or concentration claims.

For an ordinary scheduled V3 run, load only the context needed to protect current capital, avoid duplicate research, link active theses, and identify evidence due. Do not turn every scan into a full portfolio review.

## Exposure labels

- `DIRECT`
- `DERIVATIVE`
- `READ_THROUGH`
- `NONE_IDENTIFIED`

## Scheduled V3 persistence default

For scheduled News Radar V3 runs, research-only persistence is required when a supported write path exists. Mike's instruction to activate V3 authorizes persistence of Radar process state; it does not authorize thesis, underwriting, valuation, or portfolio decisions.

Persist automatically:

- one run coverage manifest;
- canonical Event Ledger additions and updates;
- first-seen, original-publication, and detection timestamps;
- detection status and latency;
- duplicate and rejected records needed for calibration;
- atomic slow-burn observations;
- P2 evidence requests, due dates, and overdue status;
- frozen catalyst packets;
- feed outages, unavailable state sources, late detections, and persistence failures;
- the exact Research With Confidence handoff for each P0 or P1 item.

### Preferred persistence order

1. supported canonical Event Ledger or research endpoint;
2. supported TaskTracker research record that preserves the V3 fields without changing a thesis or underwriting decision;
3. a dated Library artifact such as `news-radar-v3-YYYY-MM-DD-HHMM-ET.md` plus a machine-readable companion when practical;
4. report-only fallback with `PERSISTENCE_FAILED` clearly declared.

Do not silently claim continuity when no write succeeded.

## Safe write procedure

When persisting V3 research state:

1. reread the latest production or Library state immediately before writing;
2. search for the same `event_id`, underlying fact, and independence group;
3. update the canonical record rather than creating a duplicate;
4. preserve the original source and first-seen fields before adding follow-up evidence;
5. append only atomic evidence justified by the source;
6. preserve the original route, confidence, price context, and coverage limitations;
7. write the run manifest and persistence status;
8. reread after the write and verify identifiers, timestamps, route, and status;
9. never store credentials, access tokens, raw portfolio secrets, or unlicensed full-text material.

## Decision-state boundary

Automatic Radar persistence must never:

- change a Mind Model thesis, wording, probability, status, or forecast;
- approve a pending Mind Model proposal;
- change an underwriting posture, fair value, valuation scale, entry range, add/trim/exit threshold, kill criterion, or mandatory review date;
- create, modify, or close a portfolio position or strategy;
- place or simulate an executed order;
- choose account location, position size, funding source, or hedge.

Research With Confidence may recommend an underwriting advance. Full Underwriting and downstream workflows own decision-state changes and their required monitor propagation.

## Late detection and overdue evidence

A scheduled write must preserve late-discovery and absence information rather than hiding it inside narrative text.

For a late-detected event, persist:

```text
detection_status: LATE_DETECTION
original_publication_at
first_seen_at
detection_latency
missed_feed_reason
whether_decision_usefulness_was_reduced
```

For expected evidence, persist the due date and status. Do not silently move a missed date forward. Append the next resolving evidence separately.

## Run coverage manifest

Persist the V3 manifest from `v3-run-contract.md`, including:

- holdings and active underwritings checked;
- theses and watchlist checked;
- catalysts and evidence-due items checked;
- successful feeds and unavailable feeds;
- state sources unavailable;
- material blind spots;
- run status and persistence status;
- next scheduled slot.

The user-facing output may stay compact, but the stored record must make omissions auditable.

## Trade and holding boundary

A Radar write records research. It never places an order, changes a holding, or activates a strategy position. Even when Mike has previously stated that a broker transaction occurred, the Radar may link the known exposure but may not invent fill details or change the portfolio record without the supported transaction workflow.
