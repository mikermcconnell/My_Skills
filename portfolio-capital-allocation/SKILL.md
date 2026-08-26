---
name: portfolio-capital-allocation
description: Convert one or more completed public-equity underwritings into a disciplined capital-allocation decision. Use when the user asks how much to buy, position size, fund from what, add versus wait, compare decision-ready ideas, stage an entry, trim or reallocate, or assess portfolio concentration after Full Underwriting and an independent challenge. Use exact connected holdings when account-specific sizing is requested. Do not use to invent a thesis, replace Full Underwriting, execute trades, or give tax or account-location advice.
---

# Portfolio Capital Allocation

Decide whether an underwritten security deserves incremental portfolio capital, how much portfolio loss may be put at risk, what should fund it, and what evidence controls entry, addition, trimming, or exit.

The preferred sequence is:

`News Radar -> Research With Confidence -> Full Underwriting -> Underwriting Challenger -> Portfolio Capital Allocation -> Mind Model / monitoring`

A security can be attractive in isolation and still be a poor portfolio addition because the portfolio already owns the same factor, another idea offers better risk-adjusted return, liquidity or gap risk is unacceptable, or cash is the superior alternative.

## References

Read only what is needed:

- `references/sizing-and-risk-budget-rules.md` for loss-budget sizing, uncertainty adjustments, and sensitivity rules.
- `references/exposure-entry-and-monitoring-rules.md` for cluster exposure, funding source, staged entry, and add/trim/exit evidence.

## Preconditions

Before assigning an exact or narrow position range, require when material:

- a current Full Underwriting verdict, price, bear/base/bull values, and time horizon;
- fully diluted and post-financing economics;
- expected return, expected annualized return, and bear-case loss;
- a stated hurdle or hurdle sensitivity;
- challenge status and unresolved disagreements;
- current portfolio positions, cash, relevant accounts, and constraints when the decision is account-specific.

If the underwriting is screen-grade, stale, unchallenged in a high-risk case, or missing a credible Bear case, return `WAIT` or provide only broad sensitivity. Do not fill missing holdings from memory or assume that cash is available.

## Core rules

1. **Size risk, not enthusiasm.** Begin with the portfolio loss budget and underwritten downside, not the desired dollar amount.
2. **Cash is an active alternative.** Capital does not need to be deployed merely because a security is attractive.
3. **Correlation can dominate name count.** Several tickers exposed to the same AI capex, commodity, regulator, clinical mechanism, interest-rate factor, customer, or geography may behave as one position.
4. **Use the underwritten Bear case.** Do not size from historical volatility alone when permanent-loss or gap risk is material.
5. **Do not invent risk tolerance.** Use the user's stated portfolio loss budget. If none exists, show sensitivity at clearly labelled illustrative budgets rather than selecting one for the user.
6. **Confidence and liquidity matter.** Narrow evidence, binary outcomes, financing dependence, thin liquidity, foreign listings, and event gaps normally require a lower weight than identical expected value in a liquid diversified compounder.
7. **Do not use Kelly by default.** Subjective probabilities and fat-tailed outcomes make full-Kelly sizing dangerous. Use it only as a clearly labelled cross-check when inputs are unusually robust and the user requests it.
8. **Funding source matters.** State what would be sold, reduced, or left uninvested. Avoid treating portfolio capital as costless.
9. **Entry rules must be evidence- or price-based.** Do not divide a purchase into arbitrary tranches without a reason.
10. **Sizing is provisional.** Material price, thesis, financing, catalyst, correlation, or portfolio changes require a refresh.

## Workflow

### 1. Define the allocation decision

State:

- security or candidate set;
- current price and timestamp;
- account or portfolio scope;
- available cash or proposed funding source;
- user constraints, prohibited exposures, tax/account limitations supplied by the user, liquidity needs, and time horizon;
- whether this is a new position, add, trim, replacement, or reallocation.

When connected portfolio data is required, retrieve it before answering. If it is unavailable, state exactly which outputs are sensitivity-only.

### 2. Validate underwriting readiness

Summarize:

- posture and challenge result;
- expected and annualized return;
- Bear/Base/Bull returns and probabilities;
- bear-case permanent loss and expected time to resolution;
- key unresolved facts;
- entry condition if price-sensitive;
- mandatory re-underwrite date.

Reject stale price inputs or update them before sizing. A high-confidence mechanism with low security-mispricing confidence is not decision-ready.

### 3. Set the portfolio loss budget

Use the user's maximum acceptable portfolio loss for this position or risk sleeve when available.

Primary sizing relationship:

`maximum weight from downside = portfolio loss budget / bear-case loss fraction`

Example: a 0.50% portfolio loss budget and 40% underwritten Bear loss imply a 1.25% maximum weight before other adjustments.

For a near-total-loss binary security, use the realistic permanent-loss fraction rather than a mild mark-to-market drawdown.

If no loss budget is provided, show a sensitivity table at illustrative portfolio-loss budgets such as 0.25%, 0.50%, and 1.00%. Label them as examples, not recommendations.

### 4. Apply portfolio and implementation adjustments

Adjust the downside-derived maximum for:

