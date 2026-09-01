# Mike's Integration and Persistence Rules — News Radar V3

Read this when a Radar run needs live TaskTracker, Mind Model, portfolio, underwriting-monitor, Library, or persistence context.

## Read current context

Use live data rather than remembered holdings, stale screenshots, local seeds, GitHub source code, or hardcoded thesis wording. Never print credentials.

### TaskTracker and Mind Model

Local repository when available:

`C:\Users\Mike McConnell\Documents\mike_apps\TaskTracker`

1. Read `AGENTS.md` and apply the current `mind-model` skill.
2. Load the API key from `.env.local` without displaying it.
3. Prefer the authenticated production overview endpoint for current Mind Model state:
   - `GET /api/mind-model/overview`
4. The overview is the canonical read bundle for Radar thesis research and can include:
   - `theses`
   - `forecasts`
   - `sources`
   - `evidence`
   - `proposals`
   - `watchlist`
   - `research`
   - `decisions`
   - `reviewQueue`
   - `diagnosticsByThesisId`
   - `investorResearchByCompanyId`
5. Match events and thesis evidence to exact-company research, active underwritings, monitors, kill criteria, review dates, sector or thematic projects, thesis mechanisms, causal pillars, forecasts, falsifiers, watchlists, diagnostics, review-queue state, and pending proposals.
6. Treat `UNAUTHORIZED` as unavailable production state. A permitted read-only fallback may be used only when authorized and clearly labelled.
7. GitHub source, local seed data, migration content, and UI fixtures explain schema and intended behavior; they are **not confirmed live production thesis state**.

### TaskTracker thesis fields Radar should use

When current production state is readable, the Active Thesis Research lane should derive its search plan from stored fields rather than generic ticker news.

For each non-retired thesis, use as applicable:

```text
baseline
summary
assumptions
investmentHypothesis
strongestOpposingCase
falsifiers
nextReviewAt
reviewState
thesisHealth
evidenceGrade
reviewReason
lastMaterialChange
nextHighestValueTest
pillars[].claim
pillars[].mechanism
pillars[].metric
pillars[].baseline
pillars[].target
pillars[].targetDate
pillars[].sourceOfTruth
pillars[].falsifier
pillars[].nextHighestValueTest
forecasts[].statement
forecasts[].resolutionDate
forecasts[].metric
forecasts[].baseline
forecasts[].target
forecasts[].sourceOfTruth
forecasts[].confirmIndicators
forecasts[].warningIndicators
forecasts[].breakIndicators
watchlist[].mechanism
watchlist[].evidenceNeeded
watchlist[].falsifier
watchlist[].positionStatus
watchlist[].securityReadiness
reviewQueue[].requiresReunderwrite
diagnosticsByThesisId
```

Do not infer a thesis change because a field exists. Radar researches the observable world against the stored test.

### TaskTracker thesis-research write paths

When supported and authorized, Radar may persist research-only thesis state through existing TaskTracker APIs:

- **Evidence:** `POST /api/mind-model/evidence`
  - Use for a genuinely new claim tied to a thesis, and to a pillar/forecast when supported.
  - Preserve `SUPPORT`, `CHALLENGE`, or `CONTEXT`, materiality, claim type, what the evidence proves, what it does not prove, and the decision implication when those fields are supported by the schema.
- **Investor Research question:** `POST /api/mind-model/research`
  - Use when Radar has identified a precise unresolved question or next action linked to a thesis.
- **Pending thesis proposal:** `POST /api/mind-model/proposals`
  - Use only when evidence may justify a reviewed change to thesis wording, assumptions, pillars, probability, health, falsifiers, review state/date, or other approved thesis fields.
  - A proposal is not an approved thesis change.
- **Thesis decisions:** approval/rejection remains human-only through the proposal decision workflow. Radar must not attempt to approve its own proposal.

If a TaskTracker write path is unavailable, preserve the same research fields in the Event Ledger/research store or dated Library fallback rather than silently dropping them.

### TaskTracker review priority

Use the live Mind Model review queue to allocate thesis-research depth when available. The intended priority is:

1. owned exposure with `requiresReunderwrite`;
2. `EVENT_TRIGGERED` thesis;
3. owned exposure + `OVERDUE` review;
4. other `OVERDUE` review;
5. `DUE` review;
6. `BLOCKED` or materially conflicted thesis;
7. normal active thesis with timely observable evidence.

This priority controls **Radar search attention**, not thesis approval or portfolio action.

### Investing portfolios

Local repository when available:

`C:\Users\Mike McConnell\Documents\mike_apps\Investing`

1. Read `AGENTS.md`, then `CLAUDE.md`.
2. Initialize Firebase only through the supported repository configuration without exposing secrets.
3. Use user-scoped portfolio and position helpers.
4. Preserve portfolio, account, lot, strategy, instrument, share class, and currency separation.
5. Normalize CDRs, Canadian wrappers, options, duplicate underlyings, and direct versus read-through exposure.
6. Use timestamped price and FX data for value, weight, P/L, or concentration claims.

For an ordinary scheduled V3 run, load only the context needed to protect current capital, actively test current theses, avoid duplicate research, link security exposures, and identify evidence due. Do not turn every scan into a full portfolio or full thesis review.

## Exposure labels

- `DIRECT`
- `DERIVATIVE`
- `READ_THROUGH`
- `NONE_IDENTIFIED`

## Underwriting-requirement integration

Radar must assign one `Underwriting Required?` classification to every surfaced item and material thesis delta:

