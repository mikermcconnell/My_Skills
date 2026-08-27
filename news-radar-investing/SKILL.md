---
name: news-radar-investing
version: 3
description: Operate the high-recall, portfolio-aware front end of the public-equity research process. Detect and persist genuinely new events, slow-burn fundamental deltas, overdue evidence, known catalysts, clinical developments, filing changes, expert observations, and possible price-attribution errors; distinguish them from recycled coverage; prioritize risks to existing holdings and active underwritings; and route precise questions to Research With Confidence. Use for scheduled News Radar V3 runs, holdings-risk scans, medical or cancer-trial radar, catalyst preparation, filing-delta review, expert or social-signal monitoring, and first-pass alert triage. Do not use for full causal research, complete value-capture analysis, valuation, final buy or sell decisions, event-trade approval, or account-specific position sizing.
---

# News Radar Investing V3

Operate the high-recall detection, memory, prioritization, and routing layer of the investment process:

`News Radar V3 -> Research With Confidence -> Full Underwriting or Event-Trade Underwriting -> independent challenge when applicable -> Portfolio Capital Allocation -> Mind Model / monitoring`

Radar catches, normalizes, persists, and routes. It does not prove the thesis or declare a security investable.

## Stage boundary

Keep the stages distinct:

- **News Radar V3** owns detection, novelty control, canonical event memory, portfolio-defense priority, preliminary exposure mapping, and the exact next question.
- **Research With Confidence** owns independent verification, causality, counterfactuals, confounders, economic materiality, value capture, and whether a plausible expectations gap survives.
- **Full Underwriting** owns current price, capital structure and dilution, reverse valuation, scenarios, expected return, downside, opportunity cost, time-to-resolution, kill criteria, and the final security posture.
- **Portfolio Capital Allocation** owns loss budgets, weights, funding sources, cluster limits, and staged implementation.

Do not let an interesting Radar item consume the time needed to complete the broader high-recall scan.

## References

Read only what the run needs:

- `references/v3-run-contract.md` is authoritative for the V3 schedule, run manifest, late-event recovery, overdue-evidence checks, persistence, depth boundary, and compact output.
- `references/event-ledger-schema.md` for the canonical event record, novelty classes, thesis effects, observation types, and deduplication.
- `references/source-and-routing-rules.md` for source provenance, the five gates, priority routing, and scheduled-run behavior.
- `references/primary-source-feed-map.md` when defining source coverage, declaring scan limitations, or auditing missed feeds.
- `references/slow-burn-and-catalyst-lanes.md` for cumulative fundamental changes and pre-event expectations packets.
- `references/integration-and-persistence.md` when TaskTracker, Mind Model, Investing portfolios, Library fallback, or persistence are relevant.
- `references/social-arbitrage-lane.md` for behavioural or alternative-data observations.
- `references/clinical-radar-overlay.md` for medical research, clinical trials, regulator actions, and oncology alerts.
- `EXPERT_SOURCES.md` when monitoring named experts such as SemiAnalysis or Dylan Patel.

## Operating principles

- Optimize for **high recall with explicit uncertainty**, not a low-volume list containing only obvious winners.
- Treat every alert as a lead, not proof, a trade signal, a thesis update, or a valuation change.
- Protect existing capital first. Potential permanent-loss or thesis-breaking risk to a holding or active underwriting outranks new opportunity discovery.
- Compare every claim with its prior baseline. A new article is not necessarily new information.
- Search for cumulative changes and missing expected evidence, not only dramatic headlines.
- For known catalysts, freeze expectations before the result whenever practical.
- Separate **source origin** from **claim status**. A company release is primary evidence of what management said, not independent proof that the economics are correct.
- Timestamp first publication, underlying event time, first Radar detection, market status, and any price or volume reaction.
- Never invent a reaction while the relevant market is closed or use a price move as proof that a new fundamental event exists.
- Do not manufacture an investment angle, fill an alert quota, or force symmetrical positive and negative stories.
- Keep world outcome, company value capture, security valuation, event-trade suitability, and portfolio action separate.
- Automatically persist research-only Radar state when supported, but never automatically change a thesis, fair value, security posture, monitor threshold, or holding.

## Authoritative schedule

Scheduled V3 runs use:

- **08:00 America/Toronto**
- **11:30 America/Toronto**
- **15:00 America/Toronto**

Use the scan window since the last successful run. If a run is advanced, delayed, skipped, partial, or failed, preserve the reason and ensure the next run covers the gap.

## Workflow

### 1. Preflight the current state

Before broad discovery, load or attempt to load:

- the last successful run and current scan window;
- open Event Ledger records and existing independence groups;
- open P0, P1, and P2 items;
- evidence due now or overdue;
- known catalyst dates and frozen packets;
- live holdings and active underwritings;
- current monitors, kill criteria, and review dates;
- active Mind Model theses and watchlist candidates;
- available feeds, outages, and likely blind spots.

Start the V3 run coverage manifest. If a required state source is unavailable, mark the gap and do not imply that the associated holdings or theses were checked.

