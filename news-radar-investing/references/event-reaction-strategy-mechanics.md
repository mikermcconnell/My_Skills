# Event Reaction Strategy Mechanics — Radar / Portfolio Defense Override

Approved September 21, 2026. This contract separates the **Event Reaction Drift** strategy from fundamental/security underwriting inside News Radar and Portfolio Defense.

## Source of truth and strategy identity

The authoritative live strategy definition is the Investor repository `config/strategy-manifest.json`, strategy_id `event_reaction`, including its aliases such as `post_earnings`. Read the current manifest when any live position/decision is tagged to that strategy. Do not freeze this file's numeric examples as permanent rules if the strategy manifest later changes them.

A position qualifies for this override only when current live strategy/position state explicitly links it to Event Reaction / post_earnings. Do not infer strategy membership from the ticker, an old report, a remembered trade, or a generic price/volume pattern.

If the same issuer also has a non-Event-Reaction holding, preserve the two strategy expressions separately. The Event Reaction lot follows this mechanical contract; the other holding may still follow normal underwriting/Portfolio Defense rules.

## No-underwriting override

Event Reaction is a **mechanical strategy sleeve**, not a company-underwriting workflow.

For an Event Reaction-tagged position:

- ordinary strategy entry/hold/stop/target/time-exit monitoring does **not** route to Research With Confidence, Full Underwriting, Event-Trade Underwriting, or Portfolio Capital Allocation;
- internal `Underwriting Required?` is `NO` when the only question is whether the frozen Event Reaction mechanics have triggered;
- a price stop, profit target, runner target, or maximum-hold condition must never become `RE-UNDERWRITE NOW`;
- company valuation, fair value, thesis quality, target price, concentration, or opportunity-cost reviews do not replace the strategy's frozen exit mechanics for that lot;
- a material company/news development may still appear in Radar's **New news and opportunities** section, but it does not change the Event Reaction lot's mechanical action unless the Event Reaction strategy contract itself contains a rule for that circumstance;
- if a market halt, delisting, corporate action, data error, or other operational condition prevents the frozen mechanics from being evaluated/executed, use `ER MECHANICS REVIEW` / `DATA NEEDED`, not fundamental underwriting.

The strategy engine / Strategy Desk owns Event Reaction entry qualification and capacity. News Radar does not manufacture Event Reaction entries from news.

## Current frozen exit baseline

Read the current Investor strategy manifest each run. As of September 21, 2026, the authoritative Event Reaction exit block is:

- stop loss: **10% below the confirmed entry fill**;
- partial profit trigger: **+12.5% from confirmed entry**;
- partial sale: **sell 85% of the position** at that trigger;
- runner target: **+15% from confirmed entry** on the remaining 15%;
- maximum hold: **30 trading sessions**;
- after the 85% partial sale, the remaining 15% exits at the +15% runner target, the strategy stop, or the 30-session time exit, whichever valid rule occurs first;
- historical/exact-shadow daily-bar handling uses conservative stop-first ordering when stop and profit levels are both touched on one daily bar.

Do not substitute the event-day low or an analyst/fundamental stop for the manifest's current frozen rule. The production manifest is authoritative even if older prompt prose differs.

## Price calculations

Require a verified confirmed entry fill price and entry date for each live Event Reaction lot.

Using entry fill `E` and the current September 21 baseline only:

- stop price = `E × 0.90`;
- partial target price = `E × 1.125`;
- runner target price = `E × 1.15`;
- time exit = trading session 30 from the actual entry session.

Round display prices only for readability; retain the unrounded calculation in audit state when supported.

If entry price/date, remaining quantity, prior partial-sale state, or current manifest rules are unavailable, do not infer them. Show `ER DATA NEEDED` and the smallest missing field.

## Mechanical action vocabulary

Use these Event Reaction-specific actions instead of generic underwriting-review labels:

1. **ER STOP SELL** — stop condition has triggered; sell the remaining Event Reaction lot under the frozen strategy rule.
2. **ER PARTIAL TARGET SELL** — +12.5% target reached and the baseline partial has not already been executed; sell 85% of the current eligible Event Reaction position under the frozen rule.
3. **ER RUNNER TARGET SELL** — after the partial sale, +15% runner target reached; sell the remaining runner.
4. **ER TIME EXIT** — 30 trading sessions reached; sell the remaining position.
5. **ER HOLD** — no mechanical exit condition currently triggered; continue to the next stop/target/time condition.
6. **ER MECHANICS REVIEW** — operational/corporate-action ambiguity prevents reliable application of the frozen rules.
7. **ER DATA NEEDED** — required live strategy/entry/quantity/rule data are unavailable.

These are strategy instructions for the user's decision/broker workflow, not claims that ChatGPT executed an order. Holdings closeout still requires the authoritative broker/Investor Holdings record.

## Radar display

Inside section 3, **Stock monitor — Buy / Hold / Wait / Sell**, render Event Reaction positions in a distinct subsection before the generic underwriting/defense queue:

### Event Reaction — strategy mechanics

| Action | Stock / lot | Entry | Current | Stop loss | Target sells | Time exit | What to do |
|---|---|---:|---:|---:|---|---|---|

For `Target sells`, show the current manifest rule, e.g. `+12.5%: sell 85%; +15%: sell remaining 15%`, and calculate corresponding prices from the confirmed entry when available.

Do not show Event Reaction stop/target/time-exit rows again in the generic CANONICAL / LEGACY / PORTFOLIO DEFENSE action queue. De-duplicate by exact security + strategy + lot/expression so a separate long-term or other-strategy holding in the same issuer can still appear in the normal queue.

## Monitoring, alerts and closeout

Radar checks Event Reaction mechanics at the normal 08:00, 11:00 and 15:00 Toronto runs using the freshest reliable exact-instrument quote. A mechanical exit that has triggered belongs prominently in that scheduled report; use an exceptional Action Alert only if waiting until the next scheduled Radar output would create material execution risk.

For an Event Reaction close:

- no RWC / Full Underwriting / allocation gate is required solely to honor the frozen strategy exit;
- user/broker executes the trade;
- Investor Holdings records the confirmed sale;
- supported closeout/postmortem uses actual fill/quantity/date and the Event Reaction strategy lineage;
- partial profit remains `PARTIALLY_CLOSED`; the remaining runner stays under the same stop/runner/time-exit mechanics;
- do not mark a strategy position closed from a recommendation, proposed order, or target touch alone.

## Regression checks

Verify during rollout:

- Event Reaction-tagged positions never receive `RE-UNDERWRITE NOW` merely because stop/target/time rules are near or hit;
- the current manifest, not stale prompts, supplies the mechanics;
- the correct confirmed entry fill/date drives calculated stop/target/time levels;
- an already executed 85% partial is not repeated;
- the remaining runner is 15% only when authoritative state confirms the partial;
- 30 means trading sessions, not calendar days;
- same-ticker non-Event-Reaction holdings remain independently eligible for normal underwriting/defense monitoring;
- news about an Event Reaction issuer can still surface without changing the mechanical strategy action;
- no automatic order, fabricated fill, or strategy-rule mutation occurs.
