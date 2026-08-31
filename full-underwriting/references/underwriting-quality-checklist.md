# Full Underwriting Quality Checklist

Run this before finalizing.

## 1. Security and market anchor

- [ ] Correct ticker, share class, exchange, currency, and underlying asset or cash flow.
- [ ] Current price has an as-of timestamp.
- [ ] Basic and fully diluted shares are distinguished.
- [ ] Cash, debt, leases, and enterprise value are reconciled.
- [ ] Warrants, options, convertibles, royalties, streams, preferred claims, and expected financing are incorporated.
- [ ] Post-financing value per share is used when required.

## 2. Evidence discipline

- [ ] Load-bearing facts use primary or high-quality sources where available.
- [ ] Shared-origin reporting is not counted as independent confirmation.
- [ ] Facts, company claims, independent evidence, consensus, calculations, assumptions, judgments, and unknowns are distinct.
- [ ] Source dates and definitions fit the claim.
- [ ] Important conflicts and missing denominators are disclosed.
- [ ] Evidence confidence is separate from mispricing confidence and investment attractiveness.

## 3. Thesis and priced-in view

- [ ] The underwriting question is explicit.
- [ ] Three to five falsifiable claims use Mechanism -> Metric -> Benchmark -> Falsifier.
- [ ] Variant perception is measurable, not merely good company, large TAM, management quality, or low multiple.
- [ ] The analysis states what today's price appears to imply.
- [ ] The underwritten path is clearly different from the market-implied path.

## 4. Economic engine and valuation

- [ ] The small number of value-driving variables are identified.
- [ ] Historical evidence is connected to future economics.
- [ ] Sector-specific metrics are used.
- [ ] Capital intensity, reinvestment, financing, and dilution are not ignored.
- [ ] Primary valuation fits the business and an independent cross-check is used when practical.
- [ ] Assumptions are visible and the same upside driver is not double-counted.
- [ ] Multiple expansion is separated from fundamental value creation.
- [ ] Disagreement between methods is explained.

## 5. Scenarios, probability, and downside

- [ ] Bear, Base, and Bull are economically different.
- [ ] Bear contains a credible failure mechanism and residual value.
- [ ] Base is not a disguised Bull case.
- [ ] Bull does not stack every upside simultaneously without support.
- [ ] Financing and dilution differ across cases when appropriate.
- [ ] Value per fully diluted share and return from current price are shown.
- [ ] Probabilities are analyst assumptions unless externally implied and total 100% when weighted value is used.
- [ ] Market-implied, break-even, or required probabilities are used when more informative.
- [ ] Positive expected value does not hide unacceptable permanent-loss risk.

## 6. Return hurdle and opportunity cost

- [ ] The user's or strategy's actual hurdle is used when available.
- [ ] An unavailable hurdle is labelled rather than invented.
- [ ] Expected annualized return is compared with the hurdle or a clearly labelled sensitivity.
- [ ] The closest realistic alternative is identified.
- [ ] Risk, confidence, liquidity, duration, correlation, and implementation differences are compared.
- [ ] The conclusion explains why incremental capital belongs here or elsewhere.

## 7. Time-to-resolution

- [ ] Holding period is explicit.
- [ ] Target realization and mandatory re-underwrite dates are calendar dates.
- [ ] The reason and required evidence for each date are stated.
- [ ] Delay risk and the valuation cost of time are discussed.
- [ ] The thesis cannot roll forward indefinitely without renewal.

## 8. Red team and independent challenge

- [ ] The strongest credible case against the thesis is presented.
- [ ] The single strongest disconfirming fact is identified.
- [ ] Management incentives, accounting, competition, regulation, technology, financing, dilution, execution, and concentration are considered where relevant.
- [ ] Takeover or strategic optionality is not required for Base unless independently justified.
- [ ] A Decision-ready INVESTABLE conclusion received an independent challenger pass when available.
- [ ] Material challenger disagreements were reconciled.
- [ ] If no challenger ran, the output says UNCHALLENGED.

## 9. Catalysts, falsifiers, and monitoring

- [ ] Fundamental catalysts, recognition catalysts, and monitoring events are separate.
- [ ] The value-realization path is credible within the horizon.
- [ ] Three to five measurable kill criteria are stated.
- [ ] Price decline alone is not a kill criterion.
- [ ] The next evidence that would upgrade, downgrade, or kill the thesis is named.

## 10. Portfolio handoff

- [ ] Entry condition, expected return, downside, duration, and confidence are included.
- [ ] Liquidity, gap/event risk, financing, factor exposure, correlation, currency, and listing issues are included.
- [ ] Add, trim, and exit evidence are included.
- [ ] Exact size, account, hedge, tax, and execution are left to the portfolio/risk workflow.

## 11. Mandatory cross-chat case persistence

Apply `references/case-record-persistence.md` for every new Full Underwriting and every material re-underwrite, event touchpoint, mandatory renewal, or decision-changing update.

The persistent Library case record is the source of truth; conversational memory and prior chat retrieval are discovery aids only.

Required retrieval behavior before interpreting new evidence:

- [ ] Search for `/Investing/Underwriting/<TICKER>/<TICKER>-current-baseline.md`.
- [ ] If found, read and freeze that baseline before using an older preview, Radar/RWC handoff, monitor, prior chat output, or memory fragment.
- [ ] Read the newest relevant append-only decision log when the question depends on why the baseline changed.
- [ ] Reverify market-sensitive and load-bearing facts rather than treating the persisted baseline as current evidence.
- [ ] If the canonical baseline conflicts with a live monitor, treat the canonical record as authoritative and repair the monitor before finishing when tools permit.

