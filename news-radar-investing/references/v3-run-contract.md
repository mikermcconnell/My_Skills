# News Radar Investing V3 Run Contract

This contract is authoritative for scheduled News Radar V3 runs. Radar is the high-recall detection, memory, prioritization, active-thesis-testing, market-context, and routing layer. Research With Confidence owns independent verification, causality, counterfactuals, confounders, economic materiality, value capture, and the preliminary expectations-gap decision. Full Underwriting owns current-price analysis, fully diluted capital structure, scenarios, valuation, expected return, opportunity cost, timing, kill criteria, and the final security posture. Event-Trade Underwriting owns short-duration event payoff and execution analysis.

## Authoritative cadence

Use one schedule everywhere:

- **08:00 America/Toronto** — overnight international developments, pre-market filings, regulatory actions, portfolio risks, thesis evidence due, known catalyst outcomes, and pre-market/overnight market context.
- **11:30 America/Toronto** — intraday primary-source confirmation, new North American developments, thesis/forecast updates, open-event updates, evidence-due checks, and live market-tape context.
- **15:00 America/Toronto** — pre-close changes, time-sensitive holdings risk, final research-queue selection, thesis-review changes, unresolved-event status, and live market-tape context.

An explicitly invoked after-close capture may record earnings, filings, trial results, and regulatory announcements, but it does not replace the next scheduled run.

Scan from the last successful run timestamp. When a run is advanced, delayed, skipped, or fails, preserve the reason and the resulting scan window. Never silently create a gap.

## Mandatory preflight

Before broad discovery, load the narrow current context required to protect capital, test active theses, distinguish broad-market from idiosyncratic moves, and prevent duplicate work:

```text
last_successful_run_at
open_event_ledger_records
open_P0_P1_P2_items
next_evidence_due_queue
known_catalyst_calendar
active_holdings
active_underwritings_and_monitors
current_kill_criteria_and_review_dates
live_Mind_Model_overview
active_nonretired_theses
Mind_Model_review_queue
thesis_diagnostics
open_thesis_forecasts
thesis_evidence_ledger
thesis_watchlist_exposures
linked_investor_research_state
pending_thesis_proposals
same_day_market_context
available_source_feeds_and_outages
```

Use live state when supported. If a required context source cannot be read, mark it `STATE_UNAVAILABLE`, state the affected coverage, and do not imply that the holding, underwriting, thesis, or market driver was checked.

