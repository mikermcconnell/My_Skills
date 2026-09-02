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

## Required run sequence

Use this order on every run:

1. Read the canonical live monitor source.
2. Dynamically enumerate all records that are currently active and price-bearing.
3. Resolve each security's ownership state when available, active thresholds/ranges, stored downstream actions, monitor identifier/status, trigger-consumed state, and re-arm rules.
4. Retrieve the freshest reliable market price for the dynamically resolved security set as of the Radar cutoff.
5. Mechanically determine which active trigger/action is currently the **next valid action** for each security. Respect consumed and re-arm state; a previously reviewed trigger must not remain actionable merely because price remains beyond it.
6. Collapse the visible output to **one row per security**. Preserve all underlying thresholds in monitor/audit state, but show only the highest-priority currently valid action or next valid trigger in chat.
7. Sort the visible table by user action/urgency using the controlled order below.
8. Record monitor-state and quote `as_of` timestamps when supported.

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
8. **UNAVAILABLE** — required monitor membership/threshold/action/ownership/quote state cannot be resolved reliably. `What to do`: no price-monitor action from stale or guessed data.

Within the same visible action bucket, sort by proximity/severity when mechanically meaningful, then ticker alphabetically as a stable tie-breaker.

### Selecting the one visible trigger per security

- When multiple triggers are crossed, show the **highest-priority currently valid action**, not multiple rows.
- For nested buy/add levels, a deeper valid `compelling` threshold supersedes an ordinary entry/add threshold in the visible row.
- For a security with both downside buy/add triggers and upside trim/valuation-gap triggers, show whichever valid action is actually active; otherwise show the closest **next valid** trigger.
- A consumed trigger is not active until its canonical re-arm condition is satisfied. If a consumed threshold remains below/above the current price but has not re-armed, skip it and evaluate the next valid trigger.
- Do not infer re-arm logic. If canonical state does not reveal whether a previously triggered action is consumed/re-armed and that ambiguity changes the visible action, mark the relevant status `UNAVAILABLE` or explain the ambiguity compactly.
- If ownership is unavailable, do not guess `BUY` versus `ADD`; use `BUY/ADD REVIEW NOW` or `COMPELLING BUY/ADD REVIEW`.

## Freshness and failure behavior

The canonical price-monitor state is the source of truth for **membership, target/trigger, ownership-linked action, consumed state, re-arm state, and downstream workflow**. Market-data sources are the source of truth for **current price**.

If the live canonical monitor source cannot be read, show:

`UNAVAILABLE — live active price-monitor state could not be read`

Do **not** silently fall back to a previous Radar table or stale static monitor list. A stale fallback may be shown only when explicitly useful and must be labelled `STALE FALLBACK` with its original timestamp; it must never be presented as current monitor state or used to issue `BUY/ADD/TRIM/EXIT REVIEW NOW`.

If the monitor source is readable but one quote is unavailable, retain that security row and mark its action/price `UNAVAILABLE` when the trigger comparison cannot be made.

If the monitor source is only partially readable, clearly label the table `PARTIAL` and never imply completeness.

If the canonical source confirms there are no active price-bearing monitors, show `NO ACTIVE PRICE MONITORS`.

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
- market-price source and quote timestamp;
- mechanically determined crossed/near/not-crossed state;
- selected visible action and selected next valid trigger;
- unavailable or partial state.

Persisted snapshots are audit history only. They are **never** the source of truth for the next run when the live canonical monitor source is readable.
