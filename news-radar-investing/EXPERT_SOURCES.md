# Expert and Industry Source Lane — V3

Monitor high-signal experts, senior industry operators, frontier-lab executives, and industry publications that may surface important claims before they appear in conventional financial news. Expert sources improve discovery and interpretation; they are not automatic proof.

V3 organizes expert monitoring around active holdings, underwritings, and theses rather than the popularity of the source.

## Thesis-specific expert map

Maintain a compact source map for each material active thesis or sector:

```text
thesis_or_sector
named_source
source_type: TECHNICAL | PRACTITIONER | CHANNEL | CLINICAL | POLICY | LEGAL | DATA | FRONTIER_LAB_EXECUTIVE
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

## Frontier AI lab executives and research leaders

Treat the current CEOs, founders, senior executives, chief scientists/research leaders, infrastructure leaders, and major product/model leaders at frontier AI labs as priority industry sources. At minimum, every scheduled Expert / Industry Sources lane should consider relevant attributable commentary from:

- **OpenAI**;
- **Anthropic**;
- **Google / Google DeepMind**;
- **Meta / Meta AI**.

Dynamically resolve the relevant current people and roles at run time rather than relying on a permanently static name list. Extend coverage to other frontier labs when they become material to an active holding, underwriting, thesis, catalyst, or industry question.

Monitor genuinely new attributable statements from:

- official company or personal posts;
- interviews and podcasts;
- conference, developer-event, and industry-event appearances;
- earnings-call or investor-event remarks when applicable;
- testimony, regulatory or policy appearances;
- research/product launch commentary;
- technical blogs, papers, model cards, system cards, and infrastructure disclosures where the executive or research leader is directly attributable.

Prioritize comments that may change an investable causal chain, including:

- training or inference scaling, compute demand, utilization, and bottlenecks;
- accelerator, custom-silicon, networking, memory, power, datacenter, and supplier requirements;
- model capability, reliability, cost curves, context length, multimodality, agents, reasoning, and deployment cadence;
- product adoption, enterprise demand, developer usage, consumer engagement, pricing, monetization, and willingness to pay;
- capex intensity, model-training budgets, inference economics, gross-margin pressure, and the path to sustainable unit economics;
- partnerships, cloud relationships, model distribution, exclusivity, capacity reservations, and vendor concentration;
- open-source/open-weight strategy, licensing, ecosystem strategy, and competitive differentiation;
- safety, regulation, export controls, security, energy constraints, or other factors that could delay or reshape deployment;
- competitive claims about other frontier labs when they create a testable cross-company read-through.

Treat these executives as **primary evidence of what their organization is saying, planning, observing, or claiming**, not independent proof that the claim is economically correct. Management incentives, competitive positioning, fundraising/capital needs, product promotion, policy advocacy, and selective disclosure can all bias the statement.

For a material frontier-lab executive observation:

1. preserve the exact attributable speaker, role, source, publication/event time, and original context;
2. identify what is genuinely incremental versus prior public guidance or repeated talking points;
3. map the statement to the affected public-company holding, underwriting, thesis, causal pillar, forecast, supplier/customer relationship, or valuation input;
4. distinguish direct observation from aspiration, forecast, marketing claim, policy argument, or competitive positioning;
5. seek independent corroboration from counterparties, filings, technical evidence, customer/developer behavior, supplier data, or other differentiated sources when the claim is decision-relevant;
6. route unresolved causality, value capture, magnitude, and priced-in questions to Research With Confidence;
7. do not convert a frontier-lab executive statement directly into a security action, thesis approval, fair-value change, or monitor change.

## Event Ledger treatment

For every expert-source lead record:

1. what was newly said and when;
2. the prior baseline;
3. `delta_class`, `thesis_effect`, and `detection_status`;
4. source origin `NAMED_INDUSTRY_EXPERT` or `FRONTIER_LAB_EXECUTIVE` as applicable;
5. claim status: fact, channel check, estimate, forecast, derived calculation, management/industry observation, or judgment;
6. the expert item's independence group;
7. the direct holding, underwriting, thesis, or candidate affected;
8. preliminary mechanism and main capture uncertainty;
9. what requires independent verification;
10. Radar route, RWC questions, and next evidence.

Reject recycled commentary. A new podcast clip that repeats an earlier published estimate or executive talking point is `REPEATED_GUIDANCE`, not a new event.

If an expert item predates the current scan window but was missed and has no canonical record, backfill it as `LATE_DETECTION` rather than calling the later discovery new.

## Evidence rules

- Separate expert analysis, estimates, channel checks, executive/management claims, and opinions from confirmed facts.
- Trace material factual claims to filings, counterparties, suppliers, customers, contracts, official data, technical artifacts, or other independent evidence when possible.
- Do not downgrade a useful lead merely because it first appears in a podcast, post, interview, or executive appearance. Route it when the source may have an informational or analytical edge and the mechanism is plausible.
- Identify whether the edge is new information, expert interpretation, channel knowledge, technical synthesis, direct operator knowledge, management guidance, or a non-obvious cross-company mapping.
- When the expert or executive claim conflicts with guidance, consensus, another frontier lab, or observable evidence, route the disagreement to Research With Confidence rather than resolving it superficially in Radar.
- Group media articles repeating the same expert or executive statement under the same independence origin.
- Do not count access to a closed or paywalled source unless the item was actually retrieved. Declare the feed unavailable when appropriate.

## V3 depth boundary

Radar may state the expert's or executive's exact incremental claim, prior baseline, preliminary mechanism, affected exposure, strongest failure reason, and decisive verification questions.

Radar should not reproduce a full expert thesis, complete its causal analysis, calculate detailed security sensitivities, estimate valuation, or choose the best investment expression. Research With Confidence must independently determine whether the claim and mapping survive.

## RWC handoff

A P1 expert-source handoff should distinguish:

- directionally plausible claim versus exact numerical claim;
- known numerator and missing denominator;
- source-provided estimate versus independently reproduced calculation;
- direct exposure versus preliminary second-order mapping;
- the strongest source incentive, management bias, or methodological weakness;
- what observation could falsify the expert's or executive's interpretation.

Expert monitoring supplements primary-source, clinical, macro, regulatory, commodity, social-arbitrage, and company-specific scanning. It does not replace them.