GitHub source, local seeds, migrations, and remembered thesis prose may explain schema but are not confirmed production Mind Model state.

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
active_theses_loaded
theses_researched
Mind_Model_review_queue_checked
thesis_forecasts_due_checked
thesis_state_unavailable
known_catalysts_checked
market_tape_checked
market_tape_as_of
market_tape_sources
primary_feeds_searched_successfully
expert_social_and_alternative_lanes_checked
feeds_unavailable_delayed_or_not_connected
state_sources_unavailable
material_blind_spots
underwriting_requirements_assigned
persistence_status
next_scheduled_slot
```

The user-facing report may summarize this compactly, but the persisted manifest must make omissions auditable.

## Active Thesis Research lane

Run this lane on every scheduled V3 pass after urgent portfolio-defense work and before open-universe discovery.

For each readable non-retired thesis, construct the search manifest from the stored Mind Model state. Test only what the thesis says must become true, remain true, or fail:

```text
thesis baseline
assumptions
investment hypothesis
strongest opposing case
thesis falsifiers
next highest-value test
pillar claims and mechanisms
pillar metric / baseline / target / target date
pillar source of truth
pillar falsifier
pillar next highest-value test
open forecast statements
forecast resolution dates
forecast source of truth
forecast confirm indicators
forecast warning indicators
forecast break indicators
watchlist mechanisms
watchlist evidence needed
watchlist falsifiers
position status
linked security readiness
linked underwriting status
```

Do a cheap explicit sweep across every active thesis. Do not turn every thesis into a mini deep-dive three times per day.

Allocate deeper Radar search budget in this order when live TaskTracker state supports it:

1. owned exposure with `requiresReunderwrite`;
2. `EVENT_TRIGGERED` thesis;
3. owned exposure + `OVERDUE` review;
4. other `OVERDUE` review;
5. `DUE` review;
6. `BLOCKED` or materially `CONFLICTED` thesis;
7. normal active thesis with a timely forecast, falsifier, source-of-truth metric, or next-highest-value test.

A material thesis-research observation must identify:

```text
thesis_id
pillar_id when applicable
forecast_id when applicable
what_was_tested
new_evidence
stance: SUPPORT | CHALLENGE | CONTEXT when supported
what_it_proves
what_it_does_not_prove
delta_class
thesis_effect
detection_status
five_gates
primary_route
underwriting_requirement
next_test_or_evidence
```

A thesis with no material delta is recorded as checked in the manifest, not expanded in the visible report.

Radar may write research-only evidence, linked research questions, or a pending thesis proposal when supported. It must never approve the proposal or directly change the approved thesis.

## Compact market tape — What's moving markets today

Produce this on every scheduled visible run after urgent portfolio-defense classification. It is contextual market attribution, not a separate quota of Radar events.

Use the freshest same-day evidence available at the run cutoff:

- **08:00:** North American futures and overnight international markets; do not describe regular-session index moves that have not happened yet.
- **11:30 / 15:00:** actual same-day U.S./Canadian indexes, sectors, and factor leadership/weakness.
- Check S&P 500, Nasdaq/large-cap growth, and TSX when relevant. Add Treasury yields/rates, oil, FX, volatility, credit, metals, or other commodities only when materially influencing the tape or the user's portfolio.
- Identify sector/factor leadership when it helps separate market-driven portfolio moves from company-specific evidence.

Visible market-tape contract:

```text
heading: What's moving markets today
maximum_bullets: 3
visible_word_budget: about 80-100 words total
as_of_time: required when using live prices
```

Each bullet should combine an **observed move** with the best-supported **reported/likely driver**. Do not state causal attribution as fact when it is inferential. If the evidence does not support a clean explanation, say `attribution uncertain`.

Do not:

- repeat company-specific events already clear from the lead Radar table unless they are genuinely driving the broader market;
- convert ordinary index/sector movement into P0/P1/P2 simply to populate the tape;
- treat a market narrative as proof of a thesis or security event;
- exceed the compact-output budget materially to provide a macro essay.

A broad market factor becomes a normal Radar event only when it independently passes the five gates and is sufficiently linked to a holding, active underwriting, or thesis.

If reliable market data or attribution cannot be retrieved, state `Market tape unavailable or attribution uncertain` in one short line and preserve the feed gap in the manifest.

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

At every run, check items whose `next_evidence_date`, thesis forecast resolution date, pillar target date, source-of-truth observation date, or catalyst window has arrived. Absence can be decision-relevant even without a new headline.

Create or append an observation when, for example:

- a promised trial readout, filing, financing, customer confirmation, permit, launch, project milestone, regulator decision, or thesis forecast does not arrive;
- a trial completion date, endpoint, enrollment target, thesis target date, or decision window moves;
- a previously material KPI, segment table, risk disclosure, management discussion, or thesis source-of-truth metric disappears;
- repeated guidance or a thesis assumption remains unsupported past the date when observable evidence was expected.

Radar records the absence and routes the interpretation. It does not automatically call the absence negative, change a thesis probability, or alter valuation.

## Price-dislocation rule

A large or unusual price move may trigger a targeted source search, but price movement is not itself a Novelty pass.

Use `PRICE_DISLOCATION_UNEXPLAINED` until an underlying event, factor exposure, positioning effect, forced flow, or attribution error is identified. Route only the factual question that remains.

The market tape can provide factor context for this investigation, but it must not be used to manufacture a company-specific explanation.

## Research-only persistence

For scheduled V3 runs, persistence of research-only state is the default requirement, not an optional extra.

Persist when supported:

- the run coverage manifest;
- canonical Event Ledger additions and updates;
- first-seen and detection timestamps;
- duplicate and rejected-event records needed for calibration;
- atomic slow-burn observations;
- active-thesis research observations and checked-thesis coverage;
- decision-relevant Mind Model evidence records;
- linked Investor Research questions for explicit evidence gaps;
- pending thesis proposals when evidence may justify a reviewed change;
- underwriting-requirement classification and rationale;
- open P2 evidence requests and due dates;
- frozen catalyst and forecast packets;
- market-tape as-of time and high-level drivers when supported;
- late detections, feed outages, and persistence failures.

Use the supported Event Ledger or research store when available. If no canonical store is available, save a dated Library artifact and clearly label the fallback. If neither write path works, mark `PERSISTENCE_FAILED` in the report rather than implying continuity.

Automatic Radar persistence must never:

- approve or directly change a Mind Model thesis, wording, probability, status, health, or approved forecast;
- approve a pending Mind Model proposal;
- change fair value, entry ranges, security posture, kill criteria, or a re-underwrite date;
- create, alter, or approve a portfolio position or strategy;
- place a trade.

Those decisions remain downstream and follow their own authorization and monitor-propagation rules.

## Portfolio-defense priority

Use this order:

1. existing holding or active-underwriting permanent-loss risk;
2. owned thesis exposure marked `requiresReunderwrite`;
3. evidence due today or overdue, including thesis forecasts;
4. known catalyst result or material filing;
5. material update to an open Event Ledger item;
6. event-triggered / overdue active-thesis research;
7. slow-burn evidence crossing a threshold;
8. new opportunity discovery.

A P0 risk takes the fast path. Do not delay it to complete thesis research, a market-tape summary, a broad value-chain map, false-friend analysis, or thematic beneficiary list.

## Minimum security and thesis mapping

For every serious event, identify only what Radar needs to route correctly:

```text
direct_holding_or_security
linked_thesis_or_underwriting
linked_pillar_or_forecast_when_relevant
exposure_type: DIRECT | DERIVATIVE | READ_THROUGH | NONE_IDENTIFIED
preliminary_mechanism
main_capture_uncertainty
portfolio_cluster_when_relevant
linked_security_readiness_when_available
linked_underwriting_status_when_available
```

Require a second-order beneficiary and a non-beneficiary or comparator only for:

- P1 opportunity discovery;
- industry, policy, bottleneck, or class-level events;
- cases where the obvious issuer may already be fully recognized;
- events whose main value lies in cross-company transmission.

Do not require this work before routing a time-sensitive P0 risk or a simple P2 document check.

## Underwriting-requirement classification

Every surfaced event and every material thesis-research delta must receive exactly one `Underwriting Required?` value:

- **`NO`** — evidence belongs in thesis/evidence monitoring; no security underwriting is currently needed.
- **`CONDITIONAL — AFTER RWC`** — underwriting could become appropriate, but causality, materiality, value capture, or expectations still need RWC. This is the normal state for a new P1 opportunity before verification.
- **`YES — RE-UNDERWRITE EXISTING`** — an existing security underwriting may have materially changed and the main remaining work is valuation/security posture. Use when live TaskTracker says `requiresReunderwrite` or verified evidence crosses an existing re-underwrite trigger.
- **`YES — NEW FULL UNDERWRITING`** — a new security has enough verified causal/capture evidence that valuation and security work are the main remaining step. If meaningful RWC uncertainty remains, do not use this value.
- **`YES — EVENT-TRADE UNDERWRITING`** — a discrete short-duration event has adequate factual support and the main remaining question is payoff/execution.

This is routing metadata, not a valuation, trade, or investability conclusion.

Use TaskTracker as an input when available:

```text
reviewQueue.requiresReunderwrite
watchlist.positionStatus
watchlist.securityReadiness
linked Investor Research underwritingStatus
thesis reviewState
current kill / re-underwrite triggers
```

Mind Model transmission alone is not sufficient to declare a security decision-ready.

For every `YES` or `CONDITIONAL` classification, state one sentence explaining why.

## Hard depth boundary

A normal Radar item should stop after establishing:

1. exact change versus the prior baseline;
2. original source, claim status, and independence group;
3. timestamps, market status, and available reaction context;
4. plausible materiality and preliminary mechanism;
5. affected holding, thesis, pillar, forecast, or candidate set;
6. five-gate results;
7. strongest reason the lead may fail;
8. primary route;
9. underwriting-requirement classification and brief reason;
10. three or fewer decisive Research With Confidence questions in the stored record;
11. next evidence and date.

Radar should not normally perform:

- a full counterfactual or causal investigation;
- detailed company economics or sensitivity modeling;
- complete variant-perception analysis;
- reverse valuation or a percentage-priced-in estimate;
- fully diluted capital-structure analysis;
- Bear/Base/Bull scenarios or expected returns;
- detailed clinical-commercial underwriting;
- portfolio loss-budget, hedge, funding-source, or position-size calculations;
- a final buy, sell, add, trim, exit, or investability decision;
- approval of a thesis proposal or forecast change;
- an extended macro or market commentary section.

Depth exceptions are limited to:

- an urgent P0 permanent-loss question;
- comparison of an actual result with an already frozen catalyst or thesis-forecast packet;
- retrieval of one time-sensitive document needed to classify the event correctly;
- an explicitly requested combined workflow.

## Visible-output compression budget

The visible chat report should target roughly **75% of the prior V3 report length for an equivalent information set**. This is a presentation constraint only: do not reduce search coverage, stored evidence, routing metadata, or the completeness of the attached Markdown artifact.

Apply these compression rules:

- **Table first; avoid repetition.** Do not repeat a fact already clear from the lead table unless prose adds causality, uncertainty, provenance, or routing information.
- **P0/P1 detail cap:** normally 120–160 visible words per item. Exceed only for an urgent P0 when compression would make the classification misleading.
- **Gates shorthand:** use compact notation such as `Gates: N/M/C/R pass; E unknown`. Spell out only a failed or disputed gate that matters to routing.
- **RWC questions:** show one primary visible question by default; maximum two when genuinely independent. The stored record/artifact may retain up to three.
- **P2/P3:** normally table-only. Add visible prose only for overdue/missing evidence, unusual classification, or material portfolio-risk context.
- **Market tape:** mandatory, but maximum 3 bullets and roughly 80–100 words total. It must fit inside the compact-output budget rather than being additive macro commentary.
- **Baseline:** restate only the one or two baseline facts required to understand the delta.
- **Mechanism:** state once. Do not repeat the same causal chain in multiple forms.
- **Reconciliation:** mention only items whose status changed. Otherwise one sentence is enough: `Open items reconciled; no additional decision-relevant delta.`
- **Thesis lane:** show the Thesis Research table only when a material thesis delta exists. Do not list unchanged theses individually.
- **Coverage manifest:** compress to one short closing paragraph in chat. Mention only material unavailable state, outages, blind spots, late detections, scan-gap recovery, and persistence status. Preserve the full manifest in the artifact.
- **Sources:** omit a separate visible source register unless provenance itself is decision-relevant; inline citations are sufficient.
- **Artifact:** the complete dated Markdown record remains the detailed audit trail and should not be shortened merely to meet the visible-output budget.

Preferred visible order:

1. title and one-sentence run status;
2. lead table;
3. `What's moving markets today` — maximum 3 bullets / roughly 80–100 words;
4. compact P0/P1 detail blocks;
5. Thesis Research table only if needed;
6. one short `Other checks` paragraph only if needed;
7. one short coverage/persistence paragraph;
8. artifact link.

