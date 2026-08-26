---
name: radar-calibration-audit
description: Audit the News Radar, Research With Confidence, Full Underwriting, Event-Trade Underwriting, Underwriting Challenger, and Portfolio Capital Allocation funnel using preserved Event Ledger records, routes, confidence levels, decisions, allocation risk budgets, and later resolutions. Measure capture, latency, novelty, slow-burn detection, catalyst expectation accuracy, source and category yield, confidence calibration, missed events, false positives, decision quality, execution feasibility, and risk-budget adherence without hindsight or survivorship bias. Use for periodic process reviews or when improving the investment-research system. Do not use to underwrite one security or optimize rules from a tiny sample.
---

# Radar Calibration Audit

Evaluate whether the research process is finding the right information, routing it efficiently, assigning calibrated confidence, distinguishing investment from event trade, allocating capital within stated risk limits, and producing good decisions with the information available at the time.

This is a process audit, not a victory lap and not a backtest that selects only successful ideas.

## Reference

Read `references/audit-schema-and-metrics.md` for the required original snapshot, resolution fields, lane-specific metrics, and outcome windows.

## Core rules

- Include all material events: advances, waits, monitors, rejections, duplicates, slow-burn patterns, catalyst packets, event trades, allocations, and missed events discovered later.
- Preserve the original timestamp, information set, price, lane, route, confidence, thesis, expectations packet, horizon, and risk budget.
- Judge factual, research, underwriting, trade, allocation, and outcome quality separately.
- Prevent hindsight, look-ahead, survivorship, selection, source-availability, and implementation bias.
- Do not rewrite the original record after resolution. Append resolution data.
- Do not promote new weights, thresholds, source rules, or sizing caps from a small or highly dependent sample.
- Separate event categories, source origins, market regimes, security sizes, holding horizons, and decision lanes before aggregating results.
- A process can make a sound decision that loses money and a poor decision that makes money.
- A theoretically attractive event trade that was not executable is not a successful signal.
- A winning position that breached its stated portfolio loss budget or cluster limit is not evidence of sound allocation.

## Inputs

Use when available:

- Event Ledger records and Radar lane;
- source origin, claim status, and independence groups;
- five-gate results and P0/P1/P2/P3/reject route;
- slow-burn observation history and threshold-crossing decision;
- frozen catalyst expectations packets and post-event comparisons;
- RWC outcome and confidence by claim;
- Full Underwriting posture, probabilities, values, horizon, hurdle, and challenger result;
- Event-Trade posture, event tree, breakpoints, executable price assumptions, and costs;
- Portfolio Capital Allocation posture, loss budget, proposed weight, funding source, cluster exposure, and entry rules;
- monitor updates and thesis changes;
- prices and relevant benchmarks at the original timestamp and suitable outcome windows;
- known material events in the defined universe that the Radar missed.

State data gaps and do not imply complete coverage when the event universe, source universe, portfolio record, or execution data is incomplete.

## Workflow

### 1. Freeze the audit cohort

Define before examining outcomes:

- start and end dates;
- covered markets, source feeds, event categories, securities, holdings, and Radar lanes;
- scheduled scan times, slow-burn review cadence, catalyst universe, and outages;
- minimum materiality threshold for the missed-event universe;
- evaluation windows appropriate to each route and stated horizon;
- which portfolio and allocation decisions are included;
- which trades were theoretical versus actually implementable or executed.

Do not add or remove cases after seeing outcomes.

### 2. Validate record integrity

Check that each case retains when applicable:

- original first-seen and underlying-event times;
- Radar lane, baseline, delta class, and thesis effect;
- original route and confidence;
- original price context and market status;
- source coverage declaration;
- frozen catalyst expectation or slow-burn observation history;
- next evidence/date;
- underwriting and challenger versions;
- event-trade assumptions and executable-price timestamp;
- allocation loss budget, weight, funding source, and binding constraint;
- later updates as append-only records.

Flag missing or overwritten fields before calculating metrics.

### 3. Measure detection and routing

Calculate where data permits:

- **Capture rate:** material known events detected / material known events in the defined universe.
- **Capture latency:** time from original public source to first Radar detection.
- **Novelty precision:** share of events labelled new that were genuinely incremental.
- **Duplicate rate:** repeated events incorrectly treated as new.
- **P0 recall:** share of material holding/thesis risks surfaced promptly.
- **P1 precision:** share of P1 leads that survived RWC.
- **P2 resolution yield:** share of targeted-evidence items resolved by the named evidence.
- **Underwriting yield:** share of RWC advances becoming INVESTABLE or PRICE-SENSITIVE.
- **Research waste:** work spent on items later found stale, immaterial, unobservable, or weakly captured.
- **Lane mix:** event-news, after-close, holdings-risk, slow-burn, catalyst, expert, social/alternative, and clinical contributions.

A lower P1 survival rate is not automatically bad if Radar is intentionally high recall. Interpret it with research cost and missed-event rate.

### 4. Audit slow-burn and catalyst lanes

For slow-burn cases measure:

- time from first atomic observation to materiality recognition;
- share of promoted patterns that later proved cumulative and comparable;
- missed patterns where no single headline existed;
- false trends caused by seasonality, definition changes, acquisitions, FX, or dependent evidence;
- whether the named confirming or falsifying metric arrived.

