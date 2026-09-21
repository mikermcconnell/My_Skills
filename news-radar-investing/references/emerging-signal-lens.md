# Emerging Signal / Leading Indicator Lens — News Radar V3

Approved September 21, 2026. This is a **global research lens**, not a twelfth specialist lane, separate task, scoring model, or investment strategy.

Its purpose is to catch opportunities and risks that rhyme across companies and sectors:

> observable real-world change -> unusual acceleration or deterioration -> independent/persistent evidence -> plausible financial transmission -> possible expectations lag.

Radar uses this lens during protected broad discovery and the existing Social / Alternative Data lane. It identifies research-worthy trajectories before they are fully visible in reported financials. RWC verifies causality, materiality, value capture and expectations. Underwriting values the security only after that work warrants it.

## What this lens is for

Use it when a development may be a **leading indicator** rather than a completed financial result. Examples include changes in consumer adoption; developer usage; customer orders/bookings; traffic/search; inventory/availability; pricing/mix; physician uptake; hiring/headcount mix; supplier/customer deployments; utilization/capacity/lead times; competitive switching; service quality; operating efficiency; or repeated management promises becoming externally measurable.

Do not restrict this lens to consumer apps, social media, AI, current holdings, familiar tickers, or positive signals. The negative mirror image—deceleration, cancellations, worsening availability, falling utilization, rising costs, competitive loss or deteriorating service—is equally relevant.

## Pattern library

Classify a promising observation into one or more broad archetypes. These are descriptors, not scoring buckets and not independent events:

1. **ADOPTION_ACCELERATION** — users/customers/developers/physicians/partners adopt faster than the prior baseline.
2. **DEMAND_INFLECTION** — orders, bookings, traffic, searches, reservations, inventory turns or usage change materially.
3. **PRICING_POWER_OR_WEAKNESS** — price/mix changes without expected demand destruction, or discounting/elasticity worsens.
4. **CAPACITY_OR_BOTTLENECK_SHIFT** — utilization, lead time, supply availability, capacity additions or bottleneck location changes.
5. **OPERATING_LEVERAGE_OR_DELEVERAGE** — output/revenue/service volume changes faster than labor, support, capex or other inputs.
6. **DISTRIBUTION_ADVANTAGE_OR_FAILURE** — equivalent products/technology convert very differently because of channel, installed base, identity, workflow or ecosystem reach.
7. **COMPETITIVE_DISPLACEMENT** — observable switching, share loss/gain, migration, churn or supplier substitution.
8. **BEHAVIOR_TO_FINANCIAL_CONVERSION** — a prior behavioral/operating signal begins appearing in reported KPIs, guidance, revenue, margins or cash flow.
9. **NARRATIVE_EVIDENCE_DIVERGENCE** — observable evidence changes while consensus, guidance or dominant narrative appears stale or disputed.
10. **PROMISE_TO_MEASUREMENT** — repeated company claims become externally measurable, corroborated or falsified.

A single observation may fit several archetypes. Do not multiply event counts because multiple archetypes apply.

## Emerging Signal Test

For every credible material observation from broad discovery or alternative data, ask:

1. **Magnitude** — is the change large versus its own prior baseline or normal variation?
2. **Velocity** — is it accelerating/decelerating, rather than merely existing?
3. **Persistence** — does it survive beyond a one-off launch, promotion, outage, squeeze or viral spike?
4. **Breadth** — is it spreading across cohorts, geographies, channels, customers, products or independent datasets?
5. **Independence** — are confirmations genuinely independent rather than copies of one source?
6. **Business bridge** — is there a plausible path to units, price, share, revenue, margin, cash flow, capital needs, strategic advantage or permanent-loss risk?
7. **Expectations lag** — is there a plausible reason guidance, consensus, positioning or prevailing narrative may not yet reflect the change?
8. **Testability** — can Radar name the next observable fact that would confirm, weaken or kill the hypothesis?

Do **not** create a numeric score or fixed pass count. The purpose is disciplined pattern recognition, not quota-driven idea generation.

"Not yet revenue" is not a rejection when the signal is credibly upstream of revenue and has a plausible business bridge. Equally, attention/downloads/traffic alone are not proof of durable economics.

## Signal Sequences — trajectory memory

The main unit of learning is often a **sequence**, not one headline.

When a credible observation may develop over time, persist or reuse a stable `signal_sequence_id` / parent hypothesis in supported storage. If the canonical schema does not support these fields, keep them in the existing manifest or verified fallback rather than inventing an API payload.

A sequence should retain, where supported:

```text
signal_sequence_id
parent_hypothesis
linked_security_or_unresolved_mapping
archetypes
direction: POSITIVE | NEGATIVE | MIXED
first_seen_at
last_updated_at
baseline_observation
evidence_ids_and_independence_groups
trajectory_summary
magnitude_state
velocity_state
persistence_state
breadth_state
business_bridge
expectations_question
main_counter_hypothesis
next_confirmation_or_falsifier
next_evidence_date
current_route
sequence_status: WATCH | BUILDING | ESCALATE | DORMANT | INVALIDATED
```

