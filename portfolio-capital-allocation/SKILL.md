---
name: portfolio-capital-allocation
version: 2
revision: 2026-09-28-evidence-earned-integration
description: Final portfolio-sizing gate after strategy-appropriate underwriting and challenge. Decide whether to start, add, hold, trim, exit or reallocate by combining security payoff, evidence readiness, portfolio loss budget, correlated exposure and opportunity cost. Always distinguish Current, Next, Target and Maximum weight. Never execute trades.
---

# Portfolio Capital Allocation — Evidence-Earned Position Sizing

Read ../investment-strategy-lanes/SKILL.md first, then BASELINE_WORKFLOW.md and only the references the case needs. This file is the strategy-aware integration layer; BASELINE_WORKFLOW.md retains the detailed loss-budget, funding-source, exposure, staged-entry and execution-boundary rules.

## Mission

Full Underwriting answers:

> Is this security attractive enough to own at this price?

Portfolio Capital Allocation answers:

> Given the current portfolio, the evidence already earned, the downside, the competing opportunities and the remaining uncertainty, how much capital should this idea control now?

Keep those decisions separate.

**Central principle: Evidence earns size; price determines payoff; portfolio risk sets the ceiling.**

A lower price is not automatically an add. A higher price is not automatically a trim. A stronger thesis can coexist with a smaller allowed weight because cluster risk or downside increased. A good company can deserve less capital when the remaining payoff or opportunity cost deteriorates.

## Place in the Investment Firm process

Primary route:

`Radar / User Observation -> RWC -> Full Underwriting -> Challenger -> Portfolio Capital Allocation -> Human Decision -> Monitoring / Portfolio Defense -> Closeout / Learning`

Camillo route:

`Observation -> Camillo brief / focused RWC -> Full Underwriting — CAMILLO MODE -> Challenger -> Portfolio Capital Allocation -> Human Decision -> recognition monitoring`

Capital Allocation is the **final portfolio-sizing gate**. It is not a new discovery lane, not another scheduled report and not execution permission.

### Automatic routing conditions inside the process

Run or reopen Capital Allocation when any of these occurs:

1. Full Underwriting advances a new or existing security to capital allocation.
2. A valid BUY/ADD price or payoff boundary is crossed while the underlying underwriting remains current.
3. New evidence materially strengthens or weakens an owned position after the required RWC / underwriting refresh.
4. Portfolio Defense identifies concentration, opportunity cost, instrument risk or another portfolio-level sizing issue.
5. Current weight drifts materially above an approved Maximum or below an actionable Next/Target for reasons that merit review.
6. A completed purchase, sale or other holdings change materially alters the current weight or cluster exposure.
7. A mandatory allocation review date or evidence deadline arrives.

A **price-only** trigger can reopen sizing within the current evidence-stage cap. It cannot by itself promote a position into a higher evidence stage.

If the reason for the price move plausibly changes the business thesis, re-underwrite first. If the thesis is still current and the trigger is purely payoff/portfolio related, do not force a redundant Full Underwriting.

Portfolio Defense may route directly to Capital Allocation when the company/security thesis is unchanged and the issue is concentration, opportunity cost or instrument exposure. Route through Full Underwriting first when the security thesis itself changed.

## The four weights

Every owned or proposed position should carry four distinct fields when the needed portfolio data exist:

- **Current Weight** — verified actual portfolio weight now.
- **Next Action Weight** — the next justified weight if action is warranted at this decision.
- **Target Weight** — the intended weight after the currently expected evidence path is substantially proven.
- **Maximum Weight** — the ceiling under the current thesis, downside, evidence stage and portfolio constraints.

Example:

`Current 2.1% -> Next 3.0% -> Target 4.5% -> Maximum 6.0%`

The normal scale-up decision moves only to **Next**, not directly to Target or Maximum. Scale-downs may skip multiple rungs when risk or evidence deteriorates.

If complete NAV or cash is unavailable, label holdings-only weights clearly and do not pretend they are cash-inclusive NAV weights.

## What must change before weight changes

Do not use a single conviction score. Classify the decision delta across four dimensions.

### Thesis movement
- **Strengthened** — a load-bearing assumption gained credible support, the opportunity expanded or a major risk fell.
- **Unchanged** — new information does not materially change future economics.
- **Weakened** — probability, economics, capture or timing deteriorated.

### Payoff movement
- **Improved** — expected return or recognition asymmetry improved at the current price.
- **Unchanged** — payoff is broadly similar.
- **Deteriorated** — price outran value/recognition payoff, downside increased or timing worsened.

### Evidence movement
- **Proof gained**
- **No proof gained**
- **Proof lost / contradiction emerged**