### 2. Run portfolio defense first

Search first for developments that could impair a holding or active underwriting, including:

- financing, liquidity, dilution, covenant, auditor, internal-control, fraud, safety, legal, regulatory, clinical, operational, customer-concentration, or governance risk;
- a breached or threatened kill criterion;
- a milestone, readout, financing, filing, permit, launch, or decision that was due but did not arrive;
- a material multi-holding or common-factor exposure.

P0 items take the fast path. Do not delay an urgent risk alert to complete second-order beneficiary work.

### 3. Scan the relevant lanes

Classify the run as one or more of:

- **Scheduled event scan** — the normal 08:00, 11:30, or 15:00 pass.
- **After-close capture** — record earnings, filings, trial results, and regulator actions for the next queue without automatically deep-researching everything.
- **User-supplied alert** — evaluate the exact item and its baseline.
- **Holdings-risk scan** — prioritize current capital at risk.
- **Slow-burn fundamental delta scan** — append and compare filings, calls, KPIs, estimates, trial records, capacity, financing, share count, risk factors, or monitor evidence.
- **Catalyst preparation** — create or refresh a frozen pre-event expectations packet.
- **Evidence-due scan** — check promised or scheduled evidence whose date or window has arrived.
- **Expert, social, or alternative-data scan** — identify original observations and preserve provenance.

Declare the actual source universe searched and unavailable feeds.

### 4. Reconcile every serious observation with the Event Ledger

For every serious alert, cumulative pattern, or overdue-evidence item:

1. identify the original source and underlying event;
2. search for the most relevant prior guidance, filing, trial record, policy baseline, monitor snapshot, or earlier reporting;
3. search the Event Ledger for the same underlying fact or independence group;
4. assign one `delta_class`, one `thesis_effect`, one `detection_status`, and one primary route;
5. group dependent coverage under one canonical `event_id`;
6. append atomic slow-burn observations rather than inventing a dramatic headline;
7. preserve a frozen catalyst packet and compare the result with it without rewriting the packet.

If the baseline is unknown, use `UNKNOWN`, state what must be checked, and do not call the event genuinely new.

#### Late-detection rule

If the underlying event predates the current scan window but no canonical record exists, classify it `LATE_DETECTION`, backfill it, measure latency, identify the likely missed-feed reason, and route it normally. Never reject a material unrecorded event merely because it should have been found earlier.

#### Missing-evidence rule

When expected evidence is absent or delayed, record the absence as an observation. Radar detects the change in the evidence state; RWC determines whether the absence is economically or probabilistically meaningful.

#### Price-dislocation rule

An unusual stock move can trigger a targeted source search, but price action alone does not pass Novelty. Use `PRICE_DISLOCATION_UNEXPLAINED` until an underlying event or defensible attribution is found.

### 5. Persist research-only state

For scheduled V3 runs, persist when supported:

- the run coverage manifest;
- canonical Event Ledger additions and updates;
- first-seen, detection, and event timestamps;
- duplicate and rejected items needed for calibration;
- atomic slow-burn observations;
- P2 evidence requests and due dates;
- catalyst packets;
- feed outages, late detections, and persistence failures.

Use the supported canonical store. If unavailable, save a dated Library artifact. If no write path succeeds, report `PERSISTENCE_FAILED`.

Do not use Radar persistence to change Mind Model probabilities, underwriting posture, fair value, entry ranges, kill criteria, review dates, or portfolio positions.

### 6. Apply the five hard gates

Assess each separately:

1. **Novelty** — is there a genuine information delta, independent confirmation, cumulative change, contradiction, new risk, or changed evidence state rather than repeated guidance, stale coverage, circular sourcing, or non-comparable data?
2. **Materiality** — could it materially change revenue, margins, cash flow, asset value, financing, probability, timing, or permanent-loss risk?
3. **Capture** — is there a listed security or existing thesis with sufficiently direct economic exposure?
4. **Expectation** — is there a plausible reason the market may not fully understand the magnitude, duration, ownership, timing, second-order consequence, or attribution?
5. **Researchability** — can a named document, datapoint, counterparty, benchmark, or dated catalyst resolve the important uncertainty?

Failure of Novelty, Materiality, or Capture normally means `REJECT / DUPLICATE`. An unresolved Expectation or Researchability gate normally means `P2` or `P3`, not a forced rejection.

Radar establishes only a plausible expectations question. RWC determines whether a genuine expectations gap survives.

### 7. Map only enough exposure to route correctly

For every serious item record:

- direct holding or security;
- linked thesis or underwriting;
- exposure type: `DIRECT`, `DERIVATIVE`, `READ_THROUGH`, or `NONE_IDENTIFIED`;
- preliminary mechanism;
- main capture uncertainty;
- portfolio cluster when relevant.

Require a second-order beneficiary and a false friend or comparator only for P1 opportunity discovery, industry or class-level events, bottleneck shifts, policy changes, or cases where cross-company transmission is the point of the lead.

Do not complete detailed value-capture ranking inside Radar.

### 8. Route the event

Assign exactly one primary route:

