# Expression / Security Selection Gate

Use this gate for sectoral, macro, commodity, regulatory, thematic, cross-company, or other investment theses with more than one plausible tradable implementation. Complete it after the causal thesis and economic materiality survive, but before advancing any single security to underwriting.

The purpose is to answer a separate question from whether the world thesis is true:

> **What is the best public-market expression of the edge we actually have?**

Do not assume the first company named by Radar, a familiar stock, an owned position, or the most obvious beneficiary is the best expression.

## Mandatory candidate set

When available and relevant, compare:

1. **Individual stock(s)** — direct or second-order corporate beneficiaries.
2. **ETF / ETN / listed fund / commodity pool** — broad or direct packaged exposure.
3. **Basket** — a deliberate multi-security expression when no single issuer deserves the idiosyncratic risk.
4. **Direct underlying / futures / other direct instrument** — the economic variable itself when it is publicly tradable and implementation is practical.
5. **Options or other convex instrument** — only when the catalyst path and timing are bounded enough to justify theta, IV, liquidity, gap, and path risk.
6. **No trade** — when the thesis is true but every available expression is fully priced, structurally poor, too risky, or does not capture the economics.

If a category does not exist or is not accessible, state that explicitly rather than omitting it silently.

## Comparison dimensions

Evaluate each viable expression on the same dimensions:

| Expression | Exposure purity | Economic capture | Mispricing / expectations gap | Idiosyncratic risk | Timing fit | Liquidity / implementation | Portfolio fit | Verdict |
|---|---|---|---|---|---|---|---|---|

Interpret the dimensions as follows:

- **Exposure purity:** how directly the instrument responds to the variable the research edge concerns.
- **Economic capture:** how much of the thesis reaches the security holder after corporate structure, contracts, costs, financing, taxes, capital allocation, dilution, or index/basket dilution.
- **Mispricing / expectations gap:** whether the instrument itself appears to underprice the researched outcome, not merely whether the theme is attractive.
- **Idiosyncratic risk:** management, balance sheet, legal, financing, asset, basis, roll, counterparty, tracking, wrapper, concentration, or other risks unrelated to the core thesis.
- **Timing fit:** whether the instrument duration matches when the evidence should resolve and when value can be realized.
- **Liquidity / implementation:** tradability, spreads, market depth, borrow, roll costs, tax/wrapper constraints, position limits, and practical accessibility.
- **Portfolio fit:** current issuer/theme concentration, correlation, overlapping exposures, account constraints, and whether the expression improves or worsens portfolio construction. Portfolio fit is context, not evidence that the thesis is true.

Do not assume an ETF or fund is lower risk. Futures-based funds, commodity pools, ETNs, leveraged/inverse products, and options can introduce roll, basis, path, credit, leverage, or wrapper risks that must be named.

## Selection heuristics

Use these as defaults, not mechanical rules:

- Prefer the **direct underlying or futures expression** when the edge is principally a short- or medium-horizon move in a spot/forward economic variable and the direct instrument is liquid, understandable, and not already fully priced.
- Prefer an **individual equity** when the differentiated edge is durability, company-specific value capture, operating leverage, asset/NAV appreciation, capital allocation, financing, buybacks/dividends, or an equity expectations lag that the direct market does not reflect.
- Prefer an **ETF or basket** when the thesis is broad across a sector and single-name idiosyncrasy adds risk without a compensating company-specific expectations gap.
- Prefer **options** only when the thesis has a bounded catalyst window and the expected move can plausibly overcome premium, theta, implied-volatility, liquidity, and path risk. A good company thesis with an uncertain catalyst clock is not enough.
- Prefer **no trade / monitor** when the best expression already prices the thesis, when implementation risk dominates the edge, or when no instrument captures the economics cleanly enough.

## Required output

For every mandatory expression-selection case, state:

- **Best direct expression** — or `NONE / UNAVAILABLE`.
- **Best equity expression** — or `NONE / UNAVAILABLE`.
- **Best diversified expression** — or `NONE / UNAVAILABLE`.
- **Chosen expression** — including `NO TRADE` when appropriate.
- **Why it wins** — the exact edge it captures better than the alternatives.
- **What would make another expression superior** — the evidence, price, duration, or structure change that would flip the choice.

The chosen expression must still pass the expectations/priced-in and portfolio-fit checks. Exposure purity alone is not sufficient.

## Routing consequences

A thematic RWC may not route a single stock to `ADVANCE -> FULL UNDERWRITING` until this gate is complete.

After the gate:

- an equity, ETF, ETN, listed fund, or basket requiring medium/long-term valuation work may route to **ADVANCE -> FULL UNDERWRITING**;
- a short-horizon futures, direct-underlying, options, or discrete-event expression may route to **ADVANCE -> EVENT-TRADE UNDERWRITING** only when that downstream contract fits the user's intended horizon;
- unresolved wrapper, roll, basis, liquidity, options, or implementation economics should route to **TARGETED RESEARCH**;
- a credible thesis with no attractive expression should route to **MONITOR**;
- a broken thesis or structurally uninvestable expression should route to **REJECT**.

Do not force an equity just because Full Underwriting is available.

## Example: tanker scarcity

Treat examples as process illustrations, not standing recommendations.

An initial thesis such as **"usable tanker capacity is scarce and freight rates will rise more than the forward market expects"** should compare direct freight/futures exposure, any futures-based listed vehicle, a tanker-equity basket, and individual operators before selecting a stock.

A later, different thesis such as **"freight has already repriced, but tanker equities underprice how long elevated rates will persist and how that duration compounds through FCF, NAV, buybacks, or dividends"** may rationally select an individual operator instead.

The key discipline is to identify where the mispricing sits: in the underlying economic variable, the packaged/direct instrument, the sector, or a specific company's capture and valuation.