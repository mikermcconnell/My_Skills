---
name: research-with-confidence
description: Independently verify a complex claim or News Radar handoff using source provenance, cross-checking, counterfactual analysis, explicit confidence, portfolio-aware impact classification, expression/security selection, and clear stopping rules. Use for deep dives, current claim verification, fact-checking, causal research, Portfolio Defense questions, or deciding whether a public-equity lead deserves Full Underwriting, Event-Trade Underwriting, targeted research, monitoring, or rejection. Do not use for a quick factual answer, final security valuation, short-duration payoff approval, or account-specific portfolio sizing.
---

# Research With Confidence

Determine what is actually true, what changed, what caused it, how economically material it could be, what public-market expression best captures the edge, and what remains unresolved.

For investment leads, RWC is the truth, causality, and expression-selection gate between Radar and the appropriate underwriting workflow. It may validate, refine, delay, redirect, or reject the original hypothesis or proposed security. Its job is not to prove the Radar thesis or force the first named stock into underwriting.

## References

Read only what the task needs:

- `references/research-workflow.md` for the general and investment research sequence.
- `references/confidence-and-source-rules.md` for claim ledgers, source independence, and confidence calibration.
- `references/investment-handoff.md` when the output may advance to underwriting.
- `references/expression-selection.md` for sectoral, macro, commodity, regulatory, thematic, cross-company, or other investment theses with multiple plausible tradable implementations.
- `references/clinical-and-biotech-overlay.md` for medical, oncology, clinical, or regulatory research.

## Core rules

- Begin from the research question and raw evidence, not from a desired conclusion.
- Use an existing Radar or user-supplied handoff as a baseline, but independently test its interpretation.
- Distinguish the **underlying event**, the **new information delta**, and the **article or commentary discussing it**.
- Trace important claims to their original source and group dependent reporting under one origin.
- Separate `Fact`, `Company claim`, `Independent evidence`, `Derived calculation`, `Assumption`, `Inference`, and `Unknown`.
- Test a causal thesis against the counterfactual: what likely would have happened without this event?
- Look for confounders and competing explanations before attributing an observed market or operating change to the event.
- Separate evidence confidence, company value-capture confidence, security-mispricing confidence, expression-selection confidence, and short-duration tradeability.
- Preserve uncertainty. Do not manufacture opposing evidence or false precision.
- For sectoral, macro, commodity, regulatory, thematic, cross-company, or other leads with multiple plausible tradable implementations, **complete the Expression / Security Selection Gate before routing any single stock to Full Underwriting**. Compare the relevant stock(s), ETF/ETN/fund or commodity pool, basket, direct underlying/futures, options when timing supports them, and no-trade alternative. State unavailable categories explicitly.
- Never select a stock merely because Radar named it first, it is familiar, it is already owned, or it is easier to underwrite. Identify where the mispricing actually sits: the underlying economic variable, a packaged/direct instrument, the sector, or a specific company's capture and valuation.
- Do not assume an ETF/fund is lower risk. Futures-based funds, commodity pools, ETNs, leveraged/inverse products, and options can introduce roll, basis, path, credit, leverage, liquidity, or wrapper risk.
- Stop when the remaining question is principally long-term valuation, scenario modeling, financing, dilution, event payoff, market microstructure, or portfolio construction; hand that work to the appropriate workflow.
- Do not retrieve broad personal, portfolio, or workspace context unless the user requests it, supplies a specific handoff, or that exact context is necessary to answer the stated question.
- When the question affects an owned security, use MikeInvestor for current exposure and lineage. Treat ownership as decision context, never as evidence that the factual claim is true or false.
- Distinguish company-thesis deterioration from security valuation, portfolio concentration, and instrument/timing failure. A valid company thesis can coexist with a TRIM, EXIT, or option-roll review.

## Registered newsletter handoffs

When Radar advances a specialist newsletter issue, treat the **newsletter as one expert-source origin**, not as a bundle of independent confirmations.

Use the handoff's atomic claims and test only the load-bearing ones. For each material claim:
- identify whether it is externally observable fact/data, proprietary model output, derived calculation, forecast, expert interpretation, or investment hypothesis;
- retrieve independent primary/counterparty/technical evidence when available;
- test the strongest methodological assumption or missing denominator;
- separate technical importance from public-equity value capture;
- compare plausible beneficiaries, losers, and non-beneficiaries rather than defaulting to the source's most obvious ticker;
- determine whether the claim starts/updates an Emerging Signal sequence;
- state what would falsify the source's interpretation.

