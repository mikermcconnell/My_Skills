---
name: full-underwriting
description: Perform a full buy-side underwriting of a listed company or public security and decide whether it is actually investable at the current price. Use when the user says "full underwriting", "underwrite this", "is this actually cheap", "take this from research to investment", "is this investable", or when a News Radar / Research With Confidence lead needs valuation, what-is-priced-in analysis, financing/dilution, bear-base-bull scenarios, catalysts, falsifiers, time-to-resolution, and a final Investable / Watch / Pass decision. Do not use for first-pass idea generation, simple company summaries, news triage, or portfolio sizing alone.
---

# Full Underwriting

Turn a promising public-equity research lead into a security-level capital decision.

The central question is:

> At the current security price, what must be true for this investment to generate an attractive return, how likely is that outcome, how long should it take, and what can permanently impair capital?

A good company is not automatically a good investment. A compelling story is not automatically mispriced.

## Place in the workflow

Typical sequence:

`News Radar Investing -> Research With Confidence -> Full Underwriting -> portfolio/risk sizing -> Mind Model / thesis tracking`

If a Research With Confidence handoff already exists, treat it as the baseline. Do not restart from scratch. Preserve supported findings, challenges, confidence levels, and unresolved questions; reverify market-sensitive and load-bearing facts.

Full Underwriting owns the final security-level conclusion. Modeling, valuation, sector, event, or financial skills may support it, but they do not replace the integrated judgment.

## Required references

Read only what the case needs:

- `references/valuation-methods.md` for valuation, reverse valuation, capitalization, financing, and dilution.
- `references/scenario-and-probability-rules.md` for bear/base/bull, probability, expected-return, and time-to-resolution rules.
- `references/sector-overlays.md` for sector-specific underwriting requirements.
- `references/underwriting-quality-checklist.md` before finalizing.

## Core rules

1. **Price matters.** Never call a security investable without anchoring to a current price and as-of date.
2. **Fully diluted economics matter.** Include material options, warrants, convertibles, debt, royalties, streams, and expected financing. For capital-dependent businesses, underwrite post-financing value per share.
3. **Underwrite the future, not the story.** Historical evidence matters only insofar as it changes future cash flows, probabilities, valuation, or timing.
4. **Separate fact from assumption.** Label reported facts, company claims, independent evidence, consensus, derived calculations, analyst assumptions, judgment/probabilities, and unknowns.
5. **Variant perception is required.** State what the market appears to believe that the underwriting believes is wrong or incomplete. "Good company" or "large TAM" is not a variant view.
6. **Downside is part of valuation.** Model how the thesis fails and what equity value remains. Do not append a generic risk section after a bullish model.
7. **Time is part of return.** Every investable conclusion requires an expected holding period and an explicit end/re-underwrite date.
8. **Do not force a buy.** PASS and WAIT are successful underwriting outcomes.

## Workflow

### 1. Define the underwriting question

Start with one sentence that includes:

- security / ticker
- current price and date
- investment horizon under consideration
- primary investment question
- current research posture

Example:

> Is Radisson Mining worth materially more than its current fully diluted valuation after accounting for development risk, financing, dilution, and realistic O'Brien resource growth?

### 2. Establish the security and capital structure

Before detailed valuation, establish when available:

- basic shares
- diluted shares
- current price
- basic and fully diluted market capitalization
- cash
- debt
- enterprise value
- material warrants/options/convertibles
- royalties, streams, preferred claims, leases, or other material obligations
- expected future financing
- estimated post-financing share count when financing is required to reach the base case

If a material financing need is unresolved, do not declare the security undervalued using today's share count alone.

### 3. Build a falsifiable thesis map

Express the investment case as 3-5 claims.

For every major claim use:

**Mechanism -> Metric -> Benchmark -> Falsifier**

For each claim identify:

- supporting evidence
- challenging evidence
- remaining uncertainty
- evidence confidence
- next evidence that could materially change the probability

