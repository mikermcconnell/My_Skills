# Audit Schema and Metrics

## Original-decision snapshot

Preserve at the time of the decision:

```text
event_id
first_seen_at
underlying_event_at
source_origin
independence_group
prior_baseline
delta_class
thesis_effect
five_gates
original_route
original_confidence_by_claim
security_map
original_price_and_market_status
rwc_outcome
underwriting_posture
scenario_probabilities_and_values
expected_return_and_horizon
hurdle_and_alternative
challenge_status
next_evidence_and_date
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
thesis_status_change
fundamental_metric_outcome
price_outcomes
benchmark_outcomes
maximum_favourable_excursion
maximum_adverse_excursion
research_effort
post_mortem_category
notes
```

## Core metrics

### Capture rate

```text
material events detected / material events in the predefined auditable universe
```

The denominator must be defined independently of Radar output, such as all qualifying regulatory decisions, index constituents' material filings, or a curated ex-post event set using rules fixed before outcome review.

### Capture latency

Measure from the original public source timestamp to `first_seen_at`. Report median, percentiles, and late-tail cases rather than only an average.

### Novelty precision

```text
genuinely incremental events labelled new / all events labelled GENUINELY_NEW
```

### P1 precision

```text
P1 leads that survive RWC / all completed P1 RWC investigations
```

Interpret with P1 recall and research effort. High recall systems may rationally accept lower precision.

### Underwriting yield

```text
RWC advances ending INVESTABLE or PRICE-SENSITIVE / completed RWC advances
```

Also report WATCH, PASS, REJECT, and unresolved counts.

### Confidence calibration

When numeric probabilities exist, use Brier score or log loss by comparable claim class. For categorical confidence, report observed resolution ranges and confidence intervals when feasible.

Do not pool factual-event confidence with security-mispricing confidence.

## Outcome windows

Use windows appropriate to the stated thesis. A default diagnostic panel may include:

- 1 trading day;
- 5 trading days;
- 20 trading days;
- 60 trading days;
- 120 trading days;
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

Judge soundness using information available at the time, not later knowledge.

## Minimum evidence for a process change

There is no universal sample threshold. Require enough independent cases to make the failure pattern credible. State:

- number of events;
- number of independent origins;
- category and regime concentration;
- uncertainty around the metric;
- forward-test design.

Changes affecting recall, routing, or source coverage should be forward-tested before permanent adoption whenever practical.
