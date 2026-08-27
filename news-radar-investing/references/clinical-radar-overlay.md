# Clinical and Medical Radar Overlay — V3

Use this overlay for broad medical research, cancer trials, clinical results, regulator actions, safety signals, partnerships, reimbursement, manufacturing developments, and changes visible only in registry or protocol history.

Radar detects, compares, persists, and routes. Detailed clinical validity, causality, commercial translation, financing, valuation, and security analysis belong in Research With Confidence and Full Underwriting.

## Event categories

Record the most specific category:

- trial initiation, enrollment, protocol, site, endpoint, or completion-date change;
- interim or final efficacy readout;
- safety signal, clinical hold, death imbalance, or discontinuation;
- peer-reviewed publication or conference abstract;
- regulatory submission, acceptance, advisory committee, approval, rejection, delay, or label change;
- reimbursement, guideline, formulary, payer, or standard-of-care change;
- companion-diagnostic or biomarker-testing development;
- licensing, partnership, milestone, royalty, or acquisition;
- manufacturing, supply, inspection, CMC, or quality issue;
- competitor readout with meaningful class, endpoint, safety, or market read-through;
- expected clinical or regulatory evidence that becomes overdue or disappears.

## Primary baseline sources

Prefer the actual:

- trial registry record and version history;
- regulator document, label, review, calendar, or safety communication;
- protocol, statistical-analysis plan, peer-reviewed paper, or conference abstract;
- company filing and contractual economics;
- guideline, reimbursement, formulary, or payer decision;
- partner disclosure for rights, royalties, milestones, launch, manufacturing, or financing.

Sponsor releases are primary evidence of sponsor claims. Verify endpoints, populations, denominators, follow-up, statistical maturity, adverse events, discontinuations, label scope, and commercial rights from original materials when available.

## Registry and protocol version-diff rule

For relevant holdings, active underwritings, catalysts, and cancer-thesis watchlist programs, compare the current record with the archived baseline when available.

Flag changes to:

- enrollment target;
- actual or planned site count;
- arms, comparator, randomization, or eligibility;
- primary and secondary endpoints;
- primary-completion and study-completion dates;
- status, suspension, termination, withdrawal, or sponsor;
- biomarker and line-of-therapy definitions;
- statistical plan or follow-up requirements.

A registry change is evidence that the record changed. It is not automatic proof of success, failure, fraud, or regulator concern. Record the exact version delta, sponsor versus regulator origin, and strongest benign explanation.

## Evidence-due rule

At every scheduled run, check clinical and regulatory items whose readout or decision window has arrived.

Use the V3 observation types when:

- a readout, abstract, registry update, filing, advisory document, or regulator decision does not arrive;
- the completion or decision date moves;
- a previously disclosed endpoint, subgroup, safety table, or launch plan disappears;
- management repeatedly references progress without the promised observable evidence.

Preserve the original due date and frozen catalyst packet. Do not silently roll the date forward or automatically change a thesis probability.

## Radar fields

Add:

```text
trial_id_or_regulatory_id
registry_version_or_document_date
phase
indication_and_line_of_therapy
population_and_biomarker
intervention_and_comparator
primary_endpoint
readout_or_decision_date
expected_evidence_status
observation_type
detection_status
clinical_delta
safety_delta
regulatory_delta
commercial_rights
known_milestones_or_royalties
runway_or_financing_alert
pre_event_expectation_packet_status
```

## Routing

Use `P0` for clinical holds, deaths, material safety signals, regulator rejection, financing or runway risk, manufacturing shutdown, or another development that can permanently impair an existing holding.

Use `P1` when a result or decision is plausibly practice-changing, economically material, and not already fully anticipated, but still requires independent clinical and security analysis.

Use `P2` when the headline or registry delta lacks a protocol, subgroup denominator, hazard ratio or confidence interval, safety table, label detail, contractual economics, sponsor explanation, or another named decisive item.

Use `P3` for scientifically interesting developments with weak public-security materiality or long, unobservable translation paths.

A late-discovered clinical event must be backfilled as `LATE_DETECTION` and routed normally. A large stock reaction does not substitute for the missing clinical evidence.

## Hard depth boundary

Radar may state:

- what changed versus the archived baseline;
- source and claim status;
- population, endpoint, safety, rights, and timing fields needed to identify the issue;
- plausible materiality;
- affected holding, thesis, or candidate;
- decisive missing documents and RWC questions.

Radar should not complete:

- detailed statistical or clinical-validity analysis;
- cross-trial comparability and standard-of-care underwriting;
- commercial patient, pricing, reimbursement, uptake, or market-share modeling;
- milestone, royalty, financing, dilution, or fully diluted valuation;
- an approval probability, price target, or investability decision.

Do not infer investability from statistical significance, an FDA approval, a milestone payment, a large addressable population, or a dramatic price move alone.
