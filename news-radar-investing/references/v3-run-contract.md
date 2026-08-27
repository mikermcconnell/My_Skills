# News Radar Investing V3 Run Contract

This contract is authoritative for scheduled News Radar V3 runs. Radar is the high-recall detection, memory, prioritization, and routing layer. Research With Confidence owns independent verification, causality, counterfactuals, confounders, economic materiality, value capture, and the preliminary expectations-gap decision. Full Underwriting owns current-price analysis, fully diluted capital structure, scenarios, valuation, expected return, opportunity cost, timing, kill criteria, and the final security posture.

## Authoritative cadence

Use one schedule everywhere:

- **08:00 America/Toronto** — overnight international developments, pre-market filings, regulatory actions, portfolio risks, and known catalyst outcomes.
- **11:30 America/Toronto** — intraday primary-source confirmation, new North American developments, open-event updates, and evidence-due checks.
- **15:00 America/Toronto** — pre-close changes, time-sensitive holdings risk, final research-queue selection, and unresolved-event status.

An explicitly invoked after-close capture may record earnings, filings, trial results, and regulatory announcements, but it does not replace the next scheduled run.

Scan from the last successful run timestamp. When a run is advanced, delayed, skipped, or fails, preserve the reason and the resulting scan window. Never silently create a gap.

## Mandatory preflight

Before broad discovery, load the narrow current context required to protect capital and prevent duplicate work:

```text
last_successful_run_at
open_event_ledger_records
open_P0_P1_P2_items
next_evidence_due_queue
known_catalyst_calendar
active_holdings
active_underwritings_and_monitors
current_kill_criteria_and_review_dates
active_Mind_Model_theses_and_watchlist
available_source_feeds_and_outages
```

Use live state when supported. If a required context source cannot be read, mark it `STATE_UNAVAILABLE`, state the affected coverage, and do not imply that the holding or thesis was checked.

## Run coverage manifest

Persist one manifest per scheduled run:

```text
run_id
radar_version: 3
run_timestamp
scan_window_start
scan_window_end
scheduled_slot
run_status: SUCCESS | PARTIAL | FAILED | ADVANCED | DELAYED
last_successful_run_at
markets_and_event_categories_covered
holdings_checked
active_underwritings_checked
theses_and_watchlist_checked
known_catalysts_checked
primary_feeds_searched_successfully
expert_social_and_alternative_lanes_checked
feeds_unavailable_delayed_or_not_connected
state_sources_unavailable
material_blind_spots
persistence_status
next_scheduled_slot
```

The user-facing report may summarize this compactly, but the persisted manifest must make omissions auditable.

## Detection status and late-event recovery

Every material observation receives one detection status:

- `ON_TIME`
- `LATE_DETECTION`
- `FOLLOW_UP`
- `DUPLICATE`
- `EXPECTED_EVIDENCE_MISSED`
- `DISCLOSURE_REMOVED`
- `MILESTONE_DELAYED`
- `PROMISE_UNCONFIRMED`
- `PRICE_DISLOCATION_UNEXPLAINED`

Apply this rule without exception:

```text
publication or event time predates the current scan window
+ no matching canonical Event Ledger record exists
= LATE_DETECTION
```

Backfill and route a late-detected event normally. Preserve the original publication time, first Radar detection time, latency, likely missed-feed reason, and whether the delay reduced decision usefulness. Do not discard a material event merely because it should have been found earlier.

Dependent coverage discovered later is `FOLLOW_UP` or `DUPLICATE`, not a late new event.

## Evidence-due and absence detection

At every run, check items whose `next_evidence_date` or catalyst window has arrived. Absence can be decision-relevant even without a new headline.

Create or append an observation when, for example:

- a promised trial readout, filing, financing, customer confirmation, permit, launch, project milestone, or regulator decision does not arrive;
- a trial completion date, endpoint, enrollment target, or decision window moves;
- a previously material KPI, segment table, risk disclosure, or management discussion disappears;
- repeated guidance remains unsupported past the date when observable evidence was expected.

Radar records the absence and routes the interpretation. It does not automatically call the absence negative, change a thesis probability, or alter valuation.

## Price-dislocation rule

A large or unusual price move may trigger a targeted source search, but price movement is not itself a Novelty pass.

