# Sell Discipline and Position Closeout

Use this contract for the master sell check and whenever Portfolio Defense identifies a possible `TRIM`, `EXIT`, option roll, or other reduction in an owned News Radar or ChrisCamillo position.

## Purpose

Close the loop between the original investment case, current portfolio state, a reviewable sell decision, the broker-confirmed sale recorded in Investor Holdings, and the realized result.

The lifecycle is:

`OPEN -> REVIEW_DUE -> SELL_PROPOSED -> PARTIALLY_CLOSED | CLOSED -> POSTMORTEM_COMPLETE`

These are decision and record states. They are not broker order states.

## Authority and boundaries

- MikeInvestor is canonical for live ownership, issuer exposure, instrument detail, research lineage, underwritings, proposals, triggers, and position closeouts.
- News Radar detects new risk, evidence decay, strategy deadlines, and review triggers. It does not make the final security or sizing decision.
- Research With Confidence verifies disputed facts, causality, company-thesis impact, and whether the problem belongs to the company or only the instrument.
- Full Underwriting determines security posture and supplies the target-weight estimate.
- Portfolio Capital Allocation remains the final sizing, funding, account, tax, hedge, and implementation gate.
- The user and broker execute the trade. ChatGPT must never place an order.
- Investor Holdings records the actual sale and creates the owned `closedPositionId`.
- MikeInvestor may reconcile that existing closed-position record to research lineage. It must not fabricate a fill or change a holding.

A price or time trigger starts a review. It is not an automatic sale unless a separately authorized strategy contract explicitly says the rule is mechanical. Event Reaction / post_earnings is such a mechanical strategy for its frozen stop, partial-profit, runner-target and maximum-hold exits; apply the strategy exception below.

## Mechanical-strategy exception — Event Reaction

The generic sell-decision sequence below does **not** apply to ordinary exit mechanics for positions explicitly tagged to Investor strategy_id `event_reaction` or a current alias such as `post_earnings`.

For those lots, read the current Investor `config/strategy-manifest.json` and `event-reaction-strategy-mechanics.md`. The strategy manifest is authoritative for the frozen exit rules. As of September 21, 2026:

- stop loss = 10% below confirmed entry fill;
- +12.5% target = sell 85%;
- +15% runner target = sell the remaining 15%;
- maximum hold = 30 trading sessions;
- the remaining runner is also subject to the strategy stop and time exit.

A valid ER STOP SELL, ER PARTIAL TARGET SELL, ER RUNNER TARGET SELL, or ER TIME EXIT does **not** require RWC, Full Underwriting, Event-Trade Underwriting, or Portfolio Capital Allocation solely to execute the frozen strategy mechanic. It is not a company-thesis sell decision. The user/broker still executes; Investor Holdings still supplies the authoritative confirmed sale and closeout lineage.

If the same issuer has another non-Event-Reaction holding, apply the normal sell discipline to that separate expression. If the Event Reaction strategy data are missing or a trading halt/corporate action prevents reliable application, use ER DATA NEEDED / ER MECHANICS REVIEW rather than route to fundamental underwriting.

News Radar may still report material issuer news, but that news does not override the frozen Event Reaction lot mechanics unless the strategy contract itself contains a corresponding rule.

## Mandatory sell-check coverage

Run the sell check for every owned issuer and every exact instrument, with priority for News Radar and ChrisCamillo strategy positions.

Check these independent reasons:

1. `TARGET_REACHED` — the recorded profit-taking or event-completion condition has occurred.
2. `VALUATION` — expected return no longer clears the hurdle even though the company thesis may remain intact.
3. `THESIS_BREAK` — a load-bearing company claim or kill criterion failed.
4. `TIME_STOP` — the expected selling date or maximum hold expired without enough confirming evidence.
5. `CONCENTRATION` — issuer, factor, correlated, wrapper, or account exposure exceeds the approved risk budget.
6. `INSTRUMENT_FAILURE` — option expiry, strike, theta, implied volatility, assignment, call-away, leverage, or catalyst timing makes the instrument unsuitable even when the company remains attractive.
7. `OPPORTUNITY_COST` — expected return, confidence, or time-to-resolution is inferior to a credible alternative.
8. `OTHER` — use only with an explicit rationale that does not fit the controlled reasons.

