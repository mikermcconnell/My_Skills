# Audit Schema and Metrics

## Original-decision snapshot

Preserve at the time of the decision. Use null or `NOT_APPLICABLE` rather than omitting a field when the schema is persisted.

```text
radar_version
run_id
run_timestamp
scheduled_slot
run_status
scan_window_start
scan_window_end
last_successful_run_at
coverage_manifest
persistence_status
event_id
observation_type
detection_status
first_seen_at
original_publication_at
underlying_event_at
detection_latency
missed_feed_reason
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
exposure_links
linked_holdings
linked_underwritings
linked_theses
portfolio_cluster
original_price_and_market_status
slow_burn_observations_and_threshold
expected_evidence_status
next_evidence_and_date
catalyst_packet_created_at
catalyst_expectations_and_surprise_thresholds
rwc_handoff_questions
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
```

Do not require investment, event-trade, or allocation fields for a rejected Radar item. Preserve the fields relevant to the route it reached.

For News Radar V3, the `coverage_manifest` should retain when applicable:

```text
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
next_scheduled_slot
```

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
expected_evidence_arrival_status
slow_burn_pattern_validity
catalyst_surprise_classification_accuracy
late_detection_root_cause_confirmed
whether_detection_delay_reduced_decision_usefulness
coverage_omission_discovered
persistence_record_verified
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
radar_depth_spillover
post_mortem_category
notes
```

## News Radar V3 integrity metrics

These metrics test whether V3 is operationally reliable before evaluating investment outcomes.

### Coverage-manifest completeness

```text
scheduled runs with all required manifest fields / completed scheduled runs
```

Also report separately:

- runs with live holdings loaded;
- runs with active underwritings and monitors loaded;
- runs with theses and watchlists loaded;
- runs with catalyst and evidence-due queues checked;
- runs whose limitations were accurately declared;
- runs that implied coverage not supported by the manifest.

### Persistence completeness

```text
scheduled runs with verified research-state persistence / completed scheduled runs
```

Break out:

- canonical Event Ledger writes;
- TaskTracker research writes;
- Library fallback artifacts;
- `PERSISTENCE_FAILED` runs;
- writes that created duplicate canonical events;
- writes that improperly changed a thesis, underwriting decision, monitor, or holding.

### Late-detection rate

```text
material events first captured as LATE_DETECTION / material events detected
```

Report latency distribution, missed-feed reasons, affected lanes, and whether the delay reduced decision usefulness. A late detection is preferable to a permanent miss but remains a process failure to diagnose.

### Scan-gap recovery

```text
failed, delayed, skipped, or advanced slots whose next run correctly resumed from the last successful timestamp / disrupted scheduled slots
```

Flag silent gaps and overlapping windows that caused duplicate work.

### Evidence-due compliance

```text
due or overdue evidence items checked at the next scheduled run / evidence items whose due window arrived
```

Also measure:

- overdue dates silently rolled forward;
- missing evidence correctly recorded as a changed evidence state;
- benign administrative delays incorrectly treated as thesis failures;
- meaningful absences missed until later;
- P2 items resolved by the named evidence.

### P0 portfolio-defense coverage

```text
material holding or active-underwriting risks surfaced promptly / auditable material holding or underwriting risks
```

Audit whether P0 alerts were delayed by thematic mapping, broad discovery, or mini deep dives.

### Radar depth discipline

Report:

```text
P0/P1 handoffs with three or fewer decisive RWC questions / completed P0/P1 handoffs
Radar items that expanded into causal, valuation, scenario, return, or position-size work without an allowed exception / completed Radar items
median Radar research effort by route
```

A lower research effort is not automatically better. The target is enough work to route correctly without crowding out coverage or duplicating RWC and underwriting.

## Core funnel metrics

### Capture rate

```text
material events detected / material events in the predefined auditable universe
```

The denominator must be defined independently of Radar output, such as all qualifying regulatory decisions, index constituents' material filings, a fixed catalyst calendar, or a curated ex-post event set using rules fixed before outcome review.

### Capture latency

Measure from the original public source timestamp to `first_seen_at`. Report median, percentiles, and late-tail cases rather than only an average. Separate on-time detections from backfilled late detections.

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
weekly slow-burn reviews completed / scheduled weekly reviews
material filings or trial updates receiving comparable-period delta checks / eligible disclosures
```

Audit comparability failures, dependent observations, seasonality, definition changes, missing evidence, and trends recognized only with hindsight.

### Catalyst packet coverage and accuracy

```text
eligible known catalysts with packet frozen pre-event / eligible known catalysts
correct expected-versus-surprise classifications / resolved catalyst packets
known results incorrectly treated as new surprise / resolved catalyst packets
catalyst windows checked when due / eligible due windows
```

Packet quality should also be audited for date, source, price, expectation, ownership economics, scenario thresholds, post-event retrieval plan, and whether a delay or missing result was preserved rather than retroactively normalized.

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

## Source, feed, and category performance

For each source origin, feed, expert lane, event category, and Radar lane report:

- unique-origin events;
- on-time captures;
- late detections attributable to the feed;
- capture latency;
- novelty precision;
- duplicate contribution;
- P1 rate and RWC survival;
- underwriting or event-trade yield;
- evidence-due resolution yield;
- average research effort where known;
- common false-positive and missed-event patterns;
- outage frequency and whether the coverage manifest disclosed it.

Do not reward a source for derivative articles or multiple events sharing one origin.

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

- number of events and scheduled runs;
- number of independent origins;
- lane, category, and regime concentration;
- uncertainty around the metric;
- expected effect on recall, coverage, latency, and research effort;
- forward-test design and rollback condition.

Changes affecting recall, routing, source coverage, persistence, evidence-due rules, event-trade thresholds, or allocation caps should be forward-tested before permanent adoption whenever practical.