Sequence-status words are research diagnostics. Do not add them to strict production enums unless the live schema explicitly supports them.

New evidence updates the trajectory; it does not create a brand-new thesis every run. Preserve the original first-seen date and each atomic evidence item.

Examples of meaningful trajectory shapes include rank/usage/order data moving `#4 -> #2 -> #1`; one customer deployment -> second independent customer -> supplier lead times rise; one efficiency claim -> repeated operating metric -> financial KPI begins improving; or one cancellation anecdote -> multiple independent channels -> guidance/bookings weaken.

Radar should ask **what changed in the trajectory**, not merely whether another article appeared.

## Escalation and routing

Use existing P0/P1/P2/P3 routes; this lens creates no new route.

- **P3 MONITOR** — credible but weak/isolated observation; next evidence is identifiable but current trajectory is not strong enough to spend much research effort.
- **P2 TARGETED EVIDENCE** — meaningful early signal with a plausible business bridge and a decisive next test. Typical when magnitude/velocity are interesting but persistence, breadth, capture or expectations remain unknown.
- **P1 RWC NOW** — cumulative sequence now shows meaningful acceleration/deterioration, persistence or independent breadth, with a plausible financial bridge and a real expectations question. RWC should test causality, representativeness, capture, confounders and consensus rather than prove the initial story.
- **P0** — use only when the signal indicates credible material permanent-loss/thesis risk requiring immediate attention.

Do not require reported revenue, completed value capture, consensus proof or valuation before P2/P1. Those are downstream questions.

Likewise, do not escalate merely because a ticker is unfamiliar, a social post is viral, app rank is high, a stock moved, or management made a claim.

## Follow-up cadence

Set the next evidence date from the natural speed of the signal:

- very fast signals such as app rank, traffic, inventory/availability, market pricing or outage recovery: next scheduled run or roughly 1–2 days when decision-relevant;
- medium-speed signals such as channel checks, hiring, customer deployments, backlog/lead times or utilization: generally several days to a week;
- slow signals such as KPI conversion, margins, filings, clinical uptake or reported financial capture: align to the next relevant dataset/reporting/catalyst date.

These are defaults, not mandatory timers. Avoid creating one automation per signal. Existing Radar runs revisit due sequences.

## Search behavior

The broad discovery pass should include **trajectory-seeking queries**, not just event-seeking queries. For a newly interesting lead, seek a prior baseline, independent confirmation or contradiction, evidence of acceleration/deceleration, counterparties/substitutes/non-beneficiaries, the next leading metric and later financial KPI, and whether analysts/company guidance/market narrative already recognizes the change.

Do not spend the entire run researching one sequence. Radar stays high-recall and bounded.

## Visible output

Material sequences belong in **New news and opportunities** in the same Radar run.

Use compact labels when helpful:

- **EMERGING SIGNAL — EARLY**: credible P2/P3-level leading indicator; trajectory not yet established.
- **EMERGING SIGNAL — BUILDING**: cumulative evidence is strengthening/weakening across time or independent sources.
- **EMERGING SIGNAL — ESCALATE**: sequence now warrants P1 RWC or P0 risk work.

State the new atomic evidence; what changed versus the sequence baseline; broad archetype(s); why it may matter economically; the strongest counter-hypothesis or missing proof; the next confirmation/falsifier and due date; and route.

Do not show a sequence merely because it remains open with no new evidence, unless a due confirmation was missed or the unresolved item is consequential.

## Guardrails

- No story quota, emerging-signal quota or unfamiliar-ticker quota.
- Do not equate attention with purchases, purchases with revenue, revenue with profit, or growth with attractive valuation.
- Do not treat several wrappers of one origin as breadth.
- Do not retrospectively rewrite the baseline after the trajectory is known.
- Do not confuse price momentum with the operating/behavioral signal unless price itself is the object being studied.
- Do not create automatic trades or bypass RWC/underwriting/allocation for normal investment decisions.
- Event Reaction strategy mechanics remain governed by their separate strategy contract; an emerging issuer signal does not rewrite that frozen mechanical lot.
- Negative and positive leading indicators receive the same treatment.
- If evidence conflicts, preserve the conflict and downgrade confidence rather than average it away.

## Calibration

During the existing rollout review, sample missed and caught events and ask whether an upstream signal was observable before financial/news consensus caught up; whether Radar recorded the first atomic observation; whether it created/reused a sequence; whether meaningful acceleration/deterioration was escalated on time; whether noisy one-offs were left at P3/P2 or invalidated; whether RWC later confirmed/rejected the mechanism; and whether the sequence produced useful research before the market narrative became obvious.

This calibration improves pattern recognition without hard-coding one historical example into the skill.