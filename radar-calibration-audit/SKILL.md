---
name: radar-calibration-audit
description: Audit the News Radar, Research With Confidence, and Full Underwriting funnel using preserved Event Ledger records, routes, confidence levels, decisions, and later resolutions. Measure capture, latency, precision, source and category yield, confidence calibration, missed events, false positives, and decision quality without hindsight or survivorship bias. Use for periodic process reviews or when improving the investment-research system. Do not use to underwrite one security or optimize rules from a tiny sample.
---

# Radar Calibration Audit

Evaluate whether the research process is finding the right events, routing them efficiently, assigning calibrated confidence, and producing good decisions with the information available at the time.

This is a process audit, not a victory lap and not a backtest that selects only successful ideas.

## Reference

Read `references/audit-schema-and-metrics.md` for the required snapshot, resolution fields, metrics, and outcome windows.

## Core rules

- Include all material events: advances, waits, monitors, rejections, duplicates, and missed events discovered later.
- Preserve the original timestamp, information set, price, route, confidence, thesis, and expected horizon.
- Judge decision quality separately from subsequent price outcome.
- Prevent hindsight, look-ahead, survivorship, selection, and source-availability bias.
- Do not rewrite the original record after resolution. Append resolution data.
- Do not promote new weights, thresholds, or source rules from a small or highly dependent sample.
- Separate event categories, market regimes, security sizes, and holding horizons before aggregating results.
- A process can make a sound decision that loses money and a poor decision that makes money.

## Inputs

Use when available:

- Event Ledger records;
- source origin, claim status, and independence groups;
- five-gate results and P0/P1/P2/P3/reject route;
- RWC outcome and confidence by claim;
- Full Underwriting posture, probabilities, values, horizon, hurdle, and challenger result;
- monitor updates and thesis changes;
- prices and relevant benchmarks at the original timestamp and outcome windows;
- known material events in the defined universe that the Radar missed.

State data gaps and do not imply complete coverage when the event universe is incomplete.

## Workflow

### 1. Freeze the audit cohort

Define:

- start and end dates;
- covered markets, source feeds, event categories, and securities;
- scheduled scan times and outages;
- minimum materiality threshold for the missed-event universe;
- evaluation windows appropriate to each route and stated horizon.

Do not add or remove cases after seeing outcomes.

### 2. Validate record integrity

Check that each event retains:

- original first-seen and underlying-event times;
- baseline and delta class;
- original route and confidence;
- original price context and market status;
- next evidence/date;
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

A lower P1 survival rate is not automatically bad if Radar is intentionally high recall. Interpret it with research cost and missed-event rate.

### 4. Measure source and category performance

For each source origin, feed, expert lane, and event category report:

- number of unique-origin events;
- capture latency;
- novelty precision;
- P1 rate and RWC survival;
- underwriting yield;
- confidence calibration;
- average research effort where known;
- common false-positive and missed-event patterns.

Do not reward a source for derivative articles or multiple events sharing one origin.

### 5. Test confidence calibration

Resolve claim-level confidence, not only final stock outcomes. Group similar claims by stated confidence and report observed resolution rates or qualitative calibration when sample size is insufficient.

Check separately:

- event factual accuracy;
- mechanism validity;
- company value capture;
- materiality;
- security mispricing;
- scenario probabilities.

Use reliability diagrams, Brier scores, or log scores only when probabilities and sample sizes support them. Otherwise report counts, ranges, and uncertainty.

### 6. Evaluate decisions and outcomes

For each promoted security preserve:

- original recommendation or posture;
- entry condition and original tradable price;
- expected holding period and realization date;
- expected and scenario returns;
- benchmark and factor context;
- maximum favourable and adverse excursion;
- outcome at suitable windows such as 1, 5, 20, 60, and 120 trading days when relevant;
- whether the predicted fundamental metric materialized;
- whether the thesis was upgraded, downgraded, killed, or merely delayed.

Use abnormal returns only when a defensible benchmark is available. Do not judge a two-year thesis solely on a five-day price move.

### 7. Run missed-event and false-positive reviews

For missed events ask:

- Was the source feed absent?
- Did deduplication suppress a genuine delta?
- Did materiality or capture mapping fail?
- Was the event outside the declared universe?
- Was it visible only with hindsight?

For false positives ask:

- Was the baseline wrong?
- Was one origin counted as independent confirmation?
- Did a plausible mechanism lack scale?
- Was value captured by another company?
- Was the event already expected?
- Did the lead depend on an unobservable narrative?

### 8. Recommend process changes conservatively

For every proposed change state:

- observed failure pattern;
- sample size and dependence;
- expected benefit;
- risk of reducing recall or creating a new bias;
- forward-test period and success metric;
- rollback condition.

Prefer narrow corrections and forward tests. Do not tune the process to the last winner or loser.

## Required output

### Audit scope and data quality

### Funnel scorecard

| Metric | Result | Sample | Interpretation | Confidence |
|---|---:|---:|---|---|

### Source and category diagnostics

### Confidence calibration

### Missed events

### False positives and research waste

### Decision-quality review

Separate sound losing decisions, unsound winning decisions, and genuinely well-executed outcomes.

### Recommended changes

Rank as:

- implement now;
- forward-test;
- monitor only;
- reject.

### Next audit date and preserved cohort

## Boundaries

Do not retroactively alter original probabilities or routes. Do not convert process metrics into a claim of investable alpha without a properly designed out-of-sample strategy test. Hand trading-strategy performance questions to the appropriate backtesting workflow.
