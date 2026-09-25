# Event Reaction — mechanical system, trigger alerts only

Strategy separation approved September 21, 2026; reporting revised September 25, 2026. Event Reaction is a separate mechanical system, not Core or Camillo underwriting. **Do not print a recurring Event Reaction table in Radar, synthesis or the standing current view. Surface only a verified actionable trigger, with the limited urgent operational-risk exception below.**

## Authoritative rules and identity

Read the current Investor repository config/strategy-manifest.json, strategy_id event_reaction and its actual aliases such as post_earnings, plus the applicable frozen live lot/engine state. Do not infer membership from a ticker, instrument, old report or remembered position. Same-issuer non-ER holdings/cases remain separate.

The strategy engine / Strategy Desk owns entry qualification, capacity and mechanical event evaluation. Reporting does not change its trading rules, monitoring frequency, notifications, accepted thresholds, executions or lot state. Prefer verified native engine events. A read-only fallback check must use the applicable manifest, exact instrument and sufficient confirmed entry/position/session data; no new mechanics may be invented to fill a report.

## No-underwriting override

Ordinary mechanical stop, partial-profit, runner and maximum-hold exits have **Underwriting Required? = NO**. Do not route them to RWC, Full Underwriting, Event-Trade Underwriting or Portfolio Capital Allocation solely to honor the frozen strategy. A company valuation, thesis, concentration or opportunity-cost argument cannot replace the lot's frozen exit rule. Company news can still support separate Core/Camillo research without converting this lot.

An operational ambiguity, corporate action, halt or missing field is mechanics/data work, not fundamental underwriting. Keep ordinary unresolved diagnostics in internal records; do not publish a daily ER DATA NEEDED or HOLD table. Only a concrete newly material operational failure threatening an established protection or timely action may warrant the existing exceptional risk-alert channel. No all-clear is implied by omitting the routine table.

## Existing dated baseline — not a new rule

As recorded September 21, the manifest baseline was: stop 10% below confirmed entry; partial profit at +12.5% selling 85%; runner target +15% on the remainder; maximum hold 30 trading sessions; after the actual partial fill the remaining lot follows the stop/runner/time rule; conservative stop-first ordering applied to historical/exact-shadow daily bars with both levels touched. Preserve this as dated context, not a live substitute for the applicable engine/manifest rules.

For that dated baseline only, entry E implies stop E×0.90, partial target E×1.125 and runner E×1.15. Use confirmed fill/date and actual remaining quantity/partial-sale state. Display rounding cannot change an unrounded rule comparison. Do not use calendar days for a trading-session deadline, underlying USD for a CAD or option trigger, an analyst stop, event-day low, stale quotes or inferred execution. If a field is missing, record it internally and resolve it before asserting a trigger. Ambiguous stop/target ordering follows the engine/manifest, not a reporter's favourable assumption.

## When an alert is eligible

Allowed existing triggered actions are **ER STOP SELL**, **ER PARTIAL TARGET SELL**, **ER RUNNER TARGET SELL** and **ER TIME EXIT**. A valid native event or sufficiently verified read-only evaluation must establish an actual applicable trigger and its occurrence/lot identity. Mere proximity, unrealized P&L, a projected target, approaching time limit, held status, or a changed quote with the same old trigger is not an alert.

A previously unseen still-actionable trigger can be surfaced as late detection with its original time. A documented target touch between scans may qualify even if the price has since moved, only when the native event or reliable time/price evidence and current execution state establish that it remains an actionable event under the strategy. Do not require the latest spot price alone or invent an intraday crossing from incomplete bars. A filled/closed event is not an instruction to sell again.

Alert text: **Event Reaction alert — [security / exact lot]: [rule hit].** State trigger level or actual due-session condition, observed price/time and source cutoff, manifest-required action/eligible quantity if known, and whether execution is pending or confirmed. Quantity must come from actual state, not a guessed original position. A partial target does not establish that the partial was filled; no runner sale based solely on an earlier recommendation.

Keep the alert compact. Do not attach the entire sleeve's entry/stop/target table, quiet holdings, near-target rows or a routine 'No targets hit' heading. Do not duplicate ER rows in the Core/Camillo monitor queue. The same ticker's independently verified non-ER case can remain in that queue.

## Deduplication, urgency and closeout

Use native event/condition occurrence plus exact strategy/lot/instrument identity, and preserve original detection time and linkage across Radar, Portfolio Defense, the Journal and any readable authoritative alert channel. Do not key a fresh alert solely to each new quote or scheduled slot. A reported unresolved trigger remains one pending item in the standing Decision List, not a new full alert every report. A new runner/stop/time event, material correction or verified worsening execution risk can be surfaced with its linkage; a minor wording or timestamp change cannot.

Publication/delivery state is separate from execution/consumption/re-arm state. Do not mark filled, closed, consumed or re-armed merely because the alert was saved or shown. If delivery is unknown, preserve that uncertainty and use existing bounded delivery reconciliation; avoid flooding unchanged messages. Store new reporting metadata only in supported fields or the authorized Journal, not invented native API keys.

The unified Radar checks/reconciles events at 08:00, 11:00 and 15:00 Toronto. Existing independent mechanical-system/broker alerts remain untouched; these scans are not continuous tick monitoring. An already verified urgent hit may use an existing Action Alert rather than waiting for the next report when execution risk warrants it. No new polling task or notification channel is created by this contract.

The user/broker executes; Investor Holdings records actual fills; partial close remains partially closed and its real remainder keeps the mechanical rules. Supported closeout/postmortem preserves fill, quantity, date and strategy lineage. Reporting does not alter strategy evaluation or place orders.

## Regression checks

No-trigger, ER HOLD, near-target and ordinary data-needed cases produce no recurring ER section. Each verified new trigger can surface once; an old unfilled event does not re-fire merely because another slot runs. Executed partials are not repeated; new runner events remain independently eligible. Exact lots and same-issuer Core/Camillo expressions stay separate. Trading-session rules, actual manifests/quotes and broker-confirmed state remain authoritative. No automatic trade, new underwriting gate, inferred fill or changed strategy threshold.
