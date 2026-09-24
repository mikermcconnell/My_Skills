---
name: investment-strategy-lanes
version: 1
revision: 2026-09-24
description: Preserve the distinction between Core long-term portfolio construction and Camillo higher-risk speculative public-information asymmetry across Radar, RWC, Underwriting, challenge, allocation and monitoring. This is a shared strategy contract, not another analysis stage or execution permission.
---

# Two strategies, one investment process

Approved distinction: September 24, 2026. Show the strategy explicitly throughout the existing process. Do not confuse an investment strategy with a news-source or sector checklist.

## Strategy definitions

| Strategy | Main question | Decision logic | Review / exit logic |
|---|---|---|---|
| **CORE — Long-term portfolio** (`CORE_PORTFOLIO`) | Does new evidence support owning this business/security for durable, risk-adjusted returns? | Existing business, cash-flow, valuation, capital-structure, return-hurdle and portfolio-construction underwriting. | Thesis deterioration, valuation/return changes, opportunity cost, concentration and existing instrument rules. |
| **CAMILLO — Speculative information edge** (`CAMILLO_SPECULATIVE`) | What important public-information connection may investors understand next, and is getting ahead of that recognition worth the risk? | Simple dot-connecting, grounded observations, explicit uncertain bets, a plausible expectations gap, recognition timing, remaining payoff and downside. | Falsification, evidence weakening, market recognition catching up, payoff exhaustion, timing failure and instrument/risk limits. |

Core is normally longer-term; Camillo often resolves faster but is NOT defined solely by holding period. Camillo can use shares or options. Core can contain uncertainty and speculative sector overlays. Neither a risky security nor an options contract automatically makes a case Camillo. Classify by the source of expected return and intended decision, not by ticker, source publication, popularity or instrument alone.

Conventional cheapness, a DCF discount, a low multiple, an analyst-target discount or crossing a Core buy level is **not a Camillo go/no-go gate**. Waiting for reported revenue/earnings is not mandatory when a credible early observation supports a testable forward bet. Price still matters to remaining payoff and risk. Evidence that the predicted outcome is already reflected can defeat the case; looking expensive on current earnings alone cannot.

Both strategies require honest sourcing and explicit uncertainty. Higher-risk speculation concerns uncertain future outcomes, not permission to fabricate facts, misuse nonpublic information, assume supplier relationships, copy another investor's trades or dispense with loss limits.

## Authority and compatibility

This contract owns strategy classification, strategy-specific decision gates, case separation and strategy visibility. Each stage's SKILL.md loads it before its BASELINE_WORKFLOW.md. Those baseline files preserve the previous workflows byte-for-byte and remain inherited operating instructions, not separate active skills. Existing source, security, persistence, safety, portfolio and execution controls continue. This contract overrides inherited requirements only where they conflict with the authorized two-strategy distinction: Core-only valuation gates, suppression of Camillo non-price monitoring, ticker-only deduplication, and earlier blanket prohibitions on adding a strategy distinction.

The eleven existing Radar specialist checks, protected broad discovery, newsletters, Emerging Signals, clinical overlays, urgent risk channels and task schedules remain. They can supply either strategy. This change creates no twelfth specialist check, duplicate scan, additional mandatory stage, new task or trade authority.

**Event Reaction remains separate and unchanged.** Exact live Event Reaction/post_earnings lots follow their current frozen manifest and existing mechanics override. Do not fold them into Camillo, override their mechanical exits, or infer their tags from instrument type. Pre-pivotal clinical cases retain their medical, financing and loss-budget rules; classify the strategy from the case rather than automatically assigning every speculative biotech to Camillo.

## Case identity and records

The unit of judgment is a **strategy case**, not a ticker. Preserve, where supported: strategy_lane, strategy_case_id, parent_event_id, original native strategy_id, exact security/instrument/lot scope, source of edge, intended horizon, recognition/realization window, next review, falsifier, case revision, evidence cutoff and decision stage.

These are logical/reporting metadata, NOT a declaration that a backend schema supports new fields or enums. Inspect actual write schemas. Use accepted metadata/free-text fields or an authorized dated fallback when needed; never send unsupported payload keys or overwrite an issuer-wide baseline with a different strategy case. If separate-case storage is unavailable, report CASE_PERSISTENCE_UNAVAILABLE and preserve both cases outside that conflicting slot. Do not fabricate canonical IDs, supported native strategy aliases, trades or database migrations.

One public event can support both strategies: retain one source/event origin and two linked case assessments. `BOTH` is an event-routing label, never a blended capital decision. Research the shared facts once, then state the two different investment implications. Separate their assumptions, decisions, entry/add/exit conditions, clocks and outcomes.

Do not retag historical holdings or migrate accepted baselines automatically. For an explicitly identified existing Core case, retain Core rules; for a documented Camillo case, retain its speculative intent. If the strategy or lot allocation is unclear, show **STRATEGY UNCLASSIFIED — retain existing rules** and resolve the mapping before strategy-specific action. An analytical suggested lane is not an approved position relabel.

Same-ticker cases can coexist. Aggregate real issuer/theme exposure across all lanes, but count each actual lot only once. Do not invent separate share allocations. Opposing instructions that would affect the same actual lot require allocation reconciliation. A Camillo exit is not an instruction to sell unrelated Core shares. Do not silently roll a failed/expired speculation into a long-term holding; a deliberate conversion requires fresh Core underwriting and allocation review with preserved history.

## Radar

