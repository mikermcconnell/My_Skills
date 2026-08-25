---
name: full-underwriting
description: Perform a full buy-side underwriting of a listed company or public security and decide whether it is actually investable at the current price. Use when the user says full underwriting, underwrite this, is this actually cheap, take this from research to investment, or when a Research With Confidence lead needs reverse valuation, capital structure, financing and dilution, scenarios, catalysts, falsifiers, return hurdles, time-to-resolution, and a final Investable, Watch, Pass, or Reject decision. Do not use for first-pass idea generation, news triage, or account-specific sizing.
---

# Full Underwriting

Turn a promising public-equity research lead into a security-level capital decision.

> At the current price, what must be true for this investment to generate an attractive return, how likely is that outcome, how long should it take, what can permanently impair capital, and is it a better use of capital than the available alternatives?

A good company is not automatically a good investment. A correct world thesis is not automatically mispriced.

## Place in the workflow

`News Radar -> Research With Confidence -> Full Underwriting -> independent challenger -> portfolio/risk sizing -> Mind Model / monitoring`

Use an existing RWC handoff as the evidence baseline. Preserve supported findings, challenges, confidence, and unresolved questions, but reverify current price, capital structure, market-sensitive facts, and all load-bearing assumptions. Do not inherit the earlier conclusion uncritically.

## References

Read only what the case needs:

- `references/valuation-methods.md` for primary valuation, reverse valuation, capitalization, financing, and dilution.
- `references/scenario-and-probability-rules.md` for scenarios, probabilities, expected return, and time-to-resolution.
- `references/sector-overlays.md` for sector-specific economics.
- `references/portfolio-handoff-and-hurdle-rules.md` for required-return, opportunity-cost, and portfolio inputs.
- `references/underwriting-quality-checklist.md` before finalizing.

## Core rules

1. **Price and date matter.** Never call a security investable without a current price and as-of timestamp.
2. **Fully diluted economics matter.** Include options, warrants, convertibles, debt, leases, royalties, streams, preferred claims, and expected financing. Use post-financing value per share when the thesis requires capital.
3. **Underwrite the future, not the story.** Historical evidence matters only insofar as it changes future cash flows, probabilities, valuation, or timing.
4. **Separate evidence types.** Distinguish reported facts, company claims, independent evidence, consensus, derived calculations, analyst assumptions, judgment/probabilities, and unknowns.
5. **Variant perception is mandatory.** State what the current price appears to imply and what the underwriting believes is wrong or incomplete.
6. **Downside belongs inside valuation.** Model the failure mechanism and residual equity value; do not append generic risks to a bullish model.
7. **Time is part of return.** Every conclusion requires a holding period, target realization date, and mandatory re-underwrite date.
8. **Opportunity cost matters.** Compare expected annualized return and downside with the applicable hurdle and the closest realistic alternative.
9. **Independence matters.** A decision-ready INVESTABLE conclusion should receive an independent challenger pass when that workflow is available. If it was not run, say so.
10. **Do not force a buy.** PRICE-SENSITIVE, WATCH, PASS, and REJECT are successful outcomes.

## Workflow

### 1. Define the underwriting question

State one sentence containing:

- security, ticker, exchange, and currency;
- current price and date;
- proposed investment horizon;
- primary question;
- current research posture.

### 2. Establish the security and capital structure

Reconcile when material:

- basic and fully diluted shares;
- current market capitalization;
- cash, debt, leases, and enterprise value;
- options, warrants, convertibles, preferred claims, royalties, and streams;
- committed or likely financing;
- post-financing share count and value per share;
- ownership of the actual asset, territory, indication, subsidiary, or cash flow being valued.

If a material financing need is unresolved, do not declare undervaluation using today's share count alone.

### 3. Build the falsifiable thesis map

Express the investment case as three to five claims. For every major claim use:

`Mechanism -> Metric -> Benchmark -> Falsifier`

Record supporting evidence, challenging evidence, remaining uncertainty, evidence confidence, and the next evidence that could change probability.