Use `PRICE_DISLOCATION_UNEXPLAINED` until an underlying event, factor exposure, positioning effect, forced flow, or attribution error is identified. Route only the factual question that remains.

## Research-only persistence

For scheduled V3 runs, persistence of research-only state is the default requirement, not an optional extra.

Persist when supported:

- the run coverage manifest;
- canonical Event Ledger additions and updates;
- first-seen and detection timestamps;
- duplicate and rejected-event records needed for calibration;
- atomic slow-burn observations;
- open P2 evidence requests and due dates;
- frozen catalyst packets;
- late detections, feed outages, and persistence failures.

Use the supported Event Ledger or research store when available. If no canonical store is available, save a dated Library artifact and clearly label the fallback. If neither write path works, mark `PERSISTENCE_FAILED` in the report rather than implying continuity.

Automatic Radar persistence must never:

- change a Mind Model thesis, wording, probability, status, or approved forecast;
- change fair value, entry ranges, security posture, kill criteria, or a re-underwrite date;
- create, alter, or approve a portfolio position or strategy;
- place a trade.

Those decisions remain downstream and follow their own authorization and monitor-propagation rules.

## Portfolio-defense priority

Use this order:

1. existing holding or active-underwriting permanent-loss risk;
2. evidence due today or overdue;
3. known catalyst result or material filing;
4. material update to an open Event Ledger item;
5. slow-burn evidence crossing a threshold;
6. new opportunity discovery.

A P0 risk takes the fast path. Do not delay it to complete a broad value-chain map, false-friend analysis, or thematic beneficiary list.

## Minimum security mapping

For every serious event, identify only what Radar needs to route correctly:

```text
direct_holding_or_security
linked_thesis_or_underwriting
exposure_type: DIRECT | DERIVATIVE | READ_THROUGH | NONE_IDENTIFIED
preliminary_mechanism
main_capture_uncertainty
portfolio_cluster_when_relevant
```

Require a second-order beneficiary and a non-beneficiary or comparator only for:

- P1 opportunity discovery;
- industry, policy, bottleneck, or class-level events;
- cases where the obvious issuer may already be fully recognized;
- events whose main value lies in cross-company transmission.

Do not require this work before routing a time-sensitive P0 risk or a simple P2 document check.

## Hard depth boundary

A normal Radar item should stop after establishing:

1. exact change versus the prior baseline;
2. original source, claim status, and independence group;
3. timestamps, market status, and available reaction context;
4. plausible materiality and preliminary mechanism;
5. affected holding, thesis, or candidate set;
6. five-gate results;
7. strongest reason the lead may fail;
8. primary route;
9. three or fewer decisive Research With Confidence questions;
10. next evidence and date.

Radar should not normally perform:

- a full counterfactual or causal investigation;
- detailed company economics or sensitivity modeling;
- complete variant-perception analysis;
- reverse valuation or a percentage-priced-in estimate;
- fully diluted capital-structure analysis;
- Bear/Base/Bull scenarios or expected returns;
- detailed clinical-commercial underwriting;
- portfolio loss-budget, hedge, funding-source, or position-size calculations;
- a final buy, sell, add, trim, exit, or investability decision.

Depth exceptions are limited to:

- an urgent P0 permanent-loss question;
- comparison of an actual result with an already frozen catalyst packet;
- retrieval of one time-sensitive document needed to classify the event correctly;
- an explicitly requested combined workflow.

## Compact scheduled output

Lead with:

| Priority | Event ID | What changed | Affected holding / thesis | Gate issue | Route | Exact next question | Evidence / date |
|---|---|---|---|---|---|---|---|

Provide a concise detail block only for P0 and P1 items:

```text
Original source
Prior baseline
Delta class and thesis effect
Detection status
Preliminary mechanism
Why materiality is plausible
Direct exposure and capture uncertainty
Strongest failure reason
RWC questions
Next evidence and date
```

For P2 and P3, state the missing evidence and due date without expanding into a mini-report.

A valid no-lead run should report:

- no qualifying P0/P1/P2 item in the searched universe;
- material duplicates or open-event updates;
- overdue evidence checks;
- coverage exceptions and outages;
- persistence status.