### 4. Understand the economic engine

Identify the small set of variables that actually create equity value.

For operating companies this may include volume, price, market share, retention, margins, unit economics, capital intensity, ROIC, FCF, and reinvestment runway.

For development-stage, clinical, resource, or event-driven companies, use the relevant sector economics instead of forcing conventional operating metrics.

### 5. Determine what is priced in

Mandatory.

Do not merely calculate what the company could be worth. Estimate what operating or probabilistic outcome is consistent with the current price using the appropriate reverse-valuation method.

State explicitly:

> **At today's price, the market appears to discount approximately ______.**

Then compare that implied outcome with the underwritten view. The gap is the potential mispricing.

### 6. Forecast the key value drivers

Forecast only variables that materially influence value. Avoid fake precision.

Use Bear / Base / Bull assumptions and distinguish:

- evidence-supported forecast changes
- extrapolations
- analyst assumptions

Use ranges when uncertainty is too high for precise point estimates.

### 7. Value the security

Use the valuation method that best matches the business. Whenever practical use:

**Primary valuation method + independent cross-check.**

Do not choose a method simply because it produces the preferred answer. See `references/valuation-methods.md`.

### 8. Apply the Time-to-Resolution Gate

Every underwriting must answer **how long the capital is expected to be tied to the thesis**.

Classify the expected holding period using a practical label such as:

- Days / event trade
- 1-4 weeks
- 1-3 months
- 3-12 months
- 1-3 years
- 3-5+ years / compounder

Then provide:

- **Expected holding period** — e.g. 6-12 months.
- **Target realization date** — calendar date by which the principal valuation gap should begin or largely complete closing.
- **Mandatory re-underwrite date** — calendar date when the original underwriting expires and must be refreshed even if no thesis-breaking event occurred.
- **Why that date** — catalyst, earnings path, clinical readout, drill program, construction milestone, normalization cycle, or compounding period.
- **What must happen by then** — measurable evidence required to justify continuing to hold the thesis.

The end date is a **decision boundary, not an automatic sell date**. At that date the investment must be re-underwritten and explicitly renewed, downgraded, or exited from the research posture.

For discrete events, use the expected event/decision date plus a reasonable settlement or information window. For long-duration compounders, use a longer target horizon but still set a mandatory periodic re-underwrite date, normally no more than 12 months from the analysis date unless the user specifies otherwise.

If there is no credible mechanism for the valuation gap to close within the proposed horizon, downgrade the idea to WATCH or PASS.

### 9. Build genuine Bear / Base / Bull cases

Scenarios must differ economically, not merely by valuation multiple.

Each scenario should include:

- operating / project / clinical assumptions
- financing and dilution assumptions
- valuation method
- equity value
- value per fully diluted share
- upside/downside from current price
- expected timing
- annualized return where meaningful
- evidence necessary for the scenario to occur

The Bear case must contain a realistic failure mechanism.

### 10. Assign probabilities carefully

Use precise probabilities only when useful and reasonably underwriteable. Analyst probabilities must never appear as sourced facts.

When probabilities are weakly supported, prefer ranges or calculate:

- market-implied probability
- break-even success probability
- required probability for the current price to be attractive

Probabilities must total 100% when a probability-weighted value is shown.

### 11. Calculate return and skew

Where scenarios permit, show:

- probability-weighted value
- expected return
- expected annualized return where meaningful
- Bear-case downside
- Base-case return
- Bull-case upside
- upside/downside ratio
- expected time to realization

Do not hide unacceptable permanent-loss risk behind a positive expected value.

### 12. Red-team the thesis

Mandatory.

Assume the thesis is wrong and find the strongest credible reason why. Test management incentives, accounting quality, competitive response, financing, dilution, regulation, technology, execution history, cyclicality, hidden liabilities, customer concentration, time-to-value, and dependence on multiple expansion or takeover.

Identify the **single strongest disconfirming fact** and state whether the thesis survives it.