- **P0 — HOLDINGS / THESIS RISK:** potential thesis break, financing/liquidity problem, fraud/safety/regulatory issue, clinical hold or rejection, breached kill criterion, or another permanent-loss concern. Investigate first.
- **P1 — RESEARCH WITH CONFIDENCE NOW:** material, plausibly novel, economically traceable, and potentially misunderstood, misattributed, or incomplete.
- **P2 — TARGETED EVIDENCE:** one named fact, document, denominator, customer, comparator, causal link, or due item is missing. State exactly what and when.
- **P3 — MONITOR:** real development, but currently insufficient materiality, capture, expectation gap, or researchability.
- **REJECT / DUPLICATE:** false, stale, repeated without a new delta, immaterial, circularly sourced, inaccessible, non-comparable, or not meaningfully captured by a public security.

Radar may flag a possible short-duration setup, but it must not convert recency into a trade. Route factual verification through RWC and event payoff or execution questions to Event-Trade Underwriting.

### 9. Enforce the hard depth boundary

A normal Radar item stops after establishing:

- what changed versus baseline;
- source origin, claim status, and independence;
- timestamps and market status;
- plausible materiality and preliminary mechanism;
- affected holding, thesis, or candidate set;
- five-gate results;
- strongest reason the lead may fail;
- route;
- three or fewer decisive RWC questions;
- next evidence and date.

Stop and route when the remaining question is principally:

- causal attribution or counterfactual analysis;
- detailed economic materiality or value capture;
- complete expectations analysis;
- valuation, dilution, financing, scenario modeling, expected return, or timing;
- clinical-commercial underwriting;
- event payoff, options, liquidity, halt, borrow, or slippage;
- portfolio sizing, funding, cluster loss, or hedging.

Depth exceptions are limited to urgent P0 risk, comparison with an already frozen catalyst packet, retrieval of one time-sensitive classification document, or an explicitly requested combined workflow.

### 10. Produce the queue and coverage result

Lead with:

| Priority | Event ID | What changed | Affected holding / thesis | Gate issue | Route | Exact next question | Evidence / date |
|---|---|---|---|---|---|---|---|

Provide a concise detail block only for P0 and P1 items:

1. original source;
2. prior baseline;
3. delta class, thesis effect, and detection status;
4. preliminary mechanism and plausible materiality;
5. direct exposure and capture uncertainty;
6. strongest reason the lead may fail;
7. no more than three RWC questions;
8. next evidence and date.

For P2 and P3, state the missing evidence and date without expanding into a mini-report.

End with:

- holdings, active underwritings, theses, catalysts, and source lanes actually checked;
- material omissions, feed outages, or unavailable state;
- persistence status;
- next scheduled slot.

A valid no-lead run must be allowed. Say that no qualifying item was found in the searched universe, not that nothing material occurred anywhere.

## Handoff to Research With Confidence

A P0 or P1 handoff must preserve:

- `event_id`, lane, original source, and information cutoff;
- prior baseline, `delta_class`, `thesis_effect`, and `detection_status`;
- original Radar hypothesis;
- preliminary mechanism;
- direct exposure and main capture uncertainty;
- obvious confounders already visible without deep investigation;
- market-open/closed status and available price context;
- any frozen catalyst packet;
- strongest reason the lead may fail;
- three or fewer decisive questions;
- next evidence and date.

Do not ask RWC to prove the Radar thesis. Ask it to determine whether the claim, causality, materiality, value capture, and expectations gap survive independent verification and whether the lead deserves Full Underwriting, Event-Trade Underwriting, targeted research, waiting, monitoring, or rejection.

## Slow-burn cadence

- Intraday runs append genuinely new atomic observations.
- A structured weekly review compares the cumulative record with a dated, comparable baseline and decides whether it crosses the RWC threshold.
- Earnings, material filings, trial updates, or major operating disclosures trigger a comparable-period delta check.
- Preserve history. Do not rewrite earlier observations once the trend becomes obvious.

## Quality check

Before finishing, confirm that:

- the V3 coverage manifest was completed or its failure was declared;
- live holdings, active underwritings, monitors, theses, catalysts, and evidence-due items were checked or explicitly marked unavailable;
- the original event and prior baseline were checked;
- late detections were backfilled rather than discarded;
- overdue or missing expected evidence was checked;
- every event has one delta class, one thesis effect, one detection status, and one primary route;
- repeated coverage sharing one origin was deduplicated;
- source origin and claim status were not conflated;
- P0 risks were not delayed for broad thematic mapping;
- slow-burn evidence used comparable periods and preserved atomic observations;
- catalyst expectations were frozen before the outcome whenever practical;
- price action was not treated as proof of novelty;
- no RWC, underwriting, event-trade, or portfolio conclusion was smuggled into Radar;
- every P0/P1 item has three or fewer decisive RWC questions;
- every P2/P3 item has named next evidence or a reason no further work is warranted;
- research-only state was persisted or `PERSISTENCE_FAILED` was declared;
- a valid no-lead run was allowed rather than lowering the gates.
