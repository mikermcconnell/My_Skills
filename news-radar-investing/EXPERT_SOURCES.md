# Expert and Industry Source Lane — V3

Monitor high-signal experts and industry publications that may surface important claims before they appear in conventional financial news. Expert sources improve discovery and interpretation; they are not automatic proof.

V3 organizes expert monitoring around active holdings, underwritings, and theses rather than the popularity of the source.

## Thesis-specific expert map

Maintain a compact source map for each material active thesis or sector:

```text
thesis_or_sector
named_source
source_type: TECHNICAL | PRACTITIONER | CHANNEL | CLINICAL | POLICY | LEGAL | DATA
primary_topics
known_information_or_analytical_edge
known_biases_or_incentives
usual_primary_documents_for_verification
last_checked_at
last_unique_origin_event_at
unique_origin_yield
RWC_survival_history_when_available
```

Prefer two or three differentiated sources per important thesis over a large influencer list. Remove or demote a source only after checking whether another feed captures the same valuable events with comparable latency.

## SemiAnalysis / Dylan Patel

Treat SemiAnalysis and Dylan Patel as priority discovery sources for:

- AI accelerators, GPUs, custom ASICs, and inference or training economics;
- datacenter architecture, networking, optics, memory, storage, power, and cooling;
- semiconductor manufacturing, packaging, foundry capacity, equipment, and supply chains;
- hyperscaler and AI-lab capex, utilization, deployment cadence, and unit economics;
- bottlenecks, vendor share shifts, product roadmaps, and second-order beneficiaries.

Look for genuinely new material from articles, notes, posts, podcasts, interviews, conference appearances, and contributor commentary.

## Event Ledger treatment

For every expert-source lead record:

1. what was newly said and when;
2. the prior baseline;
3. `delta_class`, `thesis_effect`, and `detection_status`;
4. source origin `NAMED_INDUSTRY_EXPERT`;
5. claim status: fact, channel check, estimate, forecast, derived calculation, or judgment;
6. the expert item's independence group;
7. the direct holding, underwriting, thesis, or candidate affected;
8. preliminary mechanism and main capture uncertainty;
9. what requires independent verification;
10. Radar route, RWC questions, and next evidence.

Reject recycled commentary. A new podcast clip that repeats an earlier published estimate is `REPEATED_GUIDANCE`, not a new event.

If an expert item predates the current scan window but was missed and has no canonical record, backfill it as `LATE_DETECTION` rather than calling the later discovery new.

## Evidence rules

- Separate expert analysis, estimates, channel checks, and opinions from confirmed facts.
- Trace material factual claims to filings, counterparties, suppliers, customers, contracts, official data, or other independent evidence when possible.
- Do not downgrade a useful lead merely because it first appears in a podcast or post. Route it when the source may have an informational or analytical edge and the mechanism is plausible.
- Identify whether the edge is new information, expert interpretation, channel knowledge, technical synthesis, or a non-obvious cross-company mapping.
- When the expert claim conflicts with guidance or consensus, route the disagreement to Research With Confidence rather than resolving it superficially in Radar.
- Group media articles repeating the expert under the same independence origin.
- Do not count access to a closed or paywalled source unless the item was actually retrieved. Declare the feed unavailable when appropriate.

## V3 depth boundary

Radar may state the expert's exact incremental claim, prior baseline, preliminary mechanism, affected exposure, strongest failure reason, and decisive verification questions.

Radar should not reproduce a full expert thesis, complete its causal analysis, calculate detailed security sensitivities, estimate valuation, or choose the best investment expression. Research With Confidence must independently determine whether the claim and mapping survive.

## RWC handoff

A P1 expert-source handoff should distinguish:

- directionally plausible claim versus exact numerical claim;
- known numerator and missing denominator;
- source-provided estimate versus independently reproduced calculation;
- direct exposure versus preliminary second-order mapping;
- the strongest source incentive or methodological weakness;
- what observation could falsify the expert's interpretation.

Expert monitoring supplements primary-source, clinical, macro, regulatory, commodity, social-arbitrage, and company-specific scanning. It does not replace them.
