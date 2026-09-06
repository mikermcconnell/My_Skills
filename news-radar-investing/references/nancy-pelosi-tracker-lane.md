# Nancy Pelosi Congressional-Disclosure Tracker — News Radar V3

This contract defines the permanent Nancy Pelosi stock/options disclosure lane for News Radar V3. It is a congressional-disclosure / alternative-data lane, not an investment recommendation, political judgment, or allegation of informational advantage.

## Purpose

On every scheduled Radar pass, check for newly public financial-disclosure filings by **Nancy Pelosi** that report transactions in publicly traded stocks, ETFs, options, or other marketable securities. Purchases are the primary focus, but material sales, option exercises, exchanges, and amendments must also be captured when they change the meaning of a prior disclosure.

The lane exists to answer:

- What new Pelosi household securities transaction became public?
- When did the underlying transaction occur versus when was it disclosed?
- Was the asset stock, call/put option, or another security?
- Who is identified as the owner in the official filing?
- Does the transaction overlap an owned holding, active underwriting, watchlist, or active thesis?
- Is there any public, independently testable business/catalyst evidence worth routing to Research With Confidence?

It must **not** answer "should we copy the trade?" from the disclosure alone.

## Source hierarchy

Use sources in this order:

1. **Official House Clerk Financial Disclosure / Periodic Transaction Report (PTR) filing** — source of truth for the disclosed transaction.
2. **House Committee on Ethics guidance** — source of truth for filing mechanics and timing requirements.
3. High-quality secondary congressional-trade databases or news reports — discovery/reconciliation only; use them to find a possible filing, not to supersede the official PTR when the filing is available.
4. Social posts, screenshots, newsletters, X posts, Reddit, or viral "Pelosi trade" claims — leads only until tied to an official filing or another reliable primary record.

The House Clerk's public financial-disclosure database is the canonical public source. Under House ethics/STOCK Act rules, reportable transactions generally must be disclosed by the earlier of **30 days after the filer is made aware of the transaction or 45 days after the transaction**. Therefore this lane is inherently delayed relative to execution.

## Identity and ownership discipline

Do not casually say "Nancy Pelosi bought" when the filing identifies another owner.

Preserve exactly when available:

```text
filer: Nancy Pelosi
owner_code / owner_label
asset_name
ticker
asset_type
transaction_type
transaction_date
notification_date
filing_date
filing_id
amount_range
option_details
source_url
```

If the official filing identifies `SP` (spouse), say **"Pelosi disclosure — spouse transaction"** or **"Pelosi household disclosure"** rather than implying the Member personally executed the trade. Preserve any other owner code exactly as reported.

Never infer who made the investment decision beyond what the filing supports.

## Transaction normalization

For every new official transaction row, capture:

- official filing ID / document ID;
- filing/publication date;
- transaction date;
- notification date when provided;
- filer and owner code;
- issuer / asset name and ticker when resolvable;
- transaction type: purchase, sale, exchange, exercise, or other official label;
- disclosed dollar range — **never convert the range to an exact amount**;
- asset type;
- for options when disclosed: call/put, strike, expiration, contract count, exercise or purchase status;
- elapsed days from transaction to disclosure;
- overlap with current holdings, derivatives, active underwritings, watchlist names, or thesis exposures;
- whether the transaction is new, amended, previously reported, or a secondary-source duplicate.

### Options rules

A purchased call or put is a directional instrument, but its meaning depends on strike, expiry, premium, and whether it replaces or extends prior exposure. Do not translate an option disclosure directly into a stock-equivalent conviction level.

Do not double-count an option **exercise** as both a new option trade and a fresh common-stock purchase when it is simply conversion of previously disclosed options. Preserve exercise date and resulting share exposure separately when the filing supports it.

If option details are missing or ambiguous, say so. Never fabricate strike, expiration, premium, delta, contract count, or notional exposure.

## Disclosure-lag and detection rules

The underlying transaction may predate the current Radar scan window by weeks even when the PTR itself became public during the current window.