Do not manufacture symmetric bear evidence merely for balance. One high-quality disconfirming observation can outweigh many weak supporting observations.

### 13. Map catalysts and value realization

Separate:

- **Fundamental catalysts** — change intrinsic value.
- **Recognition catalysts** — cause the market to recognize value already present.
- **Monitoring events** — informative but do not themselves change value.

Map the path over appropriate windows such as 0-3 months, 3-12 months, and 1-3 years.

A discrete catalyst is not mandatory for a compounder, but the realization mechanism must be credible.

### 14. Define kill criteria

State 3-5 measurable developments that materially falsify the thesis.

Price decline alone is not a falsifier.

### 15. Separate evidence confidence from underwriting readiness

**Evidence confidence**
- High: multiple high-quality independent or primary sources align.
- Medium: good support exists but meaningful gaps remain.
- Low: important claims depend on weak, contradictory, single-source, or speculative evidence.

**Underwriting readiness**
- Decision-ready: the important value drivers, capital structure, financing, scenarios, timing, and major risks are sufficiently understood.
- Preliminary: the thesis is credible but one or more important questions remain unresolved.
- Screen-grade: enough evidence exists to continue researching, but not to make a capital decision.

High evidence confidence does not automatically mean decision-ready.

## Final posture

End with exactly one primary posture:

### INVESTABLE
The security appears materially mispriced and the current evidence, valuation, duration, and risk/reward support advancing toward capital allocation.

### INVESTABLE, BUT PRICE-SENSITIVE
The thesis is sound but expected return is insufficient at the current price. State the price, valuation, or operating conditions that would change the decision.

### WATCH / WAIT FOR PROOF
The thesis may work, but unresolved variables dominate expected return. State exactly what evidence is required and by what date.

### PASS
The company may be attractive, but the security does not offer enough differentiated return versus risk and time.

### REJECT
The underlying thesis failed underwriting or permanent-loss risk is unacceptable.

## Required final output

### Underwriting Verdict

**Security:**  
**Price / as-of date:**  
**Posture:** INVESTABLE / PRICE-SENSITIVE / WATCH / PASS / REJECT  
**Underwriting readiness:**  
**Evidence confidence:**  
**Expected holding period:**  
**Target realization date:**  
**Mandatory re-underwrite date:**  

**One-sentence conclusion:** State the actual investment answer.

### Variant perception
What does the market appear to be getting wrong?

### What is priced in?
State the outcome implied by today's valuation.

### Thesis
3-5 falsifiable claims using Mechanism -> Metric -> Benchmark -> Falsifier.

### Valuation
Show primary method, independent cross-check, capital-structure treatment, and major assumptions.

### Scenario skew

| Scenario | Probability | Value/share | Return | Time | Key assumption |
|---|---:|---:|---:|---|---|
| Bear | | | | | |
| Base | | | | | |
| Bull | | | | | |

**Probability-weighted value:**  
**Expected return:**  
**Expected annualized return:**  
**Bear downside:**  
**Upside/downside ratio:**  

### Time-to-resolution
Explain why the target realization and re-underwrite dates are appropriate and what evidence must arrive by then.

### Why now?
Explain the catalyst or compounding/value-realization mechanism.

### Strongest challenge
State the best evidence against the investment and whether the thesis survives.

### Kill criteria
State measurable falsifiers.

### What remains unknown
Do not hide unresolved questions.

### Next action
Choose one:

- Advance toward capital allocation
- Run additional targeted research
- Wait for named evidence/catalyst
- Add to watchlist
- Pass
- Reject

## Boundaries

Do not perform account-specific position sizing inside this skill. Once a security is decision-ready and investable, hand sizing, concentration, correlation, hedging, tax, or account-location questions to the appropriate portfolio/risk workflow.

Do not present takeover optionality, a strategic investment, a large TAM, management enthusiasm, or a recent price decline as sufficient evidence of investability.