- evidence and probability confidence;
- challenger revisions or unresolved inputs;
- liquidity, spread, daily volume, lockups, foreign-market access, or borrow constraints;
- event, halt, overnight, financing, dilution, and path-dependent gap risk;
- existing exposure to the same factor, thesis, customer, commodity, geography, regulator, duration, or financing regime;
- portfolio concentration and drawdown interactions;
- time to realization and probability of delay;
- management, governance, fraud, accounting, legal, or operational tail risk;
- availability of a cleaner or more liquid expression.

Do not double-count the same risk if it is already fully reflected in the Bear case. Explain each material haircut or cap.

### 5. Compare opportunity cost and funding source

Compare the candidate with:

- cash;
- the proposed funding position;
- the closest existing holding;
- another decision-ready idea;
- a broad index or lower-risk alternative when appropriate.

Evaluate expected annualized return, downside, duration, confidence, liquidity, correlation, tax friction supplied by the user, and monitoring burden.

State explicitly:

> Incremental capital should come from ______ because ______, or remain in cash because ______.

Do not recommend selling an existing position without evaluating its current thesis and consequences. If that underwriting is stale, route it for refresh.

### 6. Design the entry or reallocation plan

Choose one:

- **Immediate full target** — only when price, evidence, liquidity, and timing justify it.
- **Price-staged entry** — tranches tied to specified valuation or expected-return thresholds.
- **Evidence-staged entry** — initial risk budget now, additions only after named proof.
- **Catalyst-staged entry** — position before or after a dated event based on explicitly underwritten event risk.
- **Replacement / pair reallocation** — reduce a weaker correlated exposure as the stronger one is funded.
- **Wait** — current price, evidence, liquidity, or concentration does not justify deployment.

For every tranche state the trigger, target incremental weight, resulting total weight, and what would cancel the next tranche.

### 7. Define add, hold, trim, and exit evidence

Separate price from thesis evidence.

- **Add:** named operating, clinical, financial, or valuation evidence that increases expected return or reduces permanent-loss risk.
- **Hold:** thesis on track within the expected evidence window.
- **Trim:** expected return falls below the hurdle, concentration grows through price appreciation, a superior alternative emerges, or thesis confidence declines without full falsification.
- **Exit:** measurable kill criterion, financing or ownership impairment, adverse challenger finding, or expiry at the mandatory re-underwrite date without renewal.

A price decline alone is not automatically an add or exit signal.

### 8. Stress the portfolio result

Show where possible:

- position weight before and after;
- bear-case portfolio loss;
- expected contribution to portfolio return;
- cluster or factor exposure before and after;
- liquidity and days-to-exit considerations;
- impact if two or more correlated positions hit their Bear case together;
- event-gap loss if normal trading is unavailable.

Do not present a precise portfolio VaR or correlation estimate without defensible data.

### 9. Choose the allocation posture

Choose exactly one:

- **FUND** — decision-ready and attractive; proposed allocation clears risk, concentration, liquidity, and opportunity-cost gates.
- **FUND SMALL / STAGED** — attractive, but uncertainty, event risk, correlation, liquidity, or price argues for limited initial exposure and explicit add conditions.
- **WAIT** — thesis may be valid, but price, proof, catalyst timing, portfolio data, or challenge status is insufficient.
- **HOLD CASH / FUND ALTERNATIVE** — another use of capital offers superior risk-adjusted return or preserves optionality.
- **TRIM / REALLOCATE** — an existing position or cluster exceeds its justified risk budget or a stronger alternative should replace it.
- **REJECT** — underwriting failed, downside is unacceptable, implementation is impractical, or the position cannot fit the portfolio within a reasonable loss budget.

## Required output

### Capital Allocation Verdict

**Security / price / date:**  
**Portfolio or account scope:**  
**Underwriting posture:**  
**Challenge status:**  
**Allocation posture:** FUND / FUND SMALL OR STAGED / WAIT / HOLD CASH OR FUND ALTERNATIVE / TRIM OR REALLOCATE / REJECT  
**Proposed initial weight:**  
**Proposed target weight or range:**  
**Maximum incremental weight:**  
**Funding source:**  
**Mandatory allocation review date:**  

**One-sentence conclusion:**

### Risk-budget calculation

| Portfolio loss budget | Bear loss fraction | Downside-derived max weight | Adjusted max weight | Main adjustment |
|---:|---:|---:|---:|---|

### Opportunity cost

### Portfolio exposure before and after

### Entry or reallocation plan

| Step | Trigger | Incremental weight | Total weight | Cancellation condition |
|---|---|---:|---:|---|

### Add, hold, trim, and exit evidence

### Stress result and unresolved constraints

### Next action

Choose one:

- Fund at the stated weight
- Fund the initial staged tranche
- Refresh underwriting or challenge
- Retrieve current portfolio data
- Wait for named price/evidence/catalyst
- Hold cash or fund the named alternative
- Trim or reallocate
- Reject

## Boundaries

Do not execute a trade, choose an account without the user's instruction, provide tax advice, or silently infer holdings, cash, cost basis, liquidity needs, or risk tolerance.

Do not use position sizing to rescue a failed thesis. A tiny position in a bad security is still a bad decision.
