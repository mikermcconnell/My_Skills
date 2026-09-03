# Price Monitor Live-Source Contract — News Radar V3

This contract is authoritative for the `Price Monitor Check` specialized lane. It defines both the dynamic source-of-truth behavior and the visible action-queue presentation. **If any other V3 file contains older/conflicting Price Monitor table wording, this contract controls the Price Monitor lane.**

## Source-of-truth rule

At the start of **every scheduled Radar run**, query the live canonical price-monitor / underwriting-monitor state available to that run and enumerate the active price-bearing monitors **from that source at run time**.

Do not:

- hard-code tickers, thresholds, targets, or actions inside News Radar;
- use the prior Radar price table as the current monitor list;
- carry forward a removed or disabled monitor merely because it appeared on an earlier run;
- omit a newly added monitor because it was absent from an earlier Radar run;
- cache a threshold, action, consumed-state, or re-arm state after the canonical monitor has changed it;
- substitute remembered underwriting levels, analyst targets, disabled legacy tasks, or a locally reconstructed list for readable live monitor state.

A monitor added, removed, activated, disabled, re-armed, consumed, or edited in the canonical price-monitor system must therefore flow automatically into the **next Radar run** without a News Radar skill edit.

## Separate monitor state from quote state

Treat these as **two independent data planes**:

1. **Canonical monitor state** owns membership, active/inactive status, ownership, thresholds/ranges, stored downstream actions, consumed-trigger state, re-arm logic, kill/re-underwrite state, and monitor identifiers.
2. **Market-price state** owns the current or latest reliable security price, currency, market session, timestamp, and quote provenance.

Failure of one plane must **not erase readable data from the other plane**.

Examples:

- If a fresh NVDA quote is readable but its canonical trigger/re-arm state is not, show the fresh NVDA price and mark only `Action`, `Next trigger`, or `What to do` as unavailable as appropriate.
- If canonical trigger state is readable but the current quote cannot be retrieved reliably, preserve the stored trigger in `Next trigger`, mark `Current price` unavailable, and do not activate an action that requires a price comparison.
- If ownership alone is unavailable but the trigger/action is otherwise readable, preserve the price and trigger and use ownership-neutral `BUY/ADD` wording rather than suppressing the row.
- Do not use `UNAVAILABLE` as a blanket substitute for a price that was successfully retrieved.

The visible row should expose the **smallest unavailable field**, while the row-level `Action` remains `UNAVAILABLE` whenever the unresolved field prevents a reliable trigger/action determination.

## Required run sequence

Use this order on every run:

1. Read the canonical live monitor source.
2. Dynamically enumerate all records that are currently active and price-bearing.
3. Resolve each security's ownership state when available, active thresholds/ranges, stored downstream actions, monitor identifier/status, trigger-consumed state, and re-arm rules.
4. Retrieve the freshest reliable market price for the dynamically resolved security set as of the Radar cutoff using the quote-source hierarchy below.
5. Apply the near-trigger / crossed-trigger confirmation rule when required.
6. Mechanically determine which active trigger/action is currently the **next valid action** for each security. Respect consumed and re-arm state; a previously reviewed trigger must not remain actionable merely because price remains beyond it.
7. Collapse the visible output to **one row per security**. Preserve all underlying thresholds in monitor/audit state, but show only the highest-priority currently valid action or next valid trigger in chat.
8. Sort the visible table by user action/urgency using the controlled order below.
9. Record monitor-state and quote `as_of` timestamps plus quote source/provenance when supported.

## Quote-source hierarchy

The purpose of the quote hierarchy is to maximize reliable price coverage **without weakening trigger-state controls**. Use the best current source actually accessible during the run; do not declare a quote unavailable merely because one preferred website/feed failed.

### Tier 1 — direct / consolidated / official market data

Prefer a direct market-data tool, exchange feed, consolidated tape, or official exchange quote when it provides a current timestamped price for the exact instrument.

Examples include:

- U.S. consolidated or exchange-backed quote feeds;
- official Nasdaq / NYSE / CBOE-backed market data when surfaced through an accessible provider;
- TMX / TSX / TSXV official market data for Canadian listings;
- Euronext or the relevant official exchange for European listings;
- another official listing venue for securities outside those markets.

A single high-quality Tier 1 quote may be sufficient for ordinary `NO ACTION` rows when the security is not near a trigger and the instrument mapping is unambiguous.

### Tier 2 — preferred high-quality quote aggregator

For **U.S.-listed equities**, prefer **StockAnalysis** when Tier 1 direct tooling is unavailable and StockAnalysis exposes a same-day timestamped quote. Preserve whether the page identifies the observation as real-time versus delayed/consolidated-tape data when available.

StockAnalysis is a preferred practical fallback because it commonly exposes same-day U.S. quotes with timestamps and identifies underlying CBOE / Nasdaq UTP provenance. It is **not** the canonical source for monitor membership or trigger state.

