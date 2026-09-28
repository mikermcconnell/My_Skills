# Macro / Cross-Asset Regime Lens — News Radar V3

Approved September 28, 2026. This is a **Core research overlay inside protected discovery**, not a twelfth specialist lane, separate strategy, score, newsletter, task or trading system.

Its purpose is to catch macro and cross-asset changes that can alter discount rates, financing conditions, demand, margins, liquidity or portfolio risk **before** the effect is obvious in company-reported fundamentals.

> macro / cross-asset change -> transmission mechanism -> affected business assumptions -> company/security evidence test

Radar detects the regime change and maps plausible transmission. RWC tests whether the transmission is real and material for a company. Full Underwriting changes valuation/posture only when the accepted business or security assumptions actually warrant it.

## Required bounded check each slot

During the existing Core protected open-universe discovery pass, inspect a compact current macro/cross-asset state before routine case expansion and full stock-monitor assembly. Reuse a fresh same-slot source when available; do not repeatedly fetch the same series.

The minimum state is:

- **U.S. rates:** Treasury 2Y, 10Y and 30Y nominal yields.
- **Real-rate / inflation decomposition:** 5Y or 10Y real yield and corresponding inflation breakeven when reliable comparable observations are accessible.
- **Curve:** at least 2s10s; optionally 5s30s when it adds information.
- **Policy expectations:** the observable Fed-path repricing from a reliable futures/OIS or equivalent source when accessible.
- **Credit:** broad investment-grade and high-yield spread/OAS condition when accessible.
- **Dollar:** broad U.S.-dollar condition or a clearly identified liquid proxy.
- **Energy / inflation impulse:** WTI and/or Brent when the move is decision-relevant.
- **Risk / liquidity:** a broad equity-volatility measure and, when accessible, a rates-volatility or funding-stress measure.
- **Canada overlay:** Government of Canada 2Y/10Y, CAD/USD and Bank of Canada-path evidence when material to Canadian securities, CDRs or domestic economic exposure.

This is a **bounded regime screen**, not a requirement to publish a dashboard or collect every macro series on every run.

## Source hierarchy

Prefer primary or closest-to-market sources and timestamp each observation:

- U.S. Treasury / Federal Reserve / FRED for Treasury, TIPS, breakeven and credit-series observations where available.
- Federal Reserve statements, minutes and official releases for policy decisions; futures/OIS/CME or another reliable market source for market-implied policy-path changes.
- Bank of Canada / Government of Canada / Statistics Canada for Canadian rates and macro releases.
- BLS, BEA, Census, EIA and other relevant official agencies for inflation, labor, growth, trade and energy data.
- Exchange/consolidated or other reliable market-data sources for FX, commodities and volatility.
- Reuters or similarly strong financial journalism for rapid context, attribution hypotheses and cross-market synthesis, followed by primary-source checks where decision-relevant.

A news article is not the underlying yield, spread or official data release. Preserve observed market data separately from reported explanations.

## Snapshot and comparison rules

Where supported, retain:

```text
macro_snapshot_id
observed_at
series_name
instrument_or_series_id
value
unit
source
source_timestamp
retrieval_timestamp
session_or_release_context
prior_comparable_value
prior_comparable_timestamp
change
comparison_window
source_precision
access_status
```

Do not create a fake synchronous snapshot from stale observations collected at materially different times. Keep each series' timestamp.

Compare like with like. Do not mix:
- nominal yield with real yield;
- yield level with basis-point change;
- credit spread with bond yield;
- futures-implied policy probability with an official policy rate;
- spot oil with a different futures contract without labeling it;
- CAD translation effects with company operating fundamentals.

## What counts as a macro signal

Do not print routine market noise. Surface when one or more of these is true:

1. **Discontinuity:** a large or unusually fast move versus the series' recent baseline.
2. **Regime boundary:** a new multi-month / 52-week / multi-year high or low, a meaningful curve inversion/steepening change, or another historically relevant level.
3. **Cross-asset confirmation:** rates, real yields, breakevens, credit, FX, commodities or volatility move coherently enough to support a common transmission hypothesis.
4. **Persistence:** the move survives multiple observations/sessions rather than immediately reversing.
5. **Portfolio transmission:** the move plausibly changes financing cost, discount rate, demand, margins, liquidity or risk for one or more current cases.
6. **Expectations reset:** official data or policy evidence materially reprices the expected growth/inflation/policy path.

A single strong discontinuity can surface as **EMERGING SIGNAL — EARLY** when the consequence and next test are clear. Persistence and cross-asset breadth can move it to BUILDING or ESCALATE under the existing Emerging Signal contract.

Do not create a numeric macro score or fixed trigger quota. Magnitude must be judged against the series' own recent behavior and the current market regime.

## Core decomposition — ask what is actually moving

### Nominal yields

When long Treasury yields move materially, do not stop at "rates up/down." If reliable data are available, separate:

- **real-yield move** — changes the real discount rate and financing hurdle;
- **breakeven-inflation move** — changes inflation expectations and policy/margin risk;
- **curve / term-premium / supply component** — may reflect growth, fiscal supply, duration risk or term premium. Any term-premium estimate is model-based and must be labeled as such.

If decomposition is unavailable, say so rather than infer the driver.

### Credit

A Treasury-yield increase with stable/tighter spreads is different from higher yields plus widening credit spreads.

