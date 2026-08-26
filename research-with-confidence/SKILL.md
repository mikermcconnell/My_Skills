---
name: research-with-confidence
description: Independently verify a complex claim or News Radar handoff using source provenance, cross-checking, counterfactual analysis, explicit confidence, and clear stopping rules. Use for deep dives, current claim verification, fact-checking, causal research, or deciding whether a public-equity lead deserves Full Underwriting, Event-Trade Underwriting, targeted research, monitoring, or rejection. Do not use for a quick factual answer, final security valuation, short-duration payoff approval, or account-specific portfolio sizing.
---

# Research With Confidence

Determine what is actually true, what changed, what caused it, how economically material it could be, and what remains unresolved.

For investment leads, RWC is the truth and causality gate between Radar and the appropriate underwriting workflow. It may validate, refine, delay, or reject the original hypothesis. Its job is not to prove the Radar thesis.

## References

Read only what the task needs:

- `references/research-workflow.md` for the general and investment research sequence.
- `references/confidence-and-source-rules.md` for claim ledgers, source independence, and confidence calibration.
- `references/investment-handoff.md` when the output may advance to underwriting.
- `references/clinical-and-biotech-overlay.md` for medical, oncology, clinical, or regulatory research.

## Core rules

- Begin from the research question and raw evidence, not from a desired conclusion.
- Use an existing Radar or user-supplied handoff as a baseline, but independently test its interpretation.
- Distinguish the **underlying event**, the **new information delta**, and the **article or commentary discussing it**.
- Trace important claims to their original source and group dependent reporting under one origin.
- Separate `Fact`, `Company claim`, `Independent evidence`, `Derived calculation`, `Assumption`, `Inference`, and `Unknown`.
- Test a causal thesis against the counterfactual: what likely would have happened without this event?
- Look for confounders and competing explanations before attributing an observed market or operating change to the event.
- Separate evidence confidence, company value-capture confidence, security-mispricing confidence, and short-duration tradeability.
- Preserve uncertainty. Do not manufacture opposing evidence or false precision.
- Stop when the remaining question is principally long-term valuation, scenario modeling, financing, dilution, event payoff, market microstructure, or portfolio construction; hand that work to the appropriate workflow.
- Do not retrieve broad personal, portfolio, or workspace context unless the user requests it, supplies a specific handoff, or that exact context is necessary to answer the stated question.

## Workflow

### 1. Define the decision question

State:

- the exact claim or hypothesis;
- time horizon and relevant geography or market;
- what decision the research should enable;
- what would count as confirmation, refinement, delay, or rejection;
- the information cutoff and current date.

For a Radar handoff, preserve the `event_id`, lane, original hypothesis, prior baseline, delta class, thesis effect, decisive questions, and any frozen catalyst packet.

### 2. Build a claim and source ledger

Break the problem into a small number of load-bearing claims. For each claim record:

- source and date;
- source origin and claim status;
- independence group;
- evidence for and against;
- derived calculations;
- remaining unknowns;
- confidence;
- the next evidence that could change the conclusion.

Do not treat repetition as corroboration. One regulator document or customer datapoint can outweigh many derivative articles.

### 3. Reconstruct the baseline and novelty

Determine:

- what was already known, guided, expected, or plausibly priced before the new item;
- what is genuinely incremental;
- whether the item is repeated guidance, independent confirmation, acceleration/deceleration, contradiction, risk disclosure, cumulative slow-burn evidence, or an unknown delta;
- whether the market had a realistic chance to react;
- when applicable, how the actual result compares with the frozen pre-event packet.

Correct the initial framing explicitly when necessary. A materially revised thesis is a successful RWC outcome.

### 4. Test mechanism, attribution, and counterfactual

Express the proposed mechanism as:

`Event or cumulative delta -> operational or probabilistic variable -> company economics -> observable metric`

Then ask:

- Does the mechanism fit the facts and industry structure?
- What other events could produce the same observation?
- Did the outcome begin before the event?
- Is the evidence measuring cause, correlation, or only a plausible narrative?
- What would likely have happened without the event?
- What observation would distinguish the competing explanations?

Do not attribute price, volume, freight, adoption, trial, or operating changes to the focal event when a stronger confounder is present.

### 5. Determine economic materiality and value capture