### Portfolio movement
- **Capacity improved**
- **Neutral**
- **Capacity deteriorated**

The phrase “confidence increased” is insufficient unless it maps to one or more of these.

## Thesis × Payoff decision matrix

| Thesis / Payoff | Payoff improved | Payoff similar | Payoff deteriorated |
|---|---|---|---|
| **Strengthened** | Primary scale-up candidate | Add only if evidence and portfolio capacity justify it | Often hold; scale only if thesis improvement exceeds valuation deterioration |
| **Unchanged** | Opportunistic add candidate within the evidence cap | Hold | No-add / trim review |
| **Weakened** | Usually hold or reduce; add only if price clearly overcompensates and the thesis remains investable | Reduce review | Strong reduce / exit-review condition |

This table opens the review. BASELINE_WORKFLOW.md still controls loss-budget math, funding source, challenge readiness, liquidity, cluster and implementation gates.

## Evidence-earned sizing stages

Use evidence stages to cap how much of the eventual Maximum can be owned. These stages do not replace the underlying loss-budget ceiling.

- **Stage 0 — Watch / no capital.** Research is not decision-ready.
- **Stage 1 — Starter.** A coherent investable case exists, but one or more major proof points remain unresolved.
- **Stage 2 — Developing.** At least one load-bearing uncertainty has materially improved.
- **Stage 3 — Target.** Most decisive links are supported, retained economics / recognition case is credible and the security still clears its strategy-appropriate payoff gate.
- **Stage 4 — Maximum.** Rare. Multiple independent proof points are established and neither single-name nor cluster exposure is binding.

Price alone cannot promote a position to a higher stage.

As a guide, after the case-specific Maximum is determined by the binding portfolio constraints, a Starter often represents only a minority of that Maximum, a Developing position more, Target most, and Maximum the full permitted ceiling. Do not impose universal percentages where the baseline rules or case-specific loss budget say otherwise.

## Loss budget and binding ceiling

Use the detailed BASELINE_WORKFLOW.md calculations.

At minimum show:

`Portfolio Bear Hit = Proposed Weight × Bear/Failure Downside`

and where a user-approved loss budget exists:

`Downside-derived Maximum Weight = Portfolio Loss Budget / Bear/Failure Downside`

For binary, financing-dependent, levered, gap-prone or option-like positions, include complete-loss or gap stress when relevant.

The final Maximum is the **lowest binding ceiling** created by:
- portfolio loss budget;
- evidence readiness;
- single-name concentration;
- causal/thematic cluster exposure;
- liquidity / instrument constraints;
- funding source;
- opportunity cost.

Do not invent the user's loss budget. If none is approved, use clearly labelled sensitivities as BASELINE_WORKFLOW.md requires.

## Causal portfolio clusters

Diversification is not ticker count.

Track shared economic drivers such as:
- AI infrastructure capex;
- inference demand / data movement;
- AI data monetization;
- consumer-agent adoption;
- a common hyperscaler or customer;
- autonomous driving;
- GLP-1 / obesity;
- binary biotech regulatory risk;
- interest rates / duration;
- commodity or power prices.

Core, Camillo, Event Reaction and other actual exposures must be aggregated without double-counting the same lot. A different strategy label is not diversification.

## CORE — Long-term portfolio

Core retains Full Underwriting's business, cash-flow, valuation, capital-structure and required-return gates.

Scale primarily when:
- business evidence strengthens;
- retained economics improve;
- material uncertainty falls;
- balance-sheet / financing risk falls;
- valuation or expected return remains attractive;
- the original variant perception remains under-recognized.

Do not add merely because the stock fell or trim merely because it rose.

## CAMILLO — Speculative information edge

Camillo uses a different evidence sequence, not weaker risk controls.

A credible public observation, coherent causal connection, plausible company exposure, identifiable expectations gap and acceptable downside can justify a **speculative starter before quarterly financial confirmation**.

Additional size can be earned by:
- independent corroboration;
- real user/customer behaviour rather than attention alone;
- stronger company exposure or economic capture;
- acceleration;
- a still-open information edge;
- clearer recognition timing;
- acceptable remaining payoff.

Do not require reported earnings confirmation when waiting for it would destroy the edge.

Until economic capture is better established, the evidence cap may remain below a normal Core position even when the information edge is strong. When recognition catches up, perform an edge-expiry sizing review. A Camillo case may be reduced/closed or may graduate into Core only after fresh Core underwriting and allocation. Never silently convert the thesis.

## Scale-up rules

An add should normally be supported by at least one of:

1. load-bearing evidence confirmation;
2. thesis expansion;
3. material risk removal;
4. strengthening variant perception / information edge;
5. improved recognition timing;
6. materially better payoff with thesis intact;
7. improved portfolio capacity.

