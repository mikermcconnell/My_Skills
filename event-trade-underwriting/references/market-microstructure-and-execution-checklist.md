# Market Microstructure and Execution Checklist

A theoretical event edge is not actionable unless the user can reasonably enter, survive, and exit at the modeled prices.

## Market and dissemination clock

Record:

- exchange and normal trading hours;
- current local time and timezone;
- whether the market is open, pre-market, after-hours, auction, halted, or closed;
- scheduled event time and likely release channel;
- whether the source was public, designated, embargoed, leaked, or unverified;
- first public timestamp and first meaningful price reaction;
- whether related local shares, ADRs, options, futures, peers, or sector instruments traded first.

Do not compare an event with a price that predates public dissemination or assume the user could trade before the information became public.

## Tradable-price check

Use when available:

```text
bid
ask
midpoint
last trade and timestamp
spread in dollars and percent
quoted depth
normal and event-period volume
pre-market or after-hours volume
```

The last price may be stale or non-executable. For a long entry, use the ask or a defensible limit price; for a sale or short, use the bid and include borrow constraints.

## Liquidity stress

Check:

- free float and insider concentration;
- normal average daily value traded;
- event-day volume and whether it is one-sided;
- proposed order as a share of normal volume;
- expected participation rate;
- spread and depth under normal and stressed conditions;
- days-to-exit under transparent assumptions;
- possibility of a trading halt, limit up/down, auction imbalance, suspension, or delisting.

Do not assume that headline daily volume is available at one price.

## Slippage and costs

Include when material:

- half-spread or full crossing cost;
- market-impact estimate with stated limitations;
- commissions and fees;
- foreign exchange and settlement costs supplied by the user;
- borrow fee, locate cost, recall, and dividend obligation for shorts;
- option premium, implied volatility, skew, and volatility crush;
- bid/ask and assignment/exercise risk for options;
- opportunity cost when the event is delayed.

Stress at least a doubling of spread/slippage in a volatile event.

## Short-sale checklist

Do not recommend a short unless explicitly requested and supported by:

- confirmed borrow availability and timestamp;
- borrow fee and possibility of change;
- free float, short interest, days to cover, and squeeze risk when available;
- recall and forced buy-in risk;
- maximum loss and gap risk;
- halt or takeover risk;
- dividends, distributions, or corporate actions;
- an exit plan that does not depend on orderly liquidity.

A favourable fundamental thesis does not eliminate unlimited or very large short-side path risk.

## Options checklist

Do not recommend an option structure unless explicitly requested and the chain is current enough to evaluate:

- underlying price and timestamp;
- expiry relative to the event and possible delay;
- strikes, bid/ask, open interest, volume, and contract multiplier;
- implied volatility and term structure;
- skew and event premium;
- expected volatility crush;
- delta, gamma, theta, and vega relevant to the structure;
- assignment, exercise, settlement, early exercise, and pin risk;
- maximum profit, maximum loss, and break-even;
- ability to close the position after the event.

Do not use mid-market option marks as guaranteed executions in illiquid contracts.

## ADR, dual listing, and foreign-market risk

Check:

- which listing incorporates the event first;
- local-market holiday or closure;
- ADR ratio and conversion;
- currency movement;
- stale local price versus live ADR price;
- settlement, withholding, custody, and access constraints supplied by the user;
- whether the apparent arbitrage is actually inaccessible or consumed by costs.

## Rumour and manipulation risk

For social or anonymous claims:

- identify the earliest observable source;
- determine whether it cites a document, named person, screenshot, or circular reporting;
- search for issuer, regulator, exchange, court, or counterparty confirmation;
- check for trading halts or unusual volume preceding the claim;
- label impersonation, edited media, paid promotion, and coordinated amplification risk;
- route load-bearing verification to RWC.

No primary confirmation normally means `WAIT FOR CONFIRMATION`, `NO TRADE`, or `REJECT`, not a larger risk premium.

## Execution-readiness grades

Use one:

- **High:** liquid security, current executable price, normal access, limited halt/borrow complexity, and modeled slippage is credible.
- **Medium:** trade is possible but spreads, after-hours timing, event gap, foreign access, or moderate liquidity meaningfully affect payoff.
- **Low:** modeled prices are doubtful, liquidity is thin, halt/borrow/options risk is high, or access is uncertain.
- **Not executable:** the user cannot reasonably implement the modeled trade or required market data is absent.

Execution confidence is separate from evidence confidence and expectations confidence.

## No-trade microstructure triggers

Return `NO TRADE` or `REJECT` when:

- the expected edge is smaller than credible spread, slippage, borrow, or option costs;
- the security has already moved beyond the maximum acceptable entry;
- the event is public but normal liquidity has not reopened;
- the thesis requires a short without confirmed borrow;
- an option structure depends on an expiry before a plausible event delay;
- the outcome can gap beyond the user's maximum loss with no practical hedge or exit;
- the only apparent edge depends on stale prices across listings;
- source authenticity or dissemination timing cannot be established.
