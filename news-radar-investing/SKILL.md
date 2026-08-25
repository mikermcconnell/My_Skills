---
name: news-radar-investing
description: Scan and triage current public-equity news into a structured Event Ledger, distinguish genuine information deltas from recycled coverage, map possible financial transmission and listed-security exposure, prioritize risks to existing theses or holdings, and route the best leads to Research With Confidence. Use for scheduled News Radar runs, medical or cancer-trial radar, expert-source monitoring, or first-pass alert triage. Do not use for full valuation, final buy or sell decisions, or account-specific position sizing.
---

# News Radar Investing

Operate the high-recall front end of the investment process:

`News Radar -> Research With Confidence -> Full Underwriting -> portfolio/risk sizing -> Mind Model / monitoring`

Radar catches and routes. It does not prove the thesis or declare a security investable.

## References

Read only what the run needs:

- `references/event-ledger-schema.md` for the canonical event record, novelty classes, thesis effects, and deduplication.
- `references/source-and-routing-rules.md` for source provenance, the five gates, priority routing, and scheduled-run behavior.
- `references/integration-and-persistence.md` when TaskTracker, Mind Model, Investing portfolios, or persistence are relevant.
- `references/social-arbitrage-lane.md` for behavioural or alternative-data observations.
- `references/clinical-radar-overlay.md` for medical research, clinical trials, FDA actions, and oncology alerts.
- `EXPERT_SOURCES.md` when monitoring named experts such as SemiAnalysis or Dylan Patel.

## Operating principles

- Optimize for **high recall with explicit uncertainty**, not a low-volume list that only contains obvious winners.
- Treat every alert as a lead, not proof, a trade signal, or a thesis update.
- Prioritize potential permanent-loss or thesis-breaking risk to an existing holding before exciting new long ideas.
- Compare the claim with its prior baseline. A new article is not necessarily new information.
- Separate **source origin** from **claim status**. A company release is primary evidence of what management said, not independent proof that the claim is economically correct.
- Timestamp first publication, underlying event time, first radar detection, market status, and any price or volume reaction.
- Never invent a market reaction while the relevant market is closed.
- Do not manufacture an investment angle, fill an alert quota, or force symmetrical positive and negative stories.
- Keep world outcome, company value capture, security valuation, and portfolio action separate.
- Keep TaskTracker and Investing research-only unless Mike explicitly requests a supported write. Never place a trade or approve a Mind Model proposal.

## Workflow

### 1. Establish the run mode

Classify the run as one of:

- **Scheduled scan** — the normal 08:00, 12:00, or 15:00 America/Toronto pass.
- **After-close capture** — record and classify filings, earnings, trial results, or regulatory actions for the next research queue; do not automatically deep-research everything.
- **User-supplied alert** — evaluate the exact item and its baseline.
- **Holdings-risk scan** — search first for developments that could impair an existing thesis or create a time-sensitive review.

Use the scan window since the last successful run. Preserve the original first-seen timestamp when later articles repeat the same event.

### 2. Create or update the Event Ledger record

For every serious alert:

1. identify the original source and underlying event;
2. find the most relevant prior company guidance, filing, trial record, policy baseline, or earlier reporting;
3. assign one `delta_class` and one `thesis_effect` from the Event Ledger schema;
4. group dependent reporting under one origin rather than treating it as independent confirmation;
5. link duplicate or follow-up coverage to the existing `event_id` instead of creating a new lead.

If the baseline is unknown, use `UNKNOWN`, state what must be checked, and do not call the event genuinely new.

### 3. Apply the five hard gates

Assess each gate separately. Do not hide a fatal weakness inside a composite score.

1. **Novelty** — is there a genuine information delta rather than repeated guidance, a stale article, or circular sourcing?
2. **Materiality** — could the delta materially change revenue, margins, cash flow, asset value, financing, probability, timing, or permanent-loss risk?
3. **Capture** — is there a listed security with sufficiently direct economic exposure?
4. **Expectation** — is there a plausible reason the market has not fully incorporated the information, or may have misattributed or overreacted to it?
5. **Researchability** — can the important uncertainty be resolved with observable evidence within a useful decision horizon?