### 4. Identify the economic engine

Find the small number of variables that create equity value. Depending on the security, these may include:

- volume, price, mix, share, retention, utilization;
- margins, unit economics, capital intensity, ROIC, FCF, reinvestment runway;
- project resources/reserves, capex, recovery, schedule, commodity sensitivity;
- clinical/regulatory probability, launch, royalties, milestones, runway, dilution;
- rates, fleet exposure, contract duration, asset values, break-evens;
- event probability, payoff, timing, and financing.

Use the relevant sector overlay rather than forcing conventional operating metrics.

### 5. Determine what is priced in

Mandatory. Use reverse valuation, market-implied probability, normalized earnings, asset NAV, or another appropriate method to state:

> **At today's price, the market appears to discount approximately ______.**

Compare that implied path with the underwritten path. The difference is the potential mispricing.

### 6. Forecast the key value drivers

Forecast only variables that materially influence value. Separate:

- evidence-supported forecast changes;
- extrapolations;
- consensus;
- analyst assumptions.

Use ranges when uncertainty makes point estimates artificial.

### 7. Value the security

Use the method that fits the business. Whenever practical use:

`Primary valuation method + independent cross-check`

Do not select a method because it produces the preferred answer. Explain disagreements between methods rather than averaging them away.

### 8. Build genuine Bear / Base / Bull cases

Scenarios must differ economically, not only by valuation multiple. Each should include:

- operating, project, clinical, or event assumptions;
- financing and dilution;
- valuation method;
- equity value and value per fully diluted share;
- return from current price;
- expected timing and annualized return where meaningful;
- evidence required for the scenario.

The Bear case must contain a realistic failure mechanism and residual value.

### 9. Assign probabilities carefully

Use exact probabilities only when reasonably underwriteable. Analyst probabilities are assumptions, not sourced facts.

When subjective probabilities are weak, prefer:

- market-implied probability;
- break-even success probability;
- required probability for the current price to meet the return hurdle;
- probability ranges.

Probabilities must total 100% when probability-weighted value is shown.

### 10. Calculate return and skew

Show where the inputs permit:

- probability-weighted value;
- expected return and expected annualized return;
- Bear downside, Base return, and Bull upside;
- upside/downside ratio;
- expected time to realization;
- dependence on multiple expansion versus fundamental value creation.

Do not hide unacceptable permanent-loss risk behind positive expected value.

### 11. Apply the return-hurdle and opportunity-cost gate

Use the user's or strategy's actual required-return rule when available. If none is supplied, state that explicitly and show sensitivity rather than inventing a personal hurdle.

Compare the security with the closest realistic alternative: an existing holding, cash, an index, a peer, or another active idea. State:

- expected annualized return;
- applicable hurdle or hurdle sensitivity;
- return premium or shortfall;
- risk, liquidity, duration, and confidence differences;
- why incremental capital belongs here rather than in the alternative.

A positive expected return is not sufficient if it does not compensate for risk, duration, or opportunity cost.

### 12. Apply the Time-to-Resolution Gate

Provide:

- expected holding period;
- target realization date;
- mandatory re-underwrite date;
- why each date is appropriate;
- measurable evidence required by then;
- delay risk and the valuation cost of time.

The re-underwrite date is a decision boundary, not an automatic sell date. At that date the thesis must be renewed, downgraded, or exited from the research posture. Long-duration compounders should normally be re-underwritten at least annually unless there is a stated reason otherwise.

If no credible realization mechanism exists within the proposed horizon, downgrade to WATCH or PASS.

### 13. Red-team the thesis

Assume the thesis is wrong. Test:

- management incentives and capital allocation;
- accounting and metric quality;
- competition and substitution;
- financing, dilution, liquidity, and hidden claims;
- regulation, technology, safety, execution, cyclicality, and customer concentration;
- time-to-value and dependence on takeover or multiple expansion.

Identify the single strongest disconfirming fact and state whether the thesis survives it.

