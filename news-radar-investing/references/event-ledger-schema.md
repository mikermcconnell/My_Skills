# Event Ledger Schema — V3

Use one canonical record for each underlying event or cumulative evidence pattern. Articles, posts, analyst notes, and follow-up coverage that share the same origin attach to the same record.

The Event Ledger is research memory. It is not a portfolio ledger, valuation model, or automatic thesis-change mechanism.

## Required fields

```text
schema_version: 3
event_id
observation_type
detection_status
first_seen_at
last_updated_at
scan_window
underlying_event_at
original_publication_at
detection_latency
missed_feed_reason
original_source_url
source_origin
claim_status
independence_group
issuer_or_entity
securities
exchange_and_currency
event_category
prior_baseline
baseline_source
baseline_as_of
delta_class
thesis_effect
preliminary_mechanism
measurable_metric
materiality_hypothesis
market_status_at_release
price_volume_context
linked_theses
linked_holdings
linked_underwritings
portfolio_cluster
exposure_links
five_gates
primary_route
next_required_evidence
next_evidence_date
expected_evidence_status
confidence
resolution_status
resolution_notes
```

Use ISO-8601 timestamps and explicit time zones. Do not overwrite `first_seen_at`, `original_publication_at`, the original route, or the original confidence when an event is updated.

## Observation types

Assign one primary `observation_type`:

- `EVENT` — a discrete filing, decision, result, contract, announcement, datapoint, or observable development.
- `ATOMIC_SLOW_BURN` — one comparable observation appended to a durable cumulative pattern.
- `EXPECTED_EVIDENCE_MISSED` — promised or scheduled evidence did not arrive within the defined window.
- `DISCLOSURE_REMOVED` — a previously material KPI, table, segment, risk item, or management discussion disappeared or was materially reduced.
- `MILESTONE_DELAYED` — a dated operating, clinical, regulatory, legal, financing, construction, or commercial milestone moved later.
- `PROMISE_UNCONFIRMED` — repeated guidance remained unsupported beyond the date when observable proof was expected.
- `PRICE_DISLOCATION_UNEXPLAINED` — unusual price action triggered investigation but no underlying new event has yet been established.

These observation types describe the evidence state. They do not by themselves determine whether the thesis effect is positive or negative.

## Detection status

Assign one primary `detection_status`:

- `ON_TIME` — detected within the intended scheduled scan window.
- `LATE_DETECTION` — the original event predates the current scan window and no matching canonical record existed.
- `FOLLOW_UP` — later information updates an existing event with a factual delta or useful confirmation.
- `DUPLICATE` — dependent or repeated coverage adds no new evidentiary observation.
- `EXPECTED_EVIDENCE_MISSED`
- `DISCLOSURE_REMOVED`
- `MILESTONE_DELAYED`
- `PROMISE_UNCONFIRMED`
- `PRICE_DISLOCATION_UNEXPLAINED`

For `LATE_DETECTION`, preserve:

```text
original_publication_at
first_seen_at
detection_latency
missed_feed_reason
whether_decision_usefulness_was_reduced
```

A late-detected material event must still be classified and routed normally.

## Delta classes

Assign exactly one primary class:

- `GENUINELY_NEW` — a new fact, decision, datapoint, contract, result, filing, channel observation, quantified change, or changed evidence state not present in the prior baseline.
- `REPEATED_GUIDANCE` — substantially the same claim or target was previously disclosed; no independent new evidence.
- `INDEPENDENT_CONFIRMATION` — a genuinely separate source or dataset confirms a previously uncertain claim.
- `ACCELERATION` — adoption, orders, pricing, enrollment, capacity, mechanism, or impact is advancing faster or further than the prior baseline.
- `DECELERATION` — the same variables are advancing slower or reversing.
- `CONTRADICTION` — credible evidence conflicts with the baseline, company claim, or prevailing interpretation.
- `RISK_DISCLOSURE` — a new downside, liability, financing, safety, regulatory, legal, governance, accounting, or execution risk becomes visible.
- `UNKNOWN` — the prior baseline, source origin, or underlying event has not yet been resolved.