Failure of Novelty, Materiality, or Capture normally means `REJECT / DUPLICATE`. An unresolved Expectation or Researchability gate normally means `P2` or `P3`, not a forced rejection.

### 4. Map the value chain without underwriting it

For a lead that passes the first three gates, identify:

- the obvious issuer or direct beneficiary;
- at least one plausible second-order beneficiary or alternative expression;
- at least one apparently related company that should **not** be advanced because exposure is weak, economics are captured elsewhere, or the event is already obvious;
- potential losers, comparators, or hedges when they improve understanding;
- any existing holding or Mind Model thesis that is directly affected.

Require a plausible path to orders, units, pricing, margins, cash flow, assets, financing, or a dated probabilistic event. Theme association alone is insufficient.

### 5. Route the event

Assign exactly one primary route:

- **P0 — HOLDINGS / THESIS RISK:** potential thesis break, financing/liquidity problem, fraud/safety/regulatory issue, or another permanent-loss concern. Investigate first.
- **P1 — RESEARCH WITH CONFIDENCE NOW:** material, plausibly novel, economically traceable, and potentially mispriced or misattributed.
- **P2 — TARGETED EVIDENCE:** interesting, but one named fact, document, denominator, customer, or causal link is missing. State the exact evidence and expected date.
- **P3 — MONITOR:** real development, but currently insufficient materiality, capture, expectation gap, or researchability.
- **REJECT / DUPLICATE:** false, stale, repeated guidance without a new delta, immaterial, circularly sourced, inaccessible, or not meaningfully investable through public securities.

Radar may identify a possible fast event-trade candidate, but it must not turn recency alone into a trade. Final event-trade or investment decisions belong to the appropriate deeper workflow.

### 6. Produce the research queue

Lead with a compact queue:

| Priority | Event ID | Delta | Affected security / thesis | Why it matters | Route | Next evidence / date | Confidence |
|---|---|---|---|---|---|---|---|

Then provide detail only for the most decision-relevant events:

1. **What changed** — exact new claim, baseline, timestamps, and market status.
2. **Evidence status** — source origin, claim status, independence group, conflicts, and limitations.
3. **Preliminary mechanism** — how the event could reach financial variables; label this as a hypothesis.
4. **Security map** — direct, second-order, non-beneficiary/comparator, and existing exposure.
5. **Gate results** — pass/fail/unknown for all five gates.
6. **Routing reason** — why it is P0, P1, P2, P3, or rejected.
7. **Research handoff** — one falsifiable question and the evidence that would resolve it.

Do not assign a 1-10 investability score at this stage. Do not issue `INITIATE`, `ADD`, `TRIM`, or `EXIT` unless a separate authorized underwriting or portfolio workflow has already reached that conclusion.

## Handoff to Research With Confidence

A P0 or P1 handoff must include:

- `event_id` and original source;
- prior baseline and `delta_class`;
- `thesis_effect`;
- the original Radar hypothesis;
- the preliminary causal mechanism;
- obvious confounders or competing explanations;
- the direct and second-order security map;
- market-open/closed status and available pre/post-event price context;
- the strongest reason the lead may fail;
- three or fewer decisive research questions;
- the next evidence date when known.

Do not ask Research With Confidence to prove the Radar thesis. Ask it to determine whether the thesis survives independent verification and whether it deserves Full Underwriting.

## Stop conditions

Stop Radar work and route rather than expanding into a full report when:

- the question has become one of valuation, dilution, scenario modeling, or expected return;
- a primary document or named data point will soon resolve the uncertainty;
- the mechanism is real but no listed company captures enough value;
- the event is important to the world but immaterial to the security;
- the market expectation cannot be assessed without deeper research;
- additional scanning has low expected decision value.

## Quality check

Before finishing, confirm that:

- the original event and prior baseline were both checked;
- every event has one delta class, one thesis effect, and one primary route;
- repeated coverage sharing one origin was deduplicated;
- source origin and claim status were not conflated;
- holdings and thesis risks were prioritized;
- the obvious beneficiary was not automatically treated as the best security;
- no final valuation or buy/sell decision was smuggled into the Radar stage;
- every P0/P1 item has a specific RWC question;
- every P2/P3 item has named next evidence or a reason no further work is warranted.