Do not produce a second full newsletter summary. RWC's output should answer whether the article's load-bearing thesis survives and where the investable mispricing, if any, actually sits.

## Pre-pivotal biotech route

When the user or Radar asks whether a clinical-stage company is investable **before** Phase 3 / pivotal results, read `references/clinical-and-biotech-overlay.md` and explicitly use its pre-pivotal route.

Do not force `WAIT FOR PHASE 3` merely because pivotal efficacy is unresolved. RWC should determine whether prior efficacy, pivotal-design translatability, regulatory alignment, safety, class read-through, supporting de-risking catalysts, financing-to-readout and commercial differentiation make the probability distribution sufficiently underwriteable to test against current market expectations.

If that survives, the correct outcome may be **ADVANCE -> FULL UNDERWRITING — PRE-PIVOTAL SPECULATIVE**. This means the case is ready for probability-weighted security analysis and loss-budget sizing, not that the clinical outcome is likely or that a normal position is appropriate.

Preserve the explicit failure case, next pivotal/de-risking evidence, expected readout window and financing runway in the handoff.

## Workflow

### 1. Define the decision question

State:

- the exact claim or hypothesis;
- time horizon and relevant geography or market;
- what decision the research should enable;
- what would count as confirmation, refinement, delay, or rejection;
- the information cutoff and current date.

For a Radar handoff, preserve the `event_id`, lane, original hypothesis, prior baseline, delta class, thesis effect, decisive questions, and any frozen catalyst packet.

When portfolio impact is in scope, read MikeInvestor's live investor context and the relevant security context before concluding. Record the observed `stateVersion`, issuer exposure, exact instruments, active underwriting, proposal/closeout lineage, and source timestamps. Do the factual analysis independently first; then apply those facts to the live portfolio.

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

### 6A. Separate company, security, and instrument effects

For every owned exposure, classify each layer independently:

- **Company thesis:** `INTACT | IMPROVED | DETERIORATED`.
- **Security:** valuation, expected return, dilution, and what is priced in.
- **Portfolio:** issuer/cluster concentration, account constraints, and opportunity cost.
- **Instrument:** wrapper, strike, expiry, delta, theta, implied volatility, assignment/call-away, liquidity, and catalyst timing.

For options, compare the evidence/catalyst date with expiry and the intended trade horizon. State whether the underlying thesis remains valid but the instrument is timing-mismatched. Never allow a profitable or loss-making option position to bias the factual verdict.

### 6B. Select the best public-market expression

Apply this step whenever the thesis is sectoral, macro, commodity, regulatory, thematic, cross-company, or otherwise has multiple plausible tradable implementations. Use `references/expression-selection.md`.

Compare viable candidates on a common basis:

- **Exposure purity** — how directly the instrument responds to the researched variable.
- **Economic capture** — how much of the thesis reaches the holder after corporate economics, financing, capital allocation, index dilution, or wrapper mechanics.
- **Mispricing / expectations gap** — whether this instrument, not just the theme, underprices the outcome.
- **Idiosyncratic or structural risk** — company, balance-sheet, basis, roll, tracking, counterparty, leverage, liquidity, or wrapper risk unrelated to the core edge.
- **Timing fit** — whether instrument duration matches the evidence-resolution and value-realization window.
- **Liquidity / implementation** — spreads, market depth, borrow, roll costs, accessibility, and practical constraints.
- **Portfolio fit** — existing issuer/theme concentration, overlap, correlation, and account constraints.

When available and relevant, explicitly test:

1. individual stock(s);
2. ETF / ETN / listed fund / commodity pool;
3. a deliberate basket;
4. direct underlying / futures / direct instrument;
5. options only when timing can justify theta/IV/path risk;
6. `NO TRADE`.

Then state:

- **Best direct expression** — or `NONE / UNAVAILABLE`;
- **Best equity expression** — or `NONE / UNAVAILABLE`;
- **Best diversified expression** — or `NONE / UNAVAILABLE`;
- **Chosen expression** — including `NO TRADE` when appropriate;
- **Why it wins** — the edge it captures better than alternatives;
- **Flip condition** — what evidence, price, duration, or structure change would make another expression superior.

Exposure purity alone does not win the gate. A direct instrument may already price the event while an equity underprices duration; conversely, an apparently cheap equity may add management/balance-sheet risk when a cleaner direct instrument better matches the researched edge.