For non-U.S. securities, prefer a comparable high-quality local-market source that clearly resolves the exact instrument, currency, market session, and quote timestamp.

### Tier 3 — reputable secondary market source

If Tier 1 and Tier 2 are unavailable or incomplete, use a reputable secondary provider such as Investing.com, MarketScreener, or another established market-data source when it clearly identifies the correct instrument and provides a sufficiently current quote.

For Canadian or international small-cap securities where coverage is fragmented, cross-check exchange, symbol, currency, and timestamp carefully before using the price.

### Tier 4 — search/news snippets only as last resort

Search-result snippets, news articles, or other indirect price references are last-resort context only.

Do not use an unverified snippet or stale article price to activate a current `BUY/ADD`, `TRIM`, `EXIT`, `GETTING CLOSE`, or `RE-UNDERWRITE` price action. If only indirect/stale evidence exists, show the best known price with its original timestamp only when useful and label it clearly as stale/indirect.

## Near-trigger and crossed-trigger confirmation

Apply stricter quote verification whenever the price could change the user's action queue.

A security requires **confirmation** when:

- the first retrieved price is within **5%** of the next valid price trigger;
- the first retrieved price appears to have crossed any valid buy/add, compelling, trim, exit, kill, or other price-based review trigger;
- the price move is large enough that stale or mis-mapped data would materially change classification;
- the instrument, share class, listing venue, currency, or market session is ambiguous.

Confirmation standard:

- Prefer **two current observations from differentiated market-data sources**, or
- one clearly timestamped direct/consolidated/official Tier 1 quote whose instrument mapping is unambiguous.

When using two sources, they need not be economically independent data-generators, but they should be sufficiently differentiated to detect a stale page, symbol mismatch, currency error, or bad cached observation. Preserve both sources/timestamps in audit state when practical.

If sources disagree materially enough to change the trigger classification:

- do not average them;
- investigate instrument, currency, timestamp, session, split/corporate-action, and delayed-feed differences;
- keep the best-supported current price visible if one is clearly superior;
- mark the action `UNAVAILABLE` when the disagreement cannot be resolved reliably before cutoff.

## Visible action queue

The visible table is:

| Action | Stock | Current price | Next trigger | What to do |
|---|---|---:|---:|---|

The table is an **action queue**, not a raw dump of every stored threshold.

### Controlled visible actions and sort order

Sort from highest to lowest urgency:

1. **RE-UNDERWRITE NOW** — a canonical re-underwrite, kill, or equivalent material review trigger is active. `What to do`: run the required underwriting refresh before any portfolio action.
2. **EXIT REVIEW NOW** — a valid stored exit/kill-price workflow has been triggered. `What to do`: refresh thesis/kill criteria and advance to exit decision only if the downstream review confirms it.
3. **TRIM REVIEW NOW** — a valid stored valuation/trim trigger has been crossed. `What to do`: refresh valuation and advance to trim review only if the downstream review confirms the valuation gap has closed.
4. **COMPELLING ADD REVIEW** / **COMPELLING BUY REVIEW** — the most attractive stored buy/add threshold is currently valid and crossed. Use `ADD` for an owned security, `BUY` for a confirmed unowned security, and `BUY/ADD` if ownership is unavailable. `What to do`: refresh underwriting immediately; if the thesis and threshold remain valid, advance to capital-allocation review. This is **not an automatic purchase**.
5. **ADD REVIEW NOW** / **BUY REVIEW NOW** — a normal stored buy/add/entry threshold is currently valid and crossed. Use ownership-sensitive wording as above. `What to do`: refresh underwriting; if thesis/valuation remain valid, advance to capital-allocation review. This is **not an automatic purchase**.
6. **GETTING CLOSE** — no action trigger is crossed, but price is within **5% of the next valid price trigger** by default. `What to do`: watch; no underwriting or portfolio action yet. The 5% band is a Radar display rule only and does not change the canonical monitor.
7. **NO ACTION** — no valid trigger is crossed and price is not within the 5% proximity band. `What to do`: wait.
8. **UNAVAILABLE** — required state cannot be resolved reliably enough to determine the action. `What to do`: no price-monitor action from stale or guessed data.

Within the same visible action bucket, sort by proximity/severity when mechanically meaningful, then ticker alphabetically as a stable tie-breaker.

### Selecting the one visible trigger per security

- When multiple triggers are crossed, show the **highest-priority currently valid action**, not multiple rows.
- For nested buy/add levels, a deeper valid `compelling` threshold supersedes an ordinary entry/add threshold in the visible row.
- For a security with both downside buy/add triggers and upside trim/valuation-gap triggers, show whichever valid action is actually active; otherwise show the closest **next valid** trigger.
- A consumed trigger is not active until its canonical re-arm condition is satisfied. If a consumed threshold remains below/above the current price but has not re-armed, skip it and evaluate the next valid trigger.
- Do not infer re-arm logic. If canonical state does not reveal whether a previously triggered action is consumed/re-armed and that ambiguity changes the visible action, keep any reliable current price visible but mark the action and/or next-trigger state `UNAVAILABLE` and explain the ambiguity compactly.
- If ownership is unavailable, do not guess `BUY` versus `ADD`; use `BUY/ADD REVIEW NOW` or `COMPELLING BUY/ADD REVIEW` when the underlying trigger itself is valid and readable.