### 14. Map catalysts and kill criteria

Separate:

- **Fundamental catalysts** — change intrinsic value.
- **Recognition catalysts** — help the market recognize existing value.
- **Monitoring events** — informative but do not themselves change value.

State three to five measurable kill criteria. Price decline alone is not a falsifier.

### 15. Determine readiness and run the challenge gate

Separate:

**Evidence confidence**
- High — multiple high-quality independent or primary sources align.
- Medium — good support exists but meaningful gaps remain.
- Low — load-bearing claims depend on weak, contradictory, or speculative evidence.

**Underwriting readiness**
- Decision-ready — economics, capital structure, scenarios, timing, major risks, hurdle, and opportunity cost are sufficiently understood.
- Preliminary — credible, but one or more important questions remain.
- Screen-grade — enough to continue research, not enough for capital allocation.

Before advancing a Decision-ready INVESTABLE idea toward capital allocation, invoke `underwriting-challenger` when available. Give it the evidence ledger and model assumptions before the final verdict when practical. Reconcile any material disagreement. If no independent challenge was run, label the conclusion `UNCHALLENGED` rather than implying independent validation.

### 16. Produce the portfolio handoff

Full Underwriting does not choose the exact account or position size. It must provide the inputs needed by the portfolio/risk workflow, including downside, expected return, duration, liquidity, event/gap risk, factor exposures, correlation concerns, currency/listing issues, and entry/add/trim/exit evidence. Use the portfolio handoff reference.

## Final posture

Choose exactly one:

- **INVESTABLE** — materially mispriced; evidence, valuation, hurdle, duration, and downside support capital-allocation review.
- **INVESTABLE, BUT PRICE-SENSITIVE** — thesis is sound, but current expected return does not clear the hurdle; state the entry condition.
- **WATCH / WAIT FOR PROOF** — unresolved variables dominate; name the evidence and date.
- **PASS** — insufficient differentiated return versus risk, duration, or alternatives.
- **REJECT** — thesis failed or permanent-loss risk is unacceptable.

## Required output

### Underwriting Verdict

**Security:**  
**Price / as-of date:**  
**Posture:**  
**Underwriting readiness:**  
**Evidence confidence:**  
**Challenge status:** SURVIVES / REVISED / FAILED / UNCHALLENGED / NOT REQUIRED  
**Expected holding period:**  
**Target realization date:**  
**Mandatory re-underwrite date:**  

**One-sentence conclusion:** State the actual investment answer.

### Variant perception

### What is priced in?

### Thesis map

Three to five `Mechanism -> Metric -> Benchmark -> Falsifier` claims.

### Economic engine and valuation

Show the primary method, cross-check, fully diluted treatment, and major assumptions.

### Scenario skew

| Scenario | Probability | Value/share | Return | Annualized return | Time | Key assumption |
|---|---:|---:|---:|---:|---|---|
| Bear | | | | | | |
| Base | | | | | | |
| Bull | | | | | | |

**Probability-weighted value:**  
**Expected return:**  
**Expected annualized return:**  
**Bear downside:**  
**Upside/downside ratio:**  

### Hurdle and opportunity cost

**Required-return rule:**  
**Return premium / shortfall:**  
**Closest alternative:**  
**Why this is or is not the better use of capital:**  

### Time-to-resolution

### Strongest challenge and challenger reconciliation

### Catalysts and kill criteria

### What remains unknown

### Portfolio/risk handoff

### Next action

Choose one:

- Advance to independent challenge
- Advance toward portfolio/risk review
- Run targeted research
- Wait for named evidence/catalyst
- Add to watchlist
- Pass
- Reject

## Boundaries

Do not perform account-specific position sizing, trade execution, hedging implementation, tax advice, or account-location decisions inside this skill. Hand those to the appropriate portfolio/risk workflow.

Do not present takeover optionality, a strategic investor, a large TAM, management enthusiasm, a low headline multiple, or a recent price decline as sufficient proof of investability.