- stable/tighter spreads -> primarily rate/discount-rate pressure;
- widening IG/HY spreads -> increasing financing stress, risk aversion or default concern;
- sharply wider spreads plus weaker equities/liquidity -> possible portfolio-defense escalation.

### Dollar and commodities

- stronger USD can tighten global financial conditions and pressure translated foreign earnings or commodity-sensitive borrowers;
- weaker USD can reverse those effects;
- higher oil can support energy cash flows while worsening inflation, transport and consumer purchasing power;
- lower oil can relieve inflation while challenging producers/shippers depending on cause.

Always identify the causal uncertainty; oil can rise because demand improves or because supply is impaired, with very different equity implications.

## Transmission map to company research

When a macro signal matters, map it only to business mechanisms that are actually plausible.

### Long-duration growth / AI infrastructure
Watch real yields, long nominal yields, credit spreads and power/financing conditions.

Possible bridge:
higher cost of capital -> higher required project ROIC / lower distant-cash-flow present value -> pressure on externally financed or low-current-cash-flow capacity builds.

Do not assume higher yields invalidate high-ROIC reinvestment. RWC should compare incremental project returns with the changed financing hurdle.

### Utilities / regulated capital programs
Watch long rates, utility credit spreads, allowed returns, debt issuance and equity-financing requirements.

Possible bridge:
higher funding cost -> capital-plan pressure / regulatory lag -> slower rate-base growth or dilution risk.

### Financials
Watch curve shape, credit spreads, deposit betas, funding costs and credit quality.

A steeper curve is not automatically positive if credit losses or funding stress rise simultaneously.

### Consumer / housing
Watch mortgage/consumer rates, labor, real income, credit delinquencies and energy.

Possible bridge:
higher borrowing costs -> weaker housing/discretionary demand -> volume/mix/credit changes.

### Industrials / leveraged infrastructure
Watch debt costs, project finance, capex hurdle rates, backlog financing and customer funding.

### Energy / shipping
Separate commodity price, physical supply disruption, demand, freight/insurance and inflation effects. Oil price alone does not determine tanker earnings.

### Canadian exposures / CDRs
Use Canadian rates and CAD/USD where economically relevant. Do not treat a CDR's FX translation as a change in the issuer's underlying business.

## Signal Sequence memory

Macro conditions often persist across many runs. Reuse stable parent hypotheses rather than create a new story each slot.

Example sequence identities in manifest/fallback only, when useful:

- `MACRO-US-LONG-RATE-REGIME`
- `MACRO-US-REAL-YIELD-REGIME`
- `MACRO-CREDIT-TIGHTENING`
- `MACRO-USD-LIQUIDITY`
- `MACRO-OIL-INFLATION-SHOCK`
- `MACRO-CANADA-RATE-REGIME`

These are reporting/research identifiers, not new production enums. Preserve the first-seen date, prior baseline, observations, driver hypothesis, counter-hypothesis, affected cases and next confirmation/falsifier.

## Routing

Use the existing routes only:

- **P3 MONITOR:** notable macro move but weak company transmission or low persistence.
- **P2 TARGETED EVIDENCE:** meaningful regime move with a plausible company/sector bridge; identify the exact company metric or financing evidence to test.
- **P1 RWC NOW:** persistent/broad macro move materially threatens or strengthens an accepted company assumption, financing model or expectations gap.
- **P0:** only when macro/market stress creates credible imminent permanent-loss, liquidity, covenant, refinancing or instrument risk.

Macro itself does not automatically trigger Full Underwriting. Escalate a specific case when the transmission changes a load-bearing assumption.

## Visible Radar output

When material, show one compact card in **New news and opportunities**:

**MACRO — EMERGING SIGNAL — EARLY / BUILDING / ESCALATE | <regime>**

Include:
- observed move and exact cutoff;
- baseline/comparison window;
- decomposition into real yield / inflation / credit / FX / commodity drivers when supported;
- simple transmission chain, e.g. `higher real yields -> higher WACC -> tougher capex hurdle / lower distant-CF PV`;
- affected portfolio cases or sector read-through;
- strongest counter-hypothesis;
- next confirmation/falsifier;
- existing P1/P2/P3/P0 route.

Do not print a routine macro dashboard when nothing material changed.

In **Changes to existing investment cases**, show only cases where macro transmission materially changes the question being tested. Do not turn a common-factor move into duplicate issuer news for every holding.

The **Stock monitor** remains governed by the exception-only price-monitor contract; macro observations do not create stock-monitor rows unless an accepted buy/sell/near condition independently qualifies.

## Guardrails

- Macro market moves are evidence, not automatic investment decisions.
- Do not attribute a market move to one cause without evidence.
- Do not infer company earnings effects directly from rates/FX/oil without a transmission bridge.
- Do not change fair value, thesis, target, trigger, position size or risk budget inside Radar.
- Do not create a "macro strategy" or portfolio hedge automatically.
- Do not let macro commentary crowd out protected open-universe company discovery or Camillo observation-first discovery.
- Do not print repeated unchanged yield levels merely because they are high/low.
- Do not treat one bond auction, one CPI print or one oil spike as a regime unless the magnitude/materiality justifies an EARLY signal and the next test is explicit.
- Positive and negative regime changes receive the same treatment.

## Calibration

During existing Radar calibration, check whether material macro regime changes were detected near their first observable break; whether the driver decomposition was evidence-based; whether company transmission was tested rather than assumed; whether macro noise was suppressed; and whether later company evidence confirmed or rejected the proposed bridge.

No new audit task, macro newsletter, automation or score is created.