Treat the **filing/publication date** as the Radar discovery event and preserve the older **transaction date** separately. Do **not** label a transaction `LATE_DETECTION` merely because the trade date predates the current scan window when the official filing only became public during the current window.

Use normal V3 `LATE_DETECTION` only when the public filing itself was available before the scan window and no matching Event Ledger record exists.

Always show the reporting lag for a surfaced trade because it materially limits copy-trading usefulness.

## Interpretation boundary

A Pelosi household disclosure is **alternative data / a research lead**, not causal company evidence.

Do not infer:

- inside information;
- illegality or ethics violations;
- superior expected returns;
- a causal link between public policy and the trade;
- that the disclosed trade remains open today;
- that the disclosed dollar range equals current exposure;
- that a purchase is an automatic BUY signal or a sale is an automatic SELL signal.

The correct next question is normally: **what publicly observable business, catalyst, valuation, or industry evidence could explain the transaction, and does that evidence independently matter to our thesis?**

If the disclosed security overlaps a current holding or active underwriting, compare it with our existing thesis and price/valuation framework without changing the thesis or posture from the disclosure alone.

## Routing

Every material Pelosi-lane observation still passes the normal five gates and receives one primary route.

Typical routing:

- **P2 / TARGETED EVIDENCE** — new purchase in an existing holding, underwriting, or watchlist name where the disclosure creates a useful research question but proves no economics.
- **P1 / RWC NOW** — rare; reserve for unusually material, option-specific, or catalyst-adjacent disclosures where an independent public-information hypothesis could materially affect an active thesis and warrants immediate testing.
- **P3 / CONTEXT** — interesting disclosed trade with weak portfolio linkage or low decision relevance.
- **REJECT / DUPLICATE** — recycled social post, already-recorded PTR, or unverified claim with no official filing.

`Underwriting Required?` should normally be `NO` or `CONDITIONAL — AFTER RWC`. A Pelosi disclosure by itself is never sufficient for `YES — NEW FULL UNDERWRITING`.

## Visible lane status

The lane is permanently visible under `Specialized lanes` and uses exactly one status:

- `UPDATE — <new official disclosure and compact portfolio/thesis relevance>`
- `NO UPDATE — official House disclosure sources were checked and no new decision-relevant Pelosi transaction filing was found since the prior successful run`
- `UNAVAILABLE — official disclosure source could not be checked reliably enough to determine whether a new filing exists`

A material transaction that is already in the lead Priority table should be cross-referenced here in one sentence rather than repeated in full.

## Minimum visible UPDATE format

When a new official transaction is decision-relevant, the compact lane sentence should preserve:

```text
transaction date | disclosed/filing date | owner | ticker/asset | purchase/sale/exercise | amount range | option terms when applicable | overlap/route
```

Example structure only:

`UPDATE — Pelosi household disclosure: spouse purchased [asset] on [trade date], disclosed [filing date], $[official range]; [option terms if any]. Overlaps [holding/underwriting]; route [P2/RWC/etc.].`

Do not show invented exact dollar amounts or inferred present-day position size.

## Persistence and deduplication

When persistence is supported, record:

- filing ID;
- official filing URL;
- filing/publication date;
- transaction row identity;
- transaction date;
- owner code;
- asset/ticker/type;
- transaction type;
- disclosed amount range;
- option details;
- disclosure lag;
- overlap mapping;
- detection status;
- five gates;
- route;
- underwriting requirement;
- next research question.

Deduplicate primarily by **official filing ID + normalized transaction row**. An amended filing should update/link the prior event rather than create a false independent trade.

## Hard boundary

This lane tracks publicly disclosed congressional transactions for research purposes. It does not provide political advocacy, accuse any filer of misconduct, place trades, or recommend mirroring a politician's portfolio. Any investment action still requires the normal RWC -> Full Underwriting / Event-Trade Underwriting -> Portfolio Capital Allocation workflow.