## Compact scheduled output

Lead with:

| Priority | Event ID | What changed | Affected holding / thesis | Gate issue | Route | Underwriting Required? | Exact next question | Evidence / date |
|---|---|---|---|---|---|---|---|---|

Immediately after the lead table add:

### What's moving markets today

Use no more than three bullets and roughly 80–100 words total. Use the correct market state for the scheduled slot and include an as-of time when using live prices. The section should answer whether broad rates, commodities, macro/geopolitics, sector leadership, or risk appetite are driving the tape, while clearly separating observed movement from causal attribution.

For P0 and P1, visible detail should normally contain only:

```text
Delta vs baseline
Source/provenance only if not obvious from the table
One-sentence mechanism/materiality
Gates shorthand
Strongest failure reason
Underwriting Required? + brief reason
One primary RWC question, maximum two
Next evidence/date if not already clear
```

For P2 and P3, the table row is normally sufficient. Include missing evidence/date and underwriting requirement in the row rather than expanding into a mini-report.

When thesis research produces a material delta, add:

| Thesis | What Radar tested | New evidence | Pillar / forecast affected | Direction | Route | Underwriting Required? | Next test / date |
|---|---|---|---|---|---|---|---|

Do not list unchanged theses individually. Record them as checked in the persisted manifest.

A valid no-lead run should report compactly:

- no qualifying P0/P1/P2 item or material thesis delta in the searched universe;
- a short market tape or its stated unavailability;
- only material duplicate/open-event changes;
- overdue event/thesis evidence if any;
- thesis-research coverage and material unavailable Mind Model state;
- material coverage exceptions/outages;
- persistence status.
