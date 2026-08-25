# Event Ledger Schema

Use one canonical record for each underlying event. Articles, posts, analyst notes, and follow-up coverage that share the same origin attach to the same record.

## Required fields

```text
event_id
first_seen_at
last_updated_at
scan_window
underlying_event_at
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
candidate_map
five_gates
primary_route
next_required_evidence
next_evidence_date
confidence
resolution_status
resolution_notes
```

Use ISO-8601 timestamps and explicit time zones. Do not overwrite `first_seen_at` when an event is updated.

## Delta classes

Assign exactly one primary class:

- `GENUINELY_NEW` — a new fact, decision, datapoint, contract, result, filing, channel observation, or quantified change not present in the prior baseline.
- `REPEATED_GUIDANCE` — substantially the same claim or target was previously disclosed; no independent new evidence.
- `INDEPENDENT_CONFIRMATION` — a genuinely separate source or dataset confirms a previously uncertain claim.
- `ACCELERATION` — the mechanism, adoption, orders, pricing, enrollment, capacity, or impact is advancing faster or further than the prior baseline.
- `DECELERATION` — the same variables are advancing slower or reversing.
- `CONTRADICTION` — credible evidence conflicts with the baseline, company claim, or prevailing interpretation.
- `RISK_DISCLOSURE` — a new downside, liability, financing, safety, regulatory, legal, or execution risk becomes visible.
- `UNKNOWN` — the prior baseline or source origin has not yet been resolved.

A press release date alone does not make the content `GENUINELY_NEW`. Compare the underlying claim with prior filings, guidance, presentations, trial records, and earlier reporting.

## Thesis effects

Assign exactly one primary effect for the affected thesis or security:

- `INTRINSIC_VALUE_CHANGE` — expected cash flows, asset value, capital structure, dilution, or terminal economics change.
- `PROBABILITY_CHANGE` — the probability of a material outcome changes, while the payoff if it occurs is broadly unchanged.
- `TIMING_CHANGE` — value realization, cash flow, approval, launch, construction, or another milestone moves earlier or later.
- `CONFIDENCE_ONLY` — independent evidence strengthens or weakens confidence without changing the modeled central case yet.
- `MONITOR_ONLY` — informative context or a future checkpoint; no current decision change.
- `NO_CHANGE` — repeated, immaterial, already incorporated, or otherwise does not alter the thesis.

The same event may affect different theses differently. Record a primary effect and note secondary effects rather than creating duplicate events.

## Candidate map

For each serious event, record:

```text
direct_issuer
obvious_beneficiaries
second_order_beneficiaries
non_beneficiary_or_false_friend
potential_losers
comparators
existing_holdings_or_derivatives
```

Do not promote a company merely because it appears in the same theme. State the ownership, contract, unit, margin, royalty, asset, financing, or probability path through which value is captured.

## Five-gate object

```text
novelty: PASS | FAIL | UNKNOWN
materiality: PASS | FAIL | UNKNOWN
capture: PASS | FAIL | UNKNOWN
expectation: PASS | FAIL | UNKNOWN
researchability: PASS | FAIL | UNKNOWN
```

Include one sentence of evidence for each gate. Do not total the gates into a composite score.

## Deduplication rules

Treat items as one event when they share the same underlying fact, even if:

- headlines differ;
- the article is republished in another region;
- an aggregator cites a newswire;
- several outlets quote the same anonymous source;
- social posts repeat a company release;
- a scheduled scan rediscovers the event.

Create a new event only when there is a new factual delta, independent confirmation, contradiction, acceleration/deceleration, or risk disclosure.

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

Never delete rejected events from the calibration record. Preserve what was known, the original confidence, route, and price context at the time.
