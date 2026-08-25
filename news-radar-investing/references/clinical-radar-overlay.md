# Clinical and Medical Radar Overlay

Use this overlay for broad medical research, cancer trials, clinical results, FDA or other regulator actions, safety signals, partnerships, reimbursement, or manufacturing developments.

Radar detects and routes. Detailed clinical, regulatory, commercial, and security analysis belongs in Research With Confidence.

## Event categories

Record the most specific category:

- trial initiation, enrollment, protocol, or endpoint change;
- interim or final efficacy readout;
- safety signal, clinical hold, or discontinuation;
- peer-reviewed publication or conference abstract;
- regulatory submission, acceptance, advisory committee, approval, rejection, or label change;
- reimbursement, guideline, or standard-of-care change;
- licensing, partnership, milestone, royalty, or acquisition;
- manufacturing, supply, inspection, or quality issue;
- competitor readout with a meaningful class or market read-through.

## Primary baseline sources

Prefer the actual:

- trial registry record and version history;
- regulator document, label, review, or safety communication;
- protocol, statistical analysis plan, peer-reviewed paper, or conference abstract;
- company filing and contractual economics;
- guideline, reimbursement, or payer decision.

Sponsor releases are primary evidence of sponsor claims. Verify endpoints, populations, denominators, follow-up, statistical maturity, adverse events, discontinuations, and label scope from original materials when available.

## Radar fields

Add:

```text
trial_id_or_regulatory_id
phase
indication_and_line_of_therapy
population_and_biomarker
intervention_and_comparator
primary_endpoint
readout_or_decision_date
clinical_delta
safety_delta
regulatory_delta
commercial_rights
known_milestones_or_royalties
pre_event_expectation_packet_status
```

## Routing

Use `P0` for clinical holds, deaths, material safety signals, regulator rejection, financing/runway risk, or other developments that can permanently impair an existing holding.

Use `P1` when a result or decision is plausibly practice-changing, economically material, and not already fully anticipated, but still requires independent clinical and security analysis.

Use `P2` when the headline lacks a protocol, subgroup denominator, hazard ratio/confidence interval, safety table, label detail, contractual economics, or another named decisive item.

Use `P3` for scientifically interesting developments with weak public-security materiality or long, unobservable translation paths.

Do not infer investability from statistical significance, an FDA approval, a milestone payment, or a large addressable population alone.