## Visible unavailable-state rules

`UNAVAILABLE` applies to the **decision field that cannot be resolved**, not automatically to every cell in the row.

Use these patterns:

### Fresh price available; trigger/re-arm unavailable

```text
| UNAVAILABLE | NVDA | $229.45 at 15:25 ET | Trigger/re-arm unavailable | Current price is readable; no monitor action until canonical trigger state resolves |
```

### Trigger readable; quote unavailable

```text
| UNAVAILABLE | XYZ | UNAVAILABLE | <=$50 BUY review | Trigger is readable; no comparison/action until a reliable current quote is retrieved |
```

### Ownership unavailable; trigger and quote readable

```text
| BUY/ADD REVIEW NOW | XYZ | $49.20 at 14:40 ET | <=$50 entry review | Refresh underwriting; if still valid, advance to capital-allocation review; ownership unresolved |
```

### Whole monitor source unavailable

If canonical monitor membership itself cannot be read and no other canonical active-monitor source is available, show:

`UNAVAILABLE — live active price-monitor membership/state could not be read`

Do **not** reconstruct the active monitor universe from a prior Radar table merely to populate rows.

## Freshness and failure behavior

The canonical price-monitor state is the source of truth for **membership, target/trigger, ownership-linked action, consumed state, re-arm state, and downstream workflow**. Market-data sources are the source of truth for **current price**.

Do **not** silently fall back to a previous Radar table or stale static monitor list. A stale monitor fallback may be shown only when explicitly useful and must be labelled `STALE FALLBACK` with its original timestamp; it must never be presented as current monitor state or used to issue `BUY/ADD/TRIM/EXIT REVIEW NOW`.

For quote retrieval specifically, failure of one provider is **not** enough to declare the price unavailable. Attempt the next appropriate source tier when doing so is practical within the run cutoff.

If a fresh quote exists but monitor trigger/re-arm state is unresolved, **show the quote anyway** and mark only the decision-dependent fields unavailable.

If the monitor source is readable but a quote remains unavailable after reasonable source fallback, retain that security row, preserve any readable trigger, and mark the action unavailable when the trigger comparison cannot be made.

If the monitor source is only partially readable, clearly label the table `PARTIAL` and never imply completeness.

If the canonical source confirms there are no active price-bearing monitors, show `NO ACTIVE PRICE MONITORS`.

At **08:00**, use reliable pre-market pricing when available; otherwise use the latest regular-session close and label it `prev. close`.

At **11:30** and **15:00**, prefer actual same-day regular-session pricing and preserve the quote as-of time. Do not substitute stale pre-market pricing when a regular-session quote can be obtained.

## Instrument and currency validation

Before using a quote for trigger classification, verify when relevant:

- ticker and company/security identity;
- share class;
- primary or intended listing venue;
- quote currency;
- ADR/CDR/wrapper versus local ordinary share;
- split or other corporate action;
- regular-session versus pre/post-market session.

If instrument mapping is unresolved, a price for a different listing is not a valid substitute for a canonical trigger denominated on another instrument/currency.

## Trigger behavior and action boundary

The visible action is a translation of the canonical monitor into a clear user decision queue; it is **not** permission to trade.

A crossed price trigger activates only the downstream workflow named by the canonical monitor. In particular:

`BUY/ADD PRICE TRIGGER -> refresh underwriting -> if still valid, capital-allocation review -> portfolio decision`

Radar must never translate a price crossing directly into `BUY`, `ADD`, `SELL`, or `TRIM` as an executed instruction. It must use the controlled `... REVIEW` labels above.

A crossed trigger does not by itself change a thesis, fair value, security posture, holding, or portfolio size.

## Persistence

Persist the dynamic monitor coverage snapshot when supported, including:

- canonical monitor source and read timestamp;
- monitor identifier when available;
- active/inactive state used for inclusion;
- ownership state when available;
- all stored thresholds/ranges and downstream actions;
- consumed/re-arm state;
- market-price source, source tier, quote timestamp, session, listing, and currency;
- confirmation source(s) when the security was within 5% of or through a valid trigger;
- any material source disagreement and how it was resolved;
- mechanically determined crossed/near/not-crossed state;
- selected visible action and selected next valid trigger;
- unavailable fields versus row-level unavailable action;
- unavailable or partial monitor state.

Persisted snapshots are audit history only. They are **never** the source of truth for the next run when the live canonical monitor source is readable.