A press release date alone does not make content `GENUINELY_NEW`. Compare the underlying claim with prior filings, guidance, presentations, trial records, monitor snapshots, and earlier reporting.

A missing item can be `TIMING_CHANGE`, `RISK_DISCLOSURE`, `CONTRADICTION`, or `UNKNOWN` depending on what the absence actually implies. Do not automatically treat absence as failure.

## Thesis effects

Assign exactly one primary effect for the affected thesis or security:

- `INTRINSIC_VALUE_CHANGE` — expected cash flows, asset value, capital structure, dilution, or terminal economics change.
- `PROBABILITY_CHANGE` — the probability of a material outcome changes while the payoff if it occurs is broadly unchanged.
- `TIMING_CHANGE` — value realization, cash flow, approval, launch, construction, financing, or another milestone moves earlier or later.
- `CONFIDENCE_ONLY` — independent evidence strengthens or weakens confidence without changing the modeled central case yet.
- `MONITOR_ONLY` — informative context or a future checkpoint; no current decision change.
- `NO_CHANGE` — repeated, immaterial, already incorporated, or otherwise does not alter the thesis.

The same event may affect different theses differently. Preserve one canonical event and record the preliminary exposure links rather than creating duplicate events.

## Exposure links

Radar records only enough mapping to route the event correctly:

```text
exposure_links:
  - security_or_thesis
  - exposure_type: DIRECT | DERIVATIVE | READ_THROUGH | NONE_IDENTIFIED
  - preliminary_mechanism
  - main_capture_uncertainty
  - direction: POSITIVE | NEGATIVE | MIXED | UNKNOWN
```

This is not a complete value-capture or earnings-sensitivity model. Research With Confidence owns the deeper economic map.

For P1 industry, policy, bottleneck, or class-level events, also record when useful:

```text
obvious_beneficiary
second_order_candidate
non_beneficiary_or_false_friend
potential_loser_or_comparator
```

Do not require these fields before routing a time-sensitive P0 risk.

## Five-gate object

```text
novelty: PASS | FAIL | UNKNOWN
materiality: PASS | FAIL | UNKNOWN
capture: PASS | FAIL | UNKNOWN
expectation: PASS | FAIL | UNKNOWN
researchability: PASS | FAIL | UNKNOWN
```

Include one sentence of evidence for each gate. Do not total the gates into a composite score.

Price movement alone cannot support a Novelty pass. An overdue evidence item can pass Novelty when the changed evidence state is itself genuinely new, but Radar must leave the interpretation open when the implication is uncertain.

## Expected-evidence status

Use when a dated document, result, decision, or proof item matters:

- `NOT_APPLICABLE`
- `NOT_DUE`
- `DUE_TODAY`
- `OVERDUE`
- `ARRIVED_AS_EXPECTED`
- `ARRIVED_WITH_DELTA`
- `DELAY_CONFIRMED`
- `WINDOW_UNKNOWN`

Do not silently roll an overdue date forward. Append the status change and identify the next resolving evidence.

## Deduplication rules

Treat items as one event when they share the same underlying fact, even if:

- headlines differ;
- the article is republished in another region;
- an aggregator cites a newswire;
- several outlets quote the same anonymous source;
- social posts repeat a company release;
- a scheduled scan rediscovers the event;
- a later article describes an event that Radar missed earlier.

For a missed earlier event, update the canonical record as `LATE_DETECTION`; do not create a false new event dated to the later article.

Create a new event only when there is a new factual delta, independent confirmation, contradiction, acceleration or deceleration, risk disclosure, changed evidence state, or separate underlying event.

## Resolution status

Use:

- `OPEN`
- `ROUTED_RWC`
- `WAITING_EVIDENCE`
- `MONITORING`
- `ADVANCED_UNDERWRITING`
- `REJECTED`
- `RESOLVED_CORRECT`
- `RESOLVED_INCORRECT`
- `RESOLVED_MIXED`

Never delete rejected, duplicate, late-detected, or missed-evidence records from the calibration history. Preserve what was known, the original confidence, route, source coverage, price context, and decision usefulness at the time.
