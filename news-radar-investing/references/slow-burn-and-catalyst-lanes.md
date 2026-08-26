# Slow-Burn Fundamental Delta and Catalyst Lanes

Use these lanes alongside the event-news scan. They exist because material information can accumulate without a dramatic headline, and because known catalysts should be framed before the result arrives.

## Slow-burn fundamental delta lane

### Purpose

Detect cumulative evidence that changes an investment thesis even when no single item would dominate a normal news feed.

### Typical inputs

- guidance language and estimate revisions;
- backlog, book-to-bill, pricing, utilization, capacity, lead times, or customer concentration;
- unit economics, gross-margin bridge, capex intensity, working capital, or free-cash-flow conversion;
- share-count drift, compensation, financing, debt, covenants, liquidity, or capital allocation;
- risk-factor, accounting-policy, segment, KPI, or non-GAAP definition changes;
- trial enrollment, protocol, endpoint, site, completion-date, safety, or regulator-status changes;
- permits, project schedules, reserves/resources, recoveries, costs, contract coverage, or fleet fixtures;
- repeated small channel checks, customer evidence, product availability, traffic, app rankings, pricing, or alternative data;
- management wording changes across filings, calls, presentations, and designated channels.

### Method

1. Establish a dated baseline from the last comparable disclosure or monitor snapshot.
2. Compare like with like. Do not treat seasonality, reporting-definition changes, acquisitions, or FX as business deltas without adjustment.
3. Record each atomic observation under one durable `event_id` or thesis-monitor record.
4. Distinguish:
   - one-off noise;
   - repeated confirmation;
   - acceleration or deceleration;
   - contradiction of the current thesis;
   - cumulative evidence that crosses a materiality threshold.
5. Express the bridge as:

   `Observed delta -> operating driver -> financial variable -> thesis probability or value effect`

6. Route a cumulative pattern to RWC when it can materially change the thesis, even if no single observation would qualify as P1 by itself.

### Guardrails

- Do not add several dependent observations as though they were independent confirmations.
- Do not infer a trend from two non-comparable periods.
- Do not let a headline scan crowd out filings, transcripts, trial-registry changes, or monitor evidence.
- Do not treat consensus revisions as proof; identify the underlying evidence and whether it is already reflected in price.
- Preserve the first observation and append later evidence. Do not rewrite the history once the trend becomes obvious.

### Slow-burn output

For each material pattern state:

- baseline date and metric;
- current date and metric;
- number of independent observations;
- comparability limitations;
- trend classification;
- likely thesis effect;
- confidence and strongest alternative explanation;
- next confirming or falsifying evidence and date;
- route: P0, P1, P2, P3, or reject/noise.

## Catalyst preparation lane

### Purpose

Create an expectations packet before a known event so the post-event process can distinguish a genuine surprise from a result the market already anticipated.

### Suitable catalysts

- earnings, investor days, product launches, contract awards, policy decisions, court rulings, index changes, financing, or transaction votes;
- clinical readouts, conference abstracts, PDUFA or other regulatory decisions, label changes, reimbursement, or trial updates;
- resource updates, studies, permits, drill programs, construction milestones, shipping fixtures, rate resets, or commodity-policy events.

### Required pre-event packet

Record before the result whenever possible:

```text
catalyst_id / linked event_id
security and affected thesis
scheduled date, time, timezone, and market status
known decision window or possible delay
source establishing the date
prior baseline and current consensus/common expectation
company guidance versus independent expectation
pre-event price, run-up/selloff, volatility, and material positioning evidence when available
key operating, clinical, regulatory, legal, or transaction variables
capital structure, milestones, royalties, financing, or ownership claims affected
bear / expected / upside result definitions
what would constitute a genuine positive or negative surprise
likely fundamental effect versus recognition-only effect
first documents or data to retrieve after the result
post-event RWC question
```

Do not invent an options-implied move, consensus, or market probability when reliable data is unavailable. Label the expectation as unknown and state what proxy was used.

### Post-event comparison

When the result arrives:

1. freeze the pre-event packet;
2. compare actual versus the predefined expectation, not versus a vague headline;
3. classify the information delta and thesis effect;
4. separate result quality, market reaction, and investability;
5. route to RWC, Full Underwriting, Event-Trade Underwriting, monitor, or rejection as appropriate.

### Special clinical rule

For clinical or regulatory catalysts, define in advance:

- population, comparator, endpoint hierarchy, effect-size threshold, confidence interval, maturity, safety threshold, subgroup expectations, and likely label breadth;
- commercial rights, milestone/royalty ownership, runway, financing, and pre-event probability already embedded in the security.

A statistically positive result can still be commercially weak, already expected, poorly owned, or uninvestable at the current price.