- `NO`
- `CONDITIONAL — AFTER RWC`
- `YES — RE-UNDERWRITE EXISTING`
- `YES — NEW FULL UNDERWRITING`
- `YES — EVENT-TRADE UNDERWRITING`

When TaskTracker state is readable, use these fields as evidence for the routing classification:

```text
reviewQueue.requiresReunderwrite
watchlist.positionStatus
watchlist.securityReadiness
investorResearchByCompanyId[].underwritingStatus
investorResearchByCompanyId[].thesisStatus
investorResearchByCompanyId[].evidenceConfidence
thesis.reviewState
thesis.thesisHealth
current underwriting kill criteria and re-underwrite triggers
```

Rules:

- `requiresReunderwrite = true` is strong support for `YES — RE-UNDERWRITE EXISTING`.
- An owned security with verified evidence crossing a current re-underwrite trigger can also qualify for `YES — RE-UNDERWRITE EXISTING`.
- A new P1 opportunity with unresolved causality, value capture, or expectations should normally be `CONDITIONAL — AFTER RWC`, not `YES — NEW FULL UNDERWRITING`.
- Use `YES — NEW FULL UNDERWRITING` only when the principal remaining work is security valuation/return analysis rather than causal verification.
- Use `YES — EVENT-TRADE UNDERWRITING` only when a discrete event is factually established and the principal remaining questions are payoff states and execution.
- Mind Model exposure alone does not make a security decision-ready.

Persist the classification and a one-sentence rationale in the Event Ledger/research record or fallback artifact. Do not force this routing metadata into a TaskTracker schema field that does not support it.

## Scheduled V3 persistence default

For scheduled News Radar V3 runs, research-only persistence is required when a supported write path exists. Mike's instruction to activate V3 authorizes persistence of Radar process state; it does not authorize thesis, underwriting, valuation, or portfolio decisions.

Persist automatically:

- one run coverage manifest;
- canonical Event Ledger additions and updates;
- first-seen, original-publication, and detection timestamps;
- detection status and latency;
- duplicate and rejected records needed for calibration;
- atomic slow-burn observations;
- active-thesis research coverage and material thesis deltas;
- TaskTracker thesis evidence records when supported;
- linked Investor Research questions for explicit gaps when supported;
- pending thesis proposals when justified, never auto-approved;
- `Underwriting Required?` classification and rationale;
- P2 evidence requests, due dates, and overdue status;
- frozen catalyst and thesis-forecast packets;
- feed outages, unavailable state sources, late detections, and persistence failures;
- the exact Research With Confidence handoff for each P0 or P1 item.

### Preferred persistence order

1. supported canonical Event Ledger or research endpoint;
2. supported TaskTracker Mind Model evidence/research/proposal path for thesis-specific research, plus the Radar record that preserves V3 routing fields;
3. supported TaskTracker research record that preserves the V3 fields without changing a thesis or underwriting decision;
4. a dated Library artifact such as `news-radar-v3-YYYY-MM-DD-HHMM-ET.md` plus a machine-readable companion when practical;
5. report-only fallback with `PERSISTENCE_FAILED` clearly declared.

Do not silently claim continuity when no write succeeded.

## Safe write procedure

When persisting V3 research state:

1. reread the latest production or Library state immediately before writing;
2. search for the same `event_id`, underlying fact, independence group, thesis evidence, and existing pending proposal;
3. update the canonical event record rather than creating a duplicate;
4. preserve the original source and first-seen fields before adding follow-up evidence;
5. append only atomic evidence justified by the source;
6. link evidence to the correct thesis/pillar/forecast when supported;
7. preserve what the evidence proves and does not prove;
8. preserve the original route, underwriting-requirement classification, price context, and coverage limitations;
9. create a research question or proposal only when there is a precise unresolved test or a concrete proposed change;
10. never approve a proposal in the Radar workflow;
11. write the run manifest and persistence status;
12. reread after the write and verify identifiers, timestamps, route, status, and thesis links;
13. never store credentials, access tokens, raw portfolio secrets, or unlicensed full-text material.

## Decision-state boundary

Automatic Radar persistence must never:

- directly change a Mind Model thesis, wording, probability, status, thesis health, approved pillar, or approved forecast;
- approve a pending Mind Model proposal;
- change an underwriting posture, fair value, valuation scale, entry range, add/trim/exit threshold, kill criterion, or mandatory review date;
- create, modify, or close a portfolio position or strategy;
- place or simulate an executed order;
- choose account location, position size, funding source, or hedge.

Research With Confidence may recommend an underwriting advance. Full Underwriting and downstream workflows own decision-state changes and their required monitor propagation.

## Late detection and overdue thesis evidence

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

For expected event or thesis evidence, persist the due date and status. Do not silently move a missed date forward. This includes thesis forecast resolution dates, pillar target dates, source-of-truth checkpoints, and promised evidence linked to the next-highest-value test. Append the next resolving evidence separately.

## Run coverage manifest

Persist the V3 manifest from `v3-run-contract.md`, including:

- holdings and active underwritings checked;
- active theses loaded and theses researched;
- Mind Model review queue and thesis forecasts due checked;
- catalysts and evidence-due items checked;
- successful feeds and unavailable feeds;
- state sources unavailable;
- material blind spots;
- underwriting requirements assigned;
- run status and persistence status;
- next scheduled slot.

The user-facing output may stay compact, but the stored record must make omissions auditable.

## Trade and holding boundary

A Radar write records research. It never places an order, changes a holding, or activates a strategy position. Even when Mike has previously stated that a broker transaction occurred, the Radar may link the known exposure but may not invent fill details or change the portfolio record without the supported transaction workflow.
