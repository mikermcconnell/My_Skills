---
name: investment-strategy-lanes
version: 1
revision: 2026-09-25-unified-reporting
description: Preserve the distinction between Core long-term portfolio construction and Camillo higher-risk speculative public-information asymmetry across Radar, RWC, Underwriting, challenge, allocation and monitoring. This is a shared strategy contract, not another analysis stage or execution permission.
---

# Two strategies, one investment process

Approved distinction: September 24, 2026. Show the strategy explicitly throughout the existing process. Do not confuse an investment strategy with a news-source or sector checklist. September 25 reporting consolidation uses one Radar publisher; see ../investment-firm-output/SKILL.md version 14 or later for publication and Event Reaction alert-only display. Analytical gates below remain unchanged.

## Strategy definitions

| Strategy | Main question | Decision logic | Review / exit logic |
|---|---|---|---|
| **CORE — Long-term portfolio** (`CORE_PORTFOLIO`) | Does new evidence support owning this business/security for durable, risk-adjusted returns? | Existing business, cash-flow, valuation, capital-structure, return-hurdle and portfolio-construction underwriting. | Thesis deterioration, valuation/return changes, opportunity cost, concentration and existing instrument rules. |
| **CAMILLO — Speculative information edge** (`CAMILLO_SPECULATIVE`) | What important public-information connection may investors understand next, and is getting ahead of that recognition worth the risk? | Simple dot-connecting, grounded observations, explicit uncertain bets, a plausible expectations gap, recognition timing, remaining payoff and downside. | Falsification, evidence weakening, market recognition catching up, payoff exhaustion, timing failure and instrument/risk limits. |

Core is normally longer-term; Camillo often resolves faster but is NOT defined solely by holding period. Camillo can use shares or options. Core can contain uncertainty and speculative sector overlays. Neither a risky security nor an options contract automatically makes a case Camillo. Classify by the source of expected return and intended decision, not by ticker, source publication, popularity or instrument alone.

Conventional cheapness, a DCF discount, a low multiple, an analyst-target discount or crossing a Core buy level is **not a Camillo go/no-go gate**. Waiting for reported revenue/earnings is not mandatory when a credible early observation supports a testable forward bet. Price still matters to remaining payoff and risk. Evidence that the predicted outcome is already reflected can defeat the case; looking expensive on current earnings alone cannot.

Both strategies require honest sourcing and explicit uncertainty. Higher-risk speculation concerns uncertain future outcomes, not permission to fabricate facts, misuse nonpublic information, assume supplier relationships, copy another investor's trades or dispense with loss limits.

## Authority and compatibility

This contract owns strategy classification, strategy-specific decision gates and case separation. Each stage's SKILL.md loads it before its BASELINE_WORKFLOW.md. Those baseline files preserve previous workflows and remain inherited instructions, not separate active skills. Existing source, security, persistence, safety, portfolio and execution controls continue. This contract overrides inherited requirements where they conflict with the authorized two-strategy distinction: Core-only valuation gates, suppression of Camillo non-price monitoring, ticker-only deduplication and earlier blanket prohibitions on strategy distinction.

The current output contract and MONITOR_V3 own consolidated publisher/standing-view ownership and ER alert-only presentation, overriding superseded separate-brief and mandatory-table instructions. The eleven Radar specialist checks, protected broad discovery, newsletters, Emerging Signals, clinical overlays and urgent risk channels remain. They can supply either strategy. The one routine Radar task runs at 08:00, 11:00 and 15:00 Toronto daily; synthesis is integrated, not a separate mandatory stage.

**Event Reaction mechanics remain separate and unchanged.** Exact live Event Reaction/post_earnings lots follow the current frozen manifest and mechanics override, but display only as new verified trigger alerts, not a recurring table. Do not fold them into Camillo, override exits or infer tags from instrument type. Pre-pivotal clinical cases retain their medical, financing and loss-budget rules; not every speculative biotech is Camillo.

## Case identity and records

The unit of judgment is a **strategy case**, not a ticker. Preserve, where supported: strategy_lane, strategy_case_id, parent_event_id, original native strategy_id, exact security/instrument/lot scope, source of edge, intended horizon, recognition/realization window, next review, falsifier, case revision, evidence cutoff and decision stage.

These are logical/reporting metadata, NOT a declaration that a backend schema supports new fields or enums. Inspect actual write schemas. Use accepted metadata/free-text fields or an authorized dated fallback when needed; never send unsupported payload keys or overwrite an issuer-wide baseline with a different strategy case. If separate-case storage is unavailable, report CASE_PERSISTENCE_UNAVAILABLE and preserve both cases outside that conflicting slot. Do not fabricate canonical IDs, supported native strategy aliases, trades or database migrations.

One public event can support both strategies: retain one source/event origin and two linked case assessments. `BOTH` is an event-routing label, never a blended capital decision. Research the shared facts once, then state the two different implications. Separate assumptions, decisions, entry/add/exit conditions, clocks and outcomes.

Do not retag historical holdings or migrate accepted baselines automatically. For an explicitly identified Core case retain Core rules; for a documented Camillo case retain its speculative intent. If strategy or lot allocation is unclear, show **STRATEGY UNCLASSIFIED — retain existing rules** and resolve mapping before strategy-specific action. An analytical suggested lane is not an approved position relabel.

Same-ticker cases can coexist. Aggregate actual issuer/theme exposure across all lanes but count each actual lot only once. Do not invent separate share allocations. Opposing instructions affecting the same actual lot require allocation reconciliation. A Camillo exit is not an instruction to sell unrelated Core shares. Do not silently roll a failed/expired speculation into a long-term holding; conversion requires fresh Core underwriting and allocation review with preserved history.

