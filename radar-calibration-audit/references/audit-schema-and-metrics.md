# Audit Schema and Metrics

## Original-decision snapshot

Preserve at the time of the decision. Use null or `NOT_APPLICABLE` rather than omitting a field when the schema is persisted.

```text
event_id
radar_lane
first_seen_at
underlying_event_at
source_origin
source_coverage_declaration
independence_group
prior_baseline
delta_class
thesis_effect
five_gates
original_route
original_confidence_by_claim
security_map
original_price_and_market_status
slow_burn_observations_and_threshold
catalyst_packet_created_at
catalyst_expectations_and_surprise_thresholds
rwc_outcome
underwriting_posture
scenario_probabilities_and_values
expected_return_and_horizon
hurdle_and_alternative
challenge_status
event_trade_posture
event_tree_and_breakpoints
modeled_executable_price_and_costs
portfolio_allocation_posture
portfolio_loss_budget
proposed_initial_and_target_weight
funding_source
cluster_exposure_before_and_after
allocation_binding_constraint
entry_add_trim_exit_rules
next_evidence_and_date
```

Do not require investment, event-trade, or allocation fields for a rejected Radar item. Preserve the fields relevant to the route it reached.

## Resolution append

Never overwrite the original snapshot. Append:

```text
resolved_at
resolution_status
fact_accuracy
mechanism_validity
capture_validity
materiality_validity
mispricing_validity
named_evidence_arrived
slow_burn_pattern_validity
catalyst_surprise_classification_accuracy
thesis_status_change
fundamental_metric_outcome
price_outcomes
benchmark_outcomes
maximum_favourable_excursion
maximum_adverse_excursion
modeled_vs_executable_entry
modeled_vs_executable_exit
realized_or_estimated_slippage_and_costs
halt_gap_delay_or_borrow_outcome
event_trade_decision_quality
allocation_actual_weight_when_available
portfolio_risk_budget_adherence
cluster_limit_adherence
entry_rule_adherence
reunderwrite_date_adherence
research_effort
post_mortem_category
notes
```

## Core funnel metrics

### Capture rate

```text
material events detected / material events in the predefined auditable universe
```

The denominator must be defined independently of Radar output, such as all qualifying regulatory decisions, index constituents' material filings, a fixed catalyst calendar, or a curated ex-post event set using rules fixed before outcome review.

### Capture latency

Measure from the original public source timestamp to `first_seen_at`. Report median, percentiles, and late-tail cases rather than only an average.

### Novelty precision

```text
genuinely incremental events labelled new / all events labelled GENUINELY_NEW
```

### Duplicate rate

```text
dependent or repeated events incorrectly opened as new / all evaluated event records
```

### P1 precision

```text
P1 leads that survive RWC / all completed P1 RWC investigations
```

Interpret with P1 recall and research effort. High-recall systems may rationally accept lower precision.

### Underwriting yield

```text
RWC advances ending INVESTABLE or PRICE-SENSITIVE / completed RWC advances
```

Also report WATCH, PASS, REJECT, and unresolved counts.

## Lane-specific metrics

### Slow-burn detection yield

Report at least:

```text
material cumulative patterns detected before a discrete headline / all auditable material slow-burn patterns
promoted slow-burn patterns later validated / completed promoted slow-burn patterns
median time from first atomic observation to materiality recognition
```

Audit comparability failures, dependent observations, seasonality, definition changes, and trends recognized only with hindsight.

### Catalyst packet coverage and accuracy

```text
eligible known catalysts with packet frozen pre-event / eligible known catalysts
correct expected-versus-surprise classifications / resolved catalyst packets
known results incorrectly treated as new surprise / resolved catalyst packets
```

Packet quality should also be audited for date, source, price, expectation, ownership economics, scenario thresholds, and post-event retrieval plan.

### Event-trade routing and execution

Report separately:

```text
RWC cases routed to Event-Trade Underwriting / eligible short-duration cases
TRADEABLE or condition-sensitive cases / completed event-trade cases
NO TRADE and REJECT counts
theoretical edge remaining after credible costs
modeled versus executable entry and exit difference
no-trade condition adherence
halt, gap, delay, borrow, and options-assumption accuracy
```

Do not mix unexecuted theoretical signals with realized trades. Do not interpret raw event returns without the original holding window and entry condition.

### Portfolio allocation discipline

Report:

```text
allocations with explicit portfolio loss budget / completed allocation decisions
allocations within downside-derived and adjusted maximum / allocations made
cluster-limit adherence
funding-source completeness
staged-entry rule adherence
mandatory re-underwrite date adherence
profitable but oversized cases
losing but risk-budget-compliant cases
```

Risk-budget adherence is a process outcome independent of investment return.

## Confidence calibration

When numeric probabilities exist, use Brier score or log loss by comparable claim class. For categorical confidence, report observed resolution ranges and confidence intervals when feasible.

Do not pool:

- factual-event confidence;
- mechanism confidence;
- company value-capture confidence;
- security-mispricing confidence;
- event-surprise confidence;
- execution confidence;
- allocation-risk confidence.

## Outcome windows

Use windows appropriate to the stated thesis. A default diagnostic panel may include:

- 1 trading day;
- 5 trading days;
- 20 trading days;
- 60 trading days;
- 120 trading days;
- stated event-trade exit window;
- stated target realization date;
- mandatory re-underwrite date.

Do not treat these as automatic trade exits. They are diagnostic observations.

## Decision-quality matrix

| Process quality | Outcome | Interpretation |
|---|---|---|
| Sound | Positive | Good decision, favourable outcome |
| Sound | Negative | Good decision, adverse outcome or variance |
| Unsound | Positive | Lucky result; process needs correction |
| Unsound | Negative | Bad decision and bad outcome |

Additional implementation classifications:

| Signal quality | Implementation | Interpretation |
|---|---|---|
| Sound | Executable and rule-compliant | Valid process observation |
| Sound | Not executable | Research insight, not a realizable trade result |
| Sound | Oversized or rule-breaking | Allocation failure despite a sound signal |
| Unsound | Profitable | Lucky trade or investment; do not reward the process |

Judge soundness using information available at the time, not later knowledge.

## Minimum evidence for a process change

There is no universal sample threshold. Require enough independent cases to make the failure pattern credible. State:

- number of events;
- number of independent origins;
- lane, category, and regime concentration;
- uncertainty around the metric;
- expected effect on recall and research effort;
- forward-test design and rollback condition.

Changes affecting recall, routing, source coverage, event-trade thresholds, or allocation caps should be forward-tested before permanent adoption whenever practical.
