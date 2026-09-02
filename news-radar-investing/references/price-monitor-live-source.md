# Price Monitor Live-Source Contract — News Radar V3

This contract is authoritative for the `Price Monitor Check` specialized lane. It clarifies that the lane is **dynamic**, not a maintained static ticker list.

## Source-of-truth rule

At the start of **every scheduled Radar run**, query the live canonical price-monitor / underwriting-monitor state available to that run and enumerate the active price-bearing monitors **from that source at run time**.

Do not:

- hard-code tickers, thresholds, targets, or actions inside News Radar;
- use the prior Radar price table as the current monitor list;
- carry forward a removed or disabled monitor merely because it appeared on an earlier run;
- omit a newly added monitor because it was absent from an earlier Radar run;
- cache a threshold or action after the canonical monitor has changed it;
- substitute remembered underwriting levels, analyst targets, or a locally reconstructed list for readable live monitor state.

A monitor added, removed, activated, disabled, or edited in the canonical price-monitor system must therefore flow automatically into the **next Radar run** without a News Radar skill edit.

## Required run sequence

Use this order on every run:

1. Read the canonical live monitor source.
2. Dynamically enumerate all records that are currently active and price-bearing.
3. Resolve each record's security/ticker, stored target/trigger/range, stored action, currency when relevant, and monitor identifier/status.
4. Only after the active monitor set is resolved, retrieve the freshest reliable market price for those securities as of the Radar cutoff.
5. Render the visible table:

| Stock | Current price | Target / trigger | Action |
|---|---:|---:|---|

6. Record the monitor-state `as_of` time and quote `as_of` time when supported.

If one security has multiple active actionable thresholds, show multiple rows unless the canonical monitor explicitly stores them as one range.

## Freshness and failure behavior

The canonical price-monitor state is the source of truth for **membership, target/trigger, and action**. Market-data sources are the source of truth for **current price**.

If the live canonical monitor source cannot be read, show:

`UNAVAILABLE — live active price-monitor state could not be read`

Do **not** silently fall back to a previous Radar table or stale static monitor list. A stale fallback may be shown only when it is explicitly useful and must be labelled `STALE FALLBACK` with its original timestamp; it must never be presented as the current monitor state.

If the monitor source is readable but one quote is unavailable, retain that monitor row and mark only its price `UNAVAILABLE`.

If the monitor source is only partially readable, clearly label the table `PARTIAL` and never imply completeness.

If the canonical source confirms there are no active price-bearing monitors, show `NO ACTIVE PRICE MONITORS`.

## Trigger behavior

Radar reports whether the current price is near, inside, or through a stored trigger when that comparison is mechanically clear, but does not invent a new action or execute the stored action.

A crossed trigger activates only the downstream workflow named by the canonical monitor, such as review, entry review, trim review, exit review, or re-underwrite. It does not by itself change a thesis, fair value, security posture, holding, or portfolio size.

## Persistence

Persist the dynamic monitor coverage snapshot when supported, including:

- canonical monitor source and read timestamp;
- monitor identifier when available;
- active/inactive state used for inclusion;
- target/trigger/range and stored action;
- market-price source and quote timestamp;
- whether the trigger is below/inside/above/crossed when mechanically determinable;
- unavailable or partial state.

Persisted snapshots are audit history only. They are **never** the source of truth for the next run when the live canonical monitor source is readable.