Required write behavior after a material conclusion:

- [ ] Write a new dated append-only decision log at `/Investing/Underwriting/<TICKER>/<TICKER>-decision-log-YYYY-MM-DD[-NN].md`.
- [ ] Create or replace `/Investing/Underwriting/<TICKER>/<TICKER>-current-baseline.md` with the newly authoritative baseline.
- [ ] Preserve the prior decision rather than silently overwriting history.
- [ ] Include enough information in the current baseline for a fresh chat to recover the current thesis status, security posture/readiness, Bear/Base/Bull or selected fair value, probabilities, required-return/hurdle price, thresholds, kill/upgrade criteria, realization date, re-underwrite date, and event-driven accelerators.
- [ ] Keep user-specified assumptions/corrections distinct from independently verified facts.
- [ ] Verify that the persisted current baseline and live monitors agree before finalizing.

Material changes requiring a new decision log and baseline rewrite include changes to thesis status, security readiness/posture, scenario economics/probabilities, fair value, return hurdle/hurdle price, entry/add/compelling/trim/valuation-gap/exit thresholds, kill/upgrade criteria, financing/capital-structure assumptions, target realization, mandatory re-underwrite timing, monitoring-relevant trade expression, or a user correction that changes the authoritative case.

If persistent Library writes are unavailable:

- [ ] Mark `CASE_PERSISTENCE_BLOCKED` explicitly rather than claiming the case was saved.
- [ ] Preserve an exact current-baseline and decision-log artifact in the conversation when possible.
- [ ] Backfill the Library record automatically in the next session where persistent file writes are available before performing a material update.

This case-persistence step is part of completing the underwriting, not optional documentation.

## 12. Mandatory monitor propagation

Before finalizing any Full Underwriting, determine whether the conclusion creates or changes a monitor-worthy state. If it does, synchronize the live monitoring system in the same turn whenever the required task-editing capability is available.

Monitor-worthy state includes any new or changed:

- thesis status or security posture;
- fair value, probability-weighted value, Bear/Base/Bull values, or return framework;
- entry, add, compelling, trim, valuation-gap, or exit-review thresholds;
- kill or deterioration criteria;
- upgrade criteria;
- catalyst or next-evidence triggers that could force earlier review;
- target realization date;
- mandatory re-underwrite date;
- ownership/trade-expression context that changes how the security should be monitored.

Required behavior:

- [ ] If the security already exists in active underwriting monitors, update those monitors automatically before the final response.
- [ ] If the security does not yet have appropriate monitoring and the underwriting ends INVESTABLE, INVESTABLE BUT PRICE-SENSITIVE, or WATCH / WAIT FOR PROOF, create an appropriate live monitor automatically rather than waiting for a separate user request.
- [ ] Prefer integration into the central Daily Trigger Monitor, Weekly Evidence Review, and Re-underwrite Calendar when those are the authoritative monitoring surfaces; create a dedicated condition-watch only when the case benefits from security-specific evidence checks or when central-monitor integration is insufficient.
- [ ] Price alone must never create an automatic buy/sell instruction; price thresholds trigger an underwriting refresh unless the user has explicitly defined another rule.
- [ ] A mandatory re-underwrite date must be represented in the live re-underwrite calendar or an equivalent active task.
- [ ] Event-driven early-review conditions must be carried into the monitoring prompt.
- [ ] When a later re-underwrite changes the baseline, propagate the revised values, thresholds, kill criteria, and next review date into all affected live monitors before finishing.
- [ ] Avoid duplicate active monitors. Check existing tasks first and update or consolidate rather than creating overlapping watches.
- [ ] If task-editing capability is unavailable, do not falsely claim synchronization. State the specific limitation, preserve an exact monitor-update payload in a durable artifact when possible, and apply it automatically in the next session where task editing is available.

This monitor-propagation step is part of completing the underwriting, not an optional follow-up.

## Final decision questions

1. What exactly is mispriced?
2. What does today's price imply?
3. What must be true for Base?
4. Which assumption contributes most to upside?
5. What breaks first in Bear?
6. Is financing and dilution captured?
7. Is return driven by fundamentals, probability, or multiple expansion?
8. What is the strongest evidence against the thesis?
9. What evidence would upgrade or kill it?
10. Does expected annualized return clear the applicable hurdle?
11. Why is this superior to the closest alternative?
12. By what date should the thesis realize and be re-underwritten?
13. Did the independent challenger agree, revise, or fail the conclusion?
14. Did I retrieve and freeze the canonical prior case before interpreting new evidence?
15. Is the newly authoritative current baseline persisted at the canonical Library path with an append-only decision log?
16. Do the live monitors match that persisted baseline, or is synchronization explicitly marked blocked?
17. Could a fresh chat recover the current thesis, valuation, thresholds, kill criteria, and re-underwrite date without relying on memory?
18. Is the security actually investable, or merely interesting?

If the important questions cannot be answered, the underwriting is not Decision-ready.

Choose exactly one final posture: INVESTABLE; INVESTABLE, BUT PRICE-SENSITIVE; WATCH / WAIT FOR PROOF; PASS; or REJECT.