A mandatory expression gate is **incomplete** if it maps only companies and never checks the relevant ETF/fund/direct/basket/no-trade alternatives.

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

- **ADVANCE -> FULL UNDERWRITING:** mechanism and materiality survive; a plausible medium- or long-term security-level expectations gap exists; the selected equity/fund/basket captures enough of the economics; any mandatory expression-selection gate is complete; valuation, financing, downside, return, and time are now decisive.
- **ADVANCE -> EVENT-TRADE UNDERWRITING:** the user explicitly seeks an hours/days/few-weeks trade around a discrete event or short-horizon direct/derivative expression; factual verification survives; the remaining questions are event probabilities, payoff, implied expectations, executable price, liquidity, gap, halt, borrow, futures basis/roll, options, or slippage. Do not use this route for a normal investment thesis.
- **TARGETED RESEARCH:** one or more named evidence items can resolve a load-bearing uncertainty, including unresolved wrapper, roll, basis, liquidity, options, or implementation economics that determine the best expression.
- **WAIT FOR DATED EVIDENCE:** a near catalyst or document will provide substantially more information; state the date and do not underwrite stale inputs.
- **MONITOR:** the thesis is credible but currently immaterial, weakly captured, too early, fully priced across viable expressions, or has no sufficiently attractive implementation yet.
- **REJECT:** the premise is false, stale, misattributed, immaterial, uninvestable through public securities, structurally unattractive to express, untradeable on the proposed horizon, or already contradicted.

Do not route a single stock to Full Underwriting simply because the world thesis survived. When a mandatory expression gate has not been completed, stop at `TARGETED RESEARCH` rather than assuming the equity is the correct vehicle.

Stop rather than expanding the report when additional work has low expected decision value.

## Output

### Executive verdict

State the route, corrected thesis, evidence confidence, chosen expression when the expression gate applies, security-mispricing or event-surprise confidence, and one-sentence reason.

### Portfolio Defense Impact

When an owned issuer or instrument is affected, state exactly one primary impact:

- `NO CHANGE`
- `MONITOR`
- `RE-UNDERWRITE SECURITY`
- `CAPITAL-ALLOCATION REVIEW`
- `TRIM/EXIT EVIDENCE CONFIRMED`
- `INSTRUMENT/TIMING FAILURE`

Then state company-thesis impact, exact affected instruments, current exposure, controlled sell-reason candidate when relevant, and the next decision gate. This is a research verdict, not execution or final sizing.

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
9. **Expression / Security Selection Gate** when mandatory, including candidate comparison, best direct, best equity, best diversified, chosen expression, why it wins, and flip condition;
10. strongest challenge;
11. confidence by major claim;
12. unresolved questions and next evidence/date;
13. stopping decision and next gate;
14. exact Full Underwriting question when advancing to investment underwriting, including the selected security/expression;
15. exact event, intended horizon, and remaining payoff/execution questions when advancing to Event-Trade Underwriting;
16. `Portfolio Defense Impact` and company-versus-security-versus-instrument classification for owned exposure.

Use `references/investment-handoff.md` as the contract for an underwriting handoff.

## MikeInvestor persistence

When the user or scheduled contract authorizes research persistence:

1. reuse the Radar `eventId`;
2. use fresh MikeInvestor context and its observed `stateVersion`;
3. call `save_research_result` with stage `RWC`, ticker, factual verdict, corrected summary, company-thesis impact, economic bridge, expression-selection result when applicable, next question, evidence references, and portfolio context;
4. re-read and verify the result appears in the same security/event lineage.

Persist the evidence verdict even when current ownership creates urgency, but never alter the verdict to justify a desired portfolio action. RWC may confirm evidence supporting a sell-review reason; it may not place a trade, approve a proposal, mutate holdings, or fabricate a closeout. A broker-confirmed closeout follows the News Radar sell-discipline contract.

## Boundaries

- RWC does not issue a final `INVESTABLE`, event-trade posture, `PASS`, or position-size decision unless the user explicitly asks for a combined workflow and all requirements of the relevant downstream skill are completed.
- RWC does not restart an existing handoff from zero, but it may overturn its interpretation or redirect the proposed expression.
- RWC does not automatically update a Mind Model thesis. It may propose atomic evidence and a probability effect for review.
- RWC does not treat a large TAM, statistically significant result, regulatory approval, strategic investment, partnership, recent stock move, apparent event surprise, or high thematic exposure as sufficient proof of security-level mispricing, tradeability, or expression superiority.