For each candidate state:

- company thesis: `INTACT | IMPROVED | DETERIORATED`;
- security/instrument posture;
- current issuer exposure and exact lots/instruments;
- triggered rule and source;
- current price and as-of time when price-dependent;
- expected selling date, elapsed holding period, and next decision date;
- evidence required to hold, trim, exit, roll, or re-underwrite;
- proposed action: `HOLD | TRIM | EXIT | HEDGE`;
- whether RWC, Full Underwriting, or Portfolio Capital Allocation is required first.

Do not treat a company problem, security valuation problem, portfolio sizing problem, and option-timing problem as interchangeable.

## Decision and persistence sequence

1. Read `get_investor_context` and retain `stateVersion`.
2. Read `get_security_context` for each actionable issuer and reconcile issuer-level exposure to exact instruments.
3. Reuse the existing event when the same underlying condition is already open. Otherwise create one deterministic Portfolio Defense `eventId`.
4. Route factual uncertainty to RWC, security/valuation uncertainty to Full Underwriting, and concentration/account/implementation questions to Portfolio Capital Allocation.
5. If the resulting action is `TRIM` or `EXIT`, create only a `PROPOSED` trade proposal. Never mark it accepted or executed.
6. The user executes at the broker and records the confirmed sale through Investor Holdings. This creates the authoritative transaction and `closedPositionId`.
7. Only after that owned closed-position record exists, call `record_position_closeout` when the tool is discovered and authorized. Supply the matching `eventId`, `proposalId`, `closedPositionId`, ticker, controlled exit reason, rationale, evidence references, and fresh `stateVersion`.
8. Re-read MikeInvestor. Confirm the closeout is visible and the residual position is correct.
9. For a partial close, keep the residual exposure under review and reset its next review, target, invalidation, and time-stop as needed.
10. For a full close, append a `DECISION` research result containing the postmortem. Preserve the original thesis and decision history.

`record_position_closeout` is idempotent for the same event and closed-position record. A retry must return the prior closeout rather than create a duplicate.

If `record_position_closeout` is not present in tool discovery, report `CLOSEOUT_PERSISTENCE_UNAVAILABLE`. Do not claim the strategy position is closed merely because a recommendation was issued or the user said an order was submitted.

## Partial exits, options, and rolls

A partial sale is `PARTIALLY_CLOSED`, not a completed thesis. Record the realized slice and continue monitoring the remaining issuer and instrument exposure.

For options:

- closeout performance uses the actual contract multiplier, premium/cost basis, sale price, and closed-position record;
- company thesis and instrument thesis remain separate;
- an option roll is an `EXIT` or `TRIM` closeout for the old contract plus a separate `START` or `ADD` proposal for the new instrument;
- never net the old and new contracts into one synthetic fill or hide realized loss in the replacement cost basis;
- assignment, exercise, or expiry must use the relevant Holdings workflow before closeout reconciliation.

## Performance and postmortem

For News Radar, compare realized return with the strategy pace:

`target return % = ((1 + 0.02) ^ (invested calendar days / 30) - 1) * 100`

Count a same-day position as one invested day. Keep this benchmark separate from the security-specific target price and from portfolio-level opportunity cost.

A full-close postmortem must record:

- original event and thesis;
- original entry, target, invalidation, expected selling date, and sizing rationale;
- actual exit reason, price, quantity, date, holding days, realized return, and CAD result when relevant;
- whether the strategy benchmark was met;
- what the process got right and wrong;
- whether evidence, sizing, instrument choice, timing, or execution caused the outcome;
- one reusable lesson and any monitoring-rule change proposed for review.

Do not rewrite the original event, underwriting, or proposal after the outcome. Append the closeout and postmortem.

## Required sell-check output

| Priority | Ticker | Company thesis | Instrument posture | Current exposure | Trigger | Proposed action | Gate | Next date |
|---|---|---|---|---:|---|---|---|---|

Then report:

- `Open sell reviews`
- `Proposed trims/exits`
- `Broker-confirmed sales awaiting closeout reconciliation`
- `Partial closeouts with residual exposure`
- `Full closeouts awaiting postmortem`
- persistence status

A valid run may conclude `NO SELL ACTION`, but only after every active owned security and instrument was checked.