Keep one news-discovery run and existing P0/P1/P2/P3 routes. After collecting shared evidence, tag each serious idea CORE, CAMILLO, BOTH or UNCLASSIFIED with a short reason. Do not require a complete valuation or mature financial proof merely to surface a Camillo lead. Test basic signal integrity, plausible company relevance, an identifiable uncertain connection and a useful next check.

A Camillo item should fit: **what changed -> the connection -> what may be missed -> next recognition/check -> what breaks it**. Separate public facts, attributed claims, inference and the bet. Review observable consumer/product behaviour and credible second-order beneficiaries, not only stock-price moves or podcast purchases. No idea quota; source uncertainty and incomplete scans stay visible. Core discovery must not be crowded out by Camillo research, and Camillo must not disappear just because no price boundary crossed.

Preserve existing underwriting-required enums when a store is strict. A Camillo handoff can use the supported Full Underwriting route plus a clearly labelled CAMILLO mode in supported context. A discrete short-duration instrument may also need Event-Trade Underwriting support; this is not the mechanical Event Reaction strategy.

## Research With Confidence

For Core, retain the existing mechanism, materiality, expression, expectations and confidence workflow. For Camillo, read ../camillo-social-arbitrage/SKILL.md and apply the same truth standards with a different stopping rule: verified starting evidence plus a coherent, explicit forward bet can justify advancement before the future outcome is confirmed.

Separate confidence in the observed facts, the dot-connection, the expectations-gap hypothesis and recognition timing. Use the three highest-value checks before expanding. The source's claim is not automatically a fact; unknown future adoption is not automatically a research failure. Do not route all early cases to 'wait for earnings'. Reject an incoherent connection, not uncertainty itself.

Keep expression selection proportionate: compare the obvious security, one or two credible alternatives and no trade. Examine additional wrappers when genuinely relevant; do not force an exhaustive instrument survey onto a simple company-specific Camillo case. Preserve factual/source independence, counterfactuals and Portfolio Defense boundaries.

Advance surviving Camillo research as **ADVANCE -> FULL UNDERWRITING — CAMILLO MODE** in the report; retain compatible native routing fields. This is research readiness, not a buy or allocation approval.

## Underwriting, challenge and allocation

Core uses full-underwriting/BASELINE_WORKFLOW.md and its existing valuation/hurdle rules. Camillo uses full-underwriting/references/camillo-speculative-underwriting.md. Both retain exact-security identity, current-price checks for decisions, financing/claims where material, failure analysis, instrument suitability, dates, challenge and allocation boundaries.

Show separately: **information-edge judgment**, **security/instrument judgment**, and **portfolio permission**. A compelling information edge can coexist with an unsuitable option or unavailable allocation budget. Do not downgrade the information thesis merely because personal cash/limits are unavailable; do not turn that thesis into an executable recommendation without the missing inputs.

The challenger must challenge the assigned strategy rather than reimpose Core cheapness. Capital Allocation evaluates Camillo using its failure/delay/recognition payoff, instrument risk and an explicit speculative loss budget, not a mandatory Core DCF or fixed annualized hurdle imported by accident. Existing approved strategy-specific hurdles still apply. Never invent a risk budget, default portfolio percentage, leverage permission or contract count from the phrase 'higher risk'. Aggregate speculative loss, correlated Core exposure, issuer concentration, liquidity and funding. Additional size requires named evidence and a fresh payoff/risk check, not price appreciation alone.

## Visible output in every relevant stage

Every Radar report retains its three top-level sections. Within each, distinguish **CORE — Long-term portfolio** and **CAMILLO — Speculative information edge**. Both must remain visible even on quiet runs, using a compact 'No material change in checked sources', 'No active mapped cases' or 'Not assessed / coverage incomplete' as actually applicable. Do not fabricate a finding to fill a lane.

Under the Stock monitor retain **Event Reaction — strategy mechanics** first where applicable, then separate Core and Camillo queues, plus unresolved strategy mapping when present. Core keeps its valid stored price and defense rules. Camillo tracks eligible dated case state even without a price trigger: observation/edge change, recognition/falsifier, review deadline, instrument timing, actual stage and next action. A readable dated research case is a **RESEARCH CASE — NOT AN ACTIVE TRADE MONITOR** unless a supported active monitor exists; do not relabel it CANONICAL merely to put it in a table. Distinguish research coverage from active-monitor coverage.

Use case + strategy + exact instrument/lot for action deduplication. Preserve canonical/legacy/defense source precedence WITHIN that scope; do not collapse conflicting Core/Camillo conclusions into one ticker verdict. Do not double-count source origins or actual holdings.

RWC and Underwriting reports begin with **Strategy / Case / Stage / Horizon**. When both lanes are assessed, provide separate conclusions and next steps. In a single-lane report, briefly label the other 'Not assessed in this run' rather than inventing a second thesis. Daily Brief and Portfolio Defense outputs retain lane labels and their existing overall format. Do not repeat full analyses merely to display the distinction.

## Monitoring and learning

Camillo display states may include EARLY, BUILDING, READY FOR SPECULATIVE UNDERWRITING, EDGE FADING, RECOGNITION OCCURRING, EDGE EXHAUSTED and INVALIDATED. These are explanatory state labels, not backend enum or trading instructions. Maintain the actual research/underwriting/allocation stage separately. Recognition triggers reassessment of remaining payoff, not an automatic sale; explicit instrument/loss rules still apply. Never treat a preserved research result as a completed worker run or a filled order.

Record outcomes separately by strategy: observation accuracy, connection accuracy, timing of recognition, thesis failure, instrument result and net investment outcome. Preserve failed, rejected and unresolved cases. Do not blend speculative wins into evidence that the Core approach works, or vice versa. Configuration verification is not proof of live execution, notification delivery or a profitable strategy.
