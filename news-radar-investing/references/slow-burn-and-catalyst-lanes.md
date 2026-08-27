# Slow-Burn Fundamental Delta and Catalyst Lanes — V3

Use these lanes alongside the event-news scan. They exist because material information can accumulate without a dramatic headline, because missing expected evidence can itself change the information state, and because known catalysts should be framed before the result arrives.

## Slow-burn fundamental delta lane

### Purpose

Detect cumulative evidence that changes an investment thesis even when no single item would dominate a normal news feed.

Radar detects and preserves the pattern. Research With Confidence determines whether the trend survives comparability, confounder, causality, materiality, and value-capture tests.

### Typical inputs

- guidance language and estimate revisions;
- backlog, book-to-bill, pricing, utilization, capacity, lead times, or customer concentration;
- unit economics, gross-margin bridge, capex intensity, working capital, or free-cash-flow conversion;
- share-count drift, compensation, financing, debt, covenants, liquidity, or capital allocation;
- risk-factor, accounting-policy, segment, KPI, or non-GAAP definition changes;
- auditor, CFO, internal-control, related-party, restatement, or governance changes;
- trial enrollment, protocol, endpoint, site, completion-date, safety, or regulator-status changes;
- permits, project schedules, reserves or resources, recoveries, costs, contract coverage, or fleet fixtures;
- repeated small channel checks, customer evidence, product availability, traffic, app rankings, pricing, or alternative data;
- management wording changes across filings, calls, presentations, and designated channels;
- expected evidence that becomes overdue, disappears, or arrives with a meaningful delta.

### V3 cadence

Use different cadences for detection and promotion:

- **Each intraday scheduled run:** append genuinely new atomic observations, due-item status changes, and source outages. Do not reanalyze the whole historical series.
- **Structured weekly review:** compare the cumulative record with a dated, comparable baseline; identify independent observations; decide whether the pattern crosses the P0/P1/P2 threshold.
- **After earnings, a material filing, a trial update, or a major operating disclosure:** perform a mandatory comparable-period delta check.
- **At a named evidence or catalyst date:** record whether the evidence arrived, arrived with a delta, was delayed, or remains overdue.

A daily statement that no slow-burn pattern crossed a threshold is meaningful only when the run also states what new atomic observations and due items were checked.

### Method

1. Establish a dated baseline from the last comparable disclosure or monitor snapshot.
2. Compare like with like. Do not treat seasonality, definition changes, acquisitions, FX, geography, mix, or accounting presentation as business deltas without adjustment.
3. Record each atomic observation under one durable `event_id` or thesis-monitor record.
4. Distinguish:
   - one-off noise;
   - dependent repetition;
   - independent confirmation;
   - acceleration or deceleration;
   - contradiction of the current thesis;
   - changed disclosure quality;
   - missing or delayed expected evidence;
   - cumulative evidence that crosses a materiality threshold.
5. Express the preliminary bridge as:

   `Observed delta -> operating or probabilistic driver -> possible financial or thesis variable`

6. Route the cumulative pattern to RWC when it could materially change the thesis, even if no single observation would qualify as P1 by itself.

Radar should not complete the causal, value-capture, sensitivity, valuation, or return analysis.

### Missing expected evidence

Check every `next_evidence_date` that has arrived. Use the Event Ledger observation types when:

- a promised filing, result, customer proof, financing, permit, launch, project milestone, or regulator decision does not arrive;
- a trial completion date, enrollment target, endpoint, or decision window moves;
- a previously material KPI, segment table, risk factor, or management discussion disappears;
- repeated guidance remains unsupported past the date when observable proof was expected.

Record the changed evidence state and the strongest benign alternative explanation. Do not automatically treat absence as failure or update a thesis probability inside Radar.

### Guardrails

- Do not add dependent observations as though they were independent confirmations.
- Do not infer a trend from two non-comparable periods.
- Do not let a headline scan crowd out filings, transcripts, trial-registry changes, due evidence, or monitor snapshots.
- Do not treat consensus revisions as proof; identify the underlying evidence and whether the revision was already reflected in price.
- Preserve the first observation and append later evidence. Do not rewrite history once the trend becomes obvious.
- Do not silently roll an overdue date forward.
- Do not complete a mini-underwriting merely because the pattern is interesting.

### Slow-burn output

For each promoted pattern state:

- baseline date and metric;
- latest comparable date and metric;
- number of independent observations;
- detection status, including any late observation;
- comparability limitations;
- trend classification;
- likely thesis effect;
- confidence and strongest alternative explanation;
- exact RWC question;
- next confirming or falsifying evidence and date;
- route: P0, P1, P2, P3, or reject/noise.

## Catalyst preparation lane

### Purpose

Create an expectations packet before a known event so the post-event process can distinguish a genuine surprise from a result the market already anticipated.

### Suitable catalysts

- earnings, investor days, product launches, contract awards, policy decisions, court rulings, index changes, financing, or transaction votes;
- clinical readouts, conference abstracts, PDUFA or other regulator decisions, label changes, reimbursement, or trial updates;
- resource updates, studies, permits, drill programs, construction milestones, shipping fixtures, rate resets, or commodity-policy events.

### Required pre-event packet

Record before the result whenever possible:

```text
catalyst_id / linked event_id
security and affected thesis
scheduled date, time, timezone, and market status
known decision window or possible delay
source establishing the date
prior baseline and current consensus or common expectation
company guidance versus independent expectation
pre-event price, run-up or selloff, volatility, and material positioning evidence when available
key operating, clinical, regulatory, legal, or transaction variables
capital structure, milestones, royalties, financing, or ownership claims affected
bear / expected / upside result definitions
what would constitute a genuine positive or negative surprise
likely fundamental effect versus recognition-only effect
first documents or data to retrieve after the result
post-event RWC question
```

Do not invent an options-implied move, consensus, or market probability when reliable data is unavailable. Label the expectation unknown and state what proxy was used.

### Evidence-due handling

When the event window arrives:

1. check whether the result or decision appeared;
2. if absent, record `EXPECTED_EVIDENCE_MISSED`, `MILESTONE_DELAYED`, or `WINDOW_UNKNOWN` as appropriate;
3. preserve the original packet and due window;
4. identify the next official source or date;
5. route the meaning of the delay to RWC when it may be material.

Do not rewrite the packet to make a delayed or missing result appear expected.

### Post-event comparison

When the result arrives:

1. freeze the pre-event packet;
2. compare actual versus the predefined expectation, not versus a vague headline;
3. classify the information delta, thesis effect, and detection status;
4. separate result quality, market reaction, and investability;
5. route to RWC, Full Underwriting, Event-Trade Underwriting, monitor, or rejection as appropriate.

### Special clinical rule

For clinical or regulatory catalysts, define in advance:

- population, comparator, endpoint hierarchy, effect-size threshold, confidence interval, maturity, safety threshold, subgroup expectations, and likely label breadth;
- commercial rights, milestone or royalty ownership, runway, financing, and pre-event probability already embedded in the security.

A statistically positive result can still be commercially weak, already expected, poorly owned, financing-dependent, or uninvestable at the current price. Radar compares the result with the packet; RWC and underwriting own those deeper conclusions.