## Radar

Keep one discovery run and existing P0/P1/P2/P3 routes. Collect protected Core and Camillo evidence under the current discovery contracts. Tag serious ideas CORE, CAMILLO, BOTH or UNCLASSIFIED with a reason. Do not require complete valuation or mature financial proof merely to surface a Camillo lead. Test basic signal integrity, plausible consequence, an identifiable uncertain connection and a useful next check; company mapping can be unresolved.

A Camillo item should fit: **what it is -> what changed -> the connection -> what may be missed -> next recognition/check -> what breaks it**. Separate facts, claims, inference and the bet. Review observable consumer/product behaviour and credible second-order beneficiaries, not only prices or podcast purchases. No idea quota; source uncertainty and incomplete scans stay visible. Core discovery cannot be crowded out by Camillo, and Camillo cannot disappear merely because no price boundary crossed.

Preserve existing underwriting-required enums when a store is strict. A Camillo handoff can use the supported Full Underwriting route plus a labelled CAMILLO mode in supported context. A discrete short-duration instrument may also need Event-Trade Underwriting support; this is not the mechanical Event Reaction strategy.

## Research With Confidence

For Core retain the existing mechanism, materiality, expression, expectations and confidence workflow. For Camillo read ../camillo-social-arbitrage/SKILL.md and use the same truth standards with a different stopping rule: verified starting evidence plus a coherent, explicit forward bet can justify advancement before the future outcome is confirmed.

Separate confidence in observed facts, the connection, expectations-gap hypothesis and recognition timing. Use the three highest-value checks before expanding. A source claim is not automatically fact; unknown future adoption is not automatically research failure. Do not route every early case to waiting for earnings. Reject an incoherent connection, not uncertainty itself.

Keep expression selection proportionate: compare the obvious security, one or two credible alternatives and no trade. Examine other wrappers when relevant, not as an exhaustive prerequisite to a simple company-specific Camillo case. Preserve source independence, counterfactuals and Portfolio Defense boundaries.

Advance surviving Camillo research visibly as **ADVANCE -> FULL UNDERWRITING — CAMILLO MODE**, retaining compatible native routing fields. This is research readiness, not buy/allocation approval.

## Underwriting, challenge and allocation

Core uses full-underwriting/BASELINE_WORKFLOW.md and existing valuation/hurdle rules. Camillo uses full-underwriting/references/camillo-speculative-underwriting.md. Both retain exact-security identity, current-price checks for decisions, material financing/claims, failure analysis, instrument suitability, dates, challenge and allocation boundaries.

Show separately: **information-edge judgment**, **security/instrument judgment**, **portfolio permission**. A compelling edge can coexist with an unsuitable option or unavailable budget. Missing personal cash/limits do not invalidate the information thesis, but prevent an executable recommendation without those inputs.

The challenger must challenge the assigned strategy rather than reimpose Core cheapness. Allocation evaluates Camillo using failure/delay/recognition payoff, instrument risk and an explicit speculative loss budget, not an accidentally imported mandatory Core DCF or fixed annualized hurdle. Actually approved strategy-specific hurdles still apply. Never invent a budget, default portfolio percentage, leverage permission or contract count from 'higher risk'. Aggregate speculative losses, correlated Core exposure, issuer concentration, liquidity and funding. Adds require named evidence and a fresh payoff/risk review, not price appreciation alone.

## Visible output

The unified Radar retains three main sections and visible **CORE — Long-term portfolio** and **CAMILLO — Speculative information edge** labels within each. Use truthful compact no-change/no-mapped-case/not-assessed notes; no invented findings to fill a lane.

The recurring stock monitor contains Core, Camillo and unresolved mapping as applicable, **not an Event Reaction inventory**. New verified mechanical hits appear as deduplicated alert callouts under the output/ER contracts. No ER hold/proximity/quiet rows. Core retains stored price and defense rules. Camillo tracks dated observation/edge change, recognition/falsifier, review deadline, instrument timing, actual stage and next action even without a price trigger. A dated research case is **RESEARCH CASE — NOT AN ACTIVE TRADE MONITOR** unless supported active monitor state exists. Distinguish research from active-monitor coverage.

Use case + strategy + exact instrument/lot for action dedup. Preserve canonical/legacy/defense precedence within that scope, not an issuer-wide verdict. Never double-count source origins or holdings.

RWC/Underwriting begin with **Strategy / Case / Stage / Horizon** and plain subject context. Separate conclusions when both strategies are assessed; otherwise label the other not assessed. Daily synthesis lives inside 15:00 Radar, not a separate brief. Portfolio Defense retains its internal/urgent-only role and strategy labels. Do not duplicate full analyses solely for display.

## Monitoring and learning

Camillo display states may include EARLY, BUILDING, READY FOR SPECULATIVE UNDERWRITING, EDGE FADING, RECOGNITION OCCURRING, EDGE EXHAUSTED and INVALIDATED. These are explanatory labels, not backend enums or trading instructions; keep actual workflow stage separate. Recognition prompts a remaining-payoff review, not automatic sale. Existing instrument/loss rules still apply. A preserved result is not a completed worker or filled order.

Record outcomes separately by strategy: observation accuracy, connection accuracy, recognition timing, thesis failure, instrument result and net investment outcome. Preserve failed/rejected/unresolved cases. Do not blend speculative wins into proof of Core efficacy or vice versa. Saved configuration, synthetic tests, a completed scan, delivery and profitable real-world performance are different facts.