For catalyst packets measure:

- percentage created before the event rather than reconstructed afterward;
- completeness of date, source, expectations, price, scenarios, ownership, and surprise thresholds;
- accuracy of expected-versus-surprise classification;
- frequency of treating known results as new surprises;
- whether the first post-event evidence and routing decision matched the packet.

Do not grade a catalyst packet by whether the stock rose. Grade whether it captured the ex-ante expectation and enabled a better decision.

### 5. Measure source and category performance

For each source origin, feed, expert lane, Radar lane, and event category report:

- number of unique-origin events;
- capture latency;
- novelty precision;
- P1 rate and RWC survival;
- underwriting or event-trade yield;
- confidence calibration;
- average research effort where known;
- common false-positive and missed-event patterns.

Do not reward a source for derivative articles or multiple events sharing one origin.

### 6. Test confidence calibration

Resolve claim-level confidence, not only final stock outcomes. Group comparable claims by stated confidence and report observed resolution rates or qualitative calibration when sample size is insufficient.

Check separately:

- event factual accuracy;
- mechanism validity;
- company value capture;
- materiality;
- security mispricing;
- scenario probabilities;
- event-surprise classification;
- execution feasibility;
- allocation-risk assumptions.

Use reliability diagrams, Brier scores, or log scores only when probabilities and sample sizes support them. Otherwise report counts, ranges, and uncertainty.

### 7. Evaluate investment underwriting and outcomes

For each promoted investment preserve:

- original posture and entry condition;
- original tradable price;
- expected holding period and realization date;
- expected and scenario returns;
- hurdle and closest alternative;
- challenger result;
- benchmark and factor context;
- maximum favourable and adverse excursion;
- outcome at suitable windows such as 1, 5, 20, 60, and 120 trading days when relevant;
- whether the predicted fundamental metric materialized;
- whether the thesis was upgraded, downgraded, killed, or merely delayed.

Use abnormal returns only when a defensible benchmark is available. Do not judge a two-year thesis solely on a five-day price move.

### 8. Evaluate event-trade decisions

For every Event-Trade case measure when available:

- whether the focal information was genuinely new versus expected;
- event-state and probability accuracy;
- modeled versus executable entry and exit;
- spread, slippage, fees, borrow, option premium, and volatility-crush accuracy;
- halt, gap, delay, and liquidity assumptions;
- maximum favourable and adverse excursion during the stated holding window;
- whether the original no-trade or price-sensitive condition was respected;
- decision quality for theoretical signals separately from realized implementation.

Do not annualize or pool one-off event returns as if identical opportunities can be repeated continuously.

### 9. Evaluate capital allocation

For each allocation decision audit:

- stated portfolio loss budget and Bear loss;
- arithmetic of the downside-derived maximum weight;
- confidence, liquidity, event, and cluster adjustments;
- proposed versus actual initial and target weights when available;
- funding source and whether the replaced idea was fairly compared;
- cluster exposure before and after;
- combined Bear loss under correlated scenarios;
- adherence to staged entry and cancellation rules;
- add, trim, and exit discipline;
- whether the mandatory re-underwrite date was honored.

Report **risk-budget adherence** separately from returns. A profitable oversized position can still be an allocation-process failure.

### 10. Run missed-event and false-positive reviews

For missed events or slow-burn patterns ask:

- Was the source feed absent or unavailable?
- Did the source-coverage declaration reveal the blind spot?
- Did deduplication suppress a genuine delta?
- Did materiality, comparability, or capture mapping fail?
- Was the catalyst absent from the calendar?
- Was the event outside the declared universe?
- Was it visible only with hindsight?

For false positives ask:

- Was the baseline wrong?
- Was one origin counted as independent confirmation?
- Did a plausible mechanism lack scale?
- Was value captured by another company?
- Was the event already expected?
- Did a slow-burn trend use non-comparable data?
- Did the event-trade model use non-executable prices?
- Did the lead depend on an unobservable narrative?

### 11. Recommend process changes conservatively

For every proposed change state:

- observed failure pattern;
- sample size and dependence;
- expected benefit;
- risk of reducing recall or creating a new bias;
- affected lane and metric;
- forward-test period and success metric;
- rollback condition.

Prefer narrow corrections and forward tests. Do not tune the process to the last winner, loser, missed event, or oversized success.

## Required output

### Audit scope and data quality

### Funnel and lane scorecard

| Metric | Result | Sample | Interpretation | Confidence |
|---|---:|---:|---|---|

### Source, category, and lane diagnostics

### Slow-burn and catalyst review

### Confidence calibration

### Missed events and patterns

### False positives and research waste

### Investment decision-quality review

### Event-trade execution-quality review

### Capital-allocation and risk-budget review

Separate sound losing decisions, unsound winning decisions, well-executed outcomes, non-executable theoretical signals, and profitable risk-budget violations.

### Recommended changes

Rank as:

- implement now;
- forward-test;
- monitor only;
- reject.

### Next audit date and preserved cohort

## Boundaries

Do not retroactively alter original probabilities, routes, catalyst packets, event trees, allocation weights, or risk budgets. Do not convert process metrics into a claim of investable alpha without a properly designed out-of-sample strategy test. Hand trading-strategy performance questions to the appropriate backtesting workflow.