Every add must answer:

> **What has this position earned since the previous allocation decision?**

A price-only trigger can justify movement **within** the current evidence-stage cap, not beyond it.

## Scale-down rules

A reduction review can be triggered by:

1. thesis deterioration or a kill criterion;
2. valuation / recognition payoff exhaustion;
3. information-edge expiry;
4. recognition-window or time-stop failure;
5. higher downside or gap risk;
6. cluster concentration;
7. instrument mismatch;
8. superior opportunity cost;
9. evidence that previously justified the weight being lost.

A company does not need to become a bad business for its position to become too large.

## Friday Portfolio Capital Map

The unified Investment Firm Radar should run a **lightweight portfolio-wide Capital Map at Friday 15:00 Toronto** after the latest available holdings and case state are read.

Evaluate every owned position where supported using:

`Current | Next | Target | Maximum | Evidence stage | Bear/failure hit | Major causal cluster | Next sizing trigger`

This is **not** a weekly re-underwriting of every security.

Rules:
- use stored current underwriting/allocation state; do not reconstruct missing targets from memory;
- refresh current holdings and supported weights before comparing;
- flag positions materially above Maximum, materially below an actionable Next/Target, missing an allocation baseline, or creating an excessive cluster;
- route stale or thesis-changing cases back to RWC / Full Underwriting rather than forcing a size decision;
- store the full working map in the existing authorized Investment Firm state/Journal where supported;
- routine user-facing Radar should surface **material allocation exceptions and decisions**, not dump an unchanged all-holdings table;
- no additional scheduled newsletter or task is created.

## Weight Change Memo

Any material START, ADD, TRIM, EXIT or target/maximum reset should preserve an append-only sizing delta:

**Ticker / case / strategy:**  
**Date and reference price:**  
**Current -> Next -> Target -> Maximum:**  
**What changed since the prior allocation decision:**  
**Thesis movement:**  
**Payoff movement:**  
**Evidence earned / lost:**  
**Bear or failure downside:**  
**Portfolio-loss impact at proposed weight:**  
**Relevant cluster exposure before / after:**  
**Funding source / opportunity-cost comparison:**  
**What earns the next increase:**  
**What reverses this decision:**  
**Mandatory review / expiry date:**

Do not rewrite the prior sizing rationale after the outcome is known.

## Required visible result

Lead with:

**Decision:** START / ADD / HOLD / TRIM / EXIT / NO ACTION  
**Current -> Next -> Target -> Maximum:** `__ -> __ -> __ -> __`  
**Why this weight now:** two to four decision-critical sentences.

Then include only the case-relevant:
- decision delta;
- security gate / strategy-appropriate payoff;
- evidence stage;
- loss-budget and Bear/failure hit;
- cluster and opportunity-cost check;
- sizing ladder and next proof;
- add / trim / defense trigger;
- mandatory review date;
- Weight Change Memo.

Retain BASELINE_WORKFLOW.md's formal allocation posture and funding-source requirements where applicable.

## Persistence and human decision boundary

Capital Allocation may create or update a **proposal / decision-support record** only through the currently supported workflow and schemas. It never changes holdings and never implies a proposal was accepted.

The Investment Firm's optional decision queue already models:

`UNDERWRITING -> CAPITAL_ALLOCATION -> DECISION`

Do not enable, deploy or alter that queue merely by running this skill. When the queue is disabled or unavailable, preserve the allocation result in the existing authorized research / Decision List / Journal path and report the persistence limitation.

No analysis, proposal or scheduled Radar run executes a trade.

## Learning

For completed positions or meaningful sizing cycles, review separately:
- thesis accuracy;
- security/payoff quality at the decision price;
- evidence-stage accuracy;
- whether initial size matched uncertainty;
- whether adds followed genuine evidence or excitement;
- whether price-only adds helped;
- whether trims were too early or too late;
- hidden cluster drawdown;
- opportunity-cost decisions;
- instrument survival through the thesis window.

Track recurring errors such as oversized-before-proof, averaging down into deterioration, chasing after recognition, trimming solely because of appreciation, ignoring thematic concentration, optimistic Bear values, or silently moving Target/Maximum after the fact.

Do not judge sizing quality solely by the subsequent stock-price direction.

## Boundaries

- Do not replace Full Underwriting or Challenger.
- Do not invent fair values, expected returns, evidence, holdings, cash or risk tolerance.
- Do not use position sizing to rescue a failed thesis.
- Do not execute trades.
- Do not choose an account without authorization or give tax/account-location advice.
- Do not create a new scheduled report for allocation.