Estimate the order of magnitude rather than forcing precision. Identify the variables that could move:

- volume, price, market share, backlog, utilization, or retention;
- margins, productivity, capital intensity, or unit economics;
- free cash flow, debt, financing, dilution, royalties, or asset value;
- clinical, regulatory, legal, transaction, or policy probabilities;
- timing of value realization.

Map:

1. the obvious issuer or beneficiary;
2. a plausible second-order beneficiary or alternative expression;
3. a related company that should not advance because capture is weak or the event is already obvious;
4. potential losers or useful comparators.

High thematic exposure is not the same as material equity sensitivity.

### 6. Perform the expectations check

RWC should determine whether a plausible expectations gap exists without completing the relevant underwriting.

Check:

- prior guidance and known catalyst dates;
- pre-event run-up or selloff;
- contemporaneous price and estimate reaction;
- consensus or common narrative;
- frozen expected versus surprise thresholds when available;
- whether the market appears to have noticed the direct effect but missed duration, second-order consequences, ownership economics, or an attribution error.

State separately:

- confidence that the event or mechanism is real;
- confidence that the identified company captures value;
- confidence that the effect is material;
- confidence that the security may be mispriced;
- for an explicitly short-duration setup, confidence that a still-unconsumed event surprise may exist.

RWC does not calculate the complete long-term valuation or event-trade payoff.

### 7. Red-team the research conclusion

Identify:

- the strongest disconfirming fact;
- the strongest competing explanation;
- the weakest load-bearing assumption;
- evidence that would force a materially different conclusion;
- whether management, sponsor, expert, media, market participant, or researcher incentives may be distorting the interpretation.

Do not add weak negative points merely to appear balanced.

### 8. Apply the stopping rule and route

Choose exactly one primary outcome:

- **ADVANCE -> FULL UNDERWRITING:** mechanism and materiality survive; a plausible medium- or long-term security-level expectations gap exists; valuation, financing, downside, return, and time are now decisive.
- **ADVANCE -> EVENT-TRADE UNDERWRITING:** the user explicitly seeks an hours/days/few-weeks trade around a discrete event; factual verification survives; the remaining questions are event probabilities, payoff, implied expectations, executable price, liquidity, gap, halt, borrow, options, or slippage. Do not use this route for a normal investment thesis.
- **TARGETED RESEARCH:** one or more named evidence items can resolve a load-bearing uncertainty.
- **WAIT FOR DATED EVIDENCE:** a near catalyst or document will provide substantially more information; state the date and do not underwrite stale inputs.
- **MONITOR:** the thesis is credible but currently immaterial, weakly captured, or too early.
- **REJECT:** the premise is false, stale, misattributed, immaterial, uninvestable through public securities, untradeable on the proposed horizon, or already contradicted.

Stop rather than expanding the report when additional work has low expected decision value.

## Output

### Executive verdict

State the route, corrected thesis, evidence confidence, security-mispricing or event-surprise confidence, and one-sentence reason.

### Findings

Use the structure appropriate to the task, but an investment RWC report must include:

1. original hypothesis;
2. corrected hypothesis;
3. genuinely new versus previously known information;
4. primary-source confirmation and source limitations;
5. causal mechanism, counterfactual, and confounders;
6. economic materiality bridge;
7. direct, second-order, non-beneficiary, and loser/comparator map;
8. expectations and price context;
9. strongest challenge;
10. confidence by major claim;
11. unresolved questions and next evidence/date;
12. stopping decision and next gate;
13. exact Full Underwriting question when advancing to investment underwriting;
14. exact event, intended horizon, and remaining payoff/execution questions when advancing to Event-Trade Underwriting.

Use `references/investment-handoff.md` as the contract for an underwriting handoff.

## Boundaries

- RWC does not issue a final `INVESTABLE`, event-trade posture, `PASS`, or position-size decision unless the user explicitly asks for a combined workflow and all requirements of the relevant downstream skill are completed.
- RWC does not restart an existing handoff from zero, but it may overturn its interpretation.
- RWC does not automatically update a Mind Model thesis. It may propose atomic evidence and a probability effect for review.
- RWC does not treat a large TAM, statistically significant result, regulatory approval, strategic investment, partnership, recent stock move, or apparent event surprise as sufficient proof of security-level mispricing or tradeability.
