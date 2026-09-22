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

## Pre-pivotal opportunity watch

Radar must not wait for Phase 3 success before recognizing a potentially asymmetric clinical opportunity.

Use a **Pre-Pivotal Opportunity Watch** for public companies where late Phase 2 / Phase 2b evidence, regulatory alignment, pivotal design, enrollment execution, supportive de-risking catalysts, class read-through, commercial differentiation, manufacturing, or financing evidence may change the probability distribution **before** the pivotal readout.

Track the evidence ladder:

1. **Early clinical signal** — effect size, dose response, durability, safety, subgroup consistency, and biological plausibility.
2. **Pivotal translatability** — whether Phase 3 population, dose, endpoint, comparator, duration and statistical design preserve the thesis tested earlier.
3. **Regulatory alignment** — disclosed agency feedback, endpoint acceptance, trial design agreement, filing path, or unresolved regulatory risk.
4. **Execution** — trial start, site activation, enrollment velocity/completion, retention, protocol changes, CMC/manufacturing readiness.
5. **Supporting de-risking catalysts** — longer follow-up, maintenance dosing, oral/formulation data, subgroup evidence, competitor/class read-through, safety updates, biomarker evidence, commercial preparation.
6. **Financing/runway** — whether the company can reach the pivotal readout and potential filing without value-destructive financing.
7. **Differentiation / commercial bridge** — convenience, durability, efficacy, safety, dosing, manufacturing, payer or adoption characteristics that could matter even before pivotal proof.
8. **Expectations / valuation question** — whether current price and narrative already appear to assume pivotal success or still leave an asymmetric probability gap.

Do not assign a final approval probability or security value inside Radar. The point is to identify when enough pieces of the ladder have strengthened to justify **pre-readout RWC and possibly pre-readout Full Underwriting**.

Use these plain research states:

- **PRE-PIVOTAL — WATCH** — scientifically interesting, but too many load-bearing unknowns remain.
- **PRE-PIVOTAL — EVIDENCE BUILDING** — multiple independent de-risking observations are accumulating; preserve the sequence and next evidence.
- **PRE-PIVOTAL — RWC NOW** — the clinical/translational setup is sufficiently developed that independent clinical, regulatory, commercial and expectations analysis is warranted before the pivotal result.
- **PRE-PIVOTAL — POSITIONING REVIEW** — RWC has already established enough support that Full Underwriting / Portfolio Capital Allocation should assess whether a deliberately small speculative position is justified before the readout.

PRE-PIVOTAL — POSITIONING REVIEW is not a BUY instruction. Radar may only use it when a current downstream RWC/underwriting handoff actually supports that status.

A large stock move after an intermediate catalyst is not itself evidence that the pre-pivotal case was valid; compare the underlying clinical/regulatory/commercial delta with the frozen baseline.

### Front-running the pivotal result without front-running the evidence

The intended process is:

`Phase 2 / de-risking evidence -> regulatory/pivotal design check -> execution/supporting catalysts -> RWC -> probability-weighted pre-pivotal underwriting -> loss-budgeted speculative starter when justified -> pivotal readout`

Do not require Phase 3 efficacy data before RWC or Full Underwriting if the remaining uncertainty can be modeled honestly. Do not bypass RWC merely because the upside could be large.

For each serious pre-pivotal candidate, persist or retain:

```text
pre_pivotal_status
phase_2_or_prior_evidence
pivotal_trial_id
pivotal_design_match
regulatory_alignment_status
enrollment_execution_status
supporting_derisking_catalysts
class_or_competitor_readthrough
cash_runway_to_readout
financing_risk
commercial_differentiation_hypothesis
expected_pivotal_window
next_pre_pivotal_evidence
next_pre_pivotal_evidence_date
rwc_question
```

Use supported schema fields where available; keep unsupported enrichment in the existing manifest/fallback rather than inventing API fields.

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
pre_pivotal_status
pivotal_design_match
regulatory_alignment_status
enrollment_execution_status
cash_runway_to_readout
expected_pivotal_window
next_pre_pivotal_evidence
next_pre_pivotal_evidence_date
```

## Routing

Use `P0` for clinical holds, deaths, material safety signals, regulator rejection, financing or runway risk, manufacturing shutdown, or another development that can permanently impair an existing holding.

Use `P1` when a result or decision is plausibly practice-changing, economically material, and not already fully anticipated, but still requires independent clinical and security analysis. Also use `P1` for **PRE-PIVOTAL — RWC NOW** when cumulative Phase 2/translational, regulatory, pivotal-design, execution, supporting-catalyst and financing evidence creates a credible pre-readout probability/expectations question.

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
