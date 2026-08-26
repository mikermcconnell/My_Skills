---
name: event-trade-underwriting
description: Underwrite a short-duration public-security trade around a discrete, dated event such as earnings, FDA or regulatory decisions, merger votes, court rulings, financings, index changes, contract awards, or policy announcements. Use when the intended holding period is hours, days, or a few weeks and the decision depends on expected versus actual information, event probabilities, payoffs, implied move, liquidity, halts, borrow, spreads, slippage, and explicit entry/exit rules. Do not use for medium-term company investing, thesis creation from headlines, routine earnings analysis, account-specific position sizing, or trade execution.
---

# Event-Trade Underwriting

Determine whether a discrete event creates a tradeable expectations gap after accounting for what was known, the current price, event probabilities, payoff asymmetry, market microstructure, and the possibility that the security cannot be exited normally.

This is a separate fast lane from Full Underwriting:

`News Radar -> Research With Confidence when factual verification is needed -> Event-Trade Underwriting -> Portfolio Capital Allocation or NO TRADE`

Use Full Underwriting when the core thesis is a multi-month or multi-year change in intrinsic value. Do not use a strong long-term company thesis to justify an unexamined short-term event bet.

## References

Read only what is needed:

- `references/event-tree-and-payoff-rules.md` for expectations, event trees, break-even probabilities, and payoff calculations.
- `references/market-microstructure-and-execution-checklist.md` for dissemination, market status, implied move, liquidity, halt, borrow, spread, and slippage checks.

## Core rules

1. **Define the clock.** Record the event date, time, timezone, decision window, market status, and information cutoff.
2. **Expected is not new.** Compare the result or rumour with a frozen pre-event baseline. An expected approval, beat, milestone, or contract is not automatically a positive surprise.
3. **Separate event quality from trade quality.** A favourable fundamental result can be a bad trade when the price already discounts it.
4. **Use executable prices.** Anchor to a current bid/ask or defensible tradable price and timestamp, not an stale close or headline move.
5. **Model discontinuity.** Include halts, gaps, borrow recalls, option-volatility collapse, failed liquidity, delayed rulings, and inability to exit.
6. **Probabilities are assumptions.** Distinguish market-implied, evidence-based, and analyst-judgment probabilities.
7. **Costs matter.** Include spread, slippage, fees, borrow, option premium/volatility, and expected execution limitations where applicable.
8. **No forced trade.** `NO TRADE` is a successful outcome. Recency and volatility are not edge.
9. **No hidden leverage.** Do not recommend options, leverage, shorting, or complex structures unless the user explicitly requests them and the required market data and risk analysis are available.
10. **Do not execute.** Hand any allocation decision to Portfolio Capital Allocation and any actual order to an explicitly authorized execution workflow.

## Preconditions

Require enough information to identify:

- exact security, exchange, currency, and instrument;
- current tradable price and timestamp;
- event and decision window;
- original source and evidence status;
- prior baseline and market expectation;
- relevant payoff states;
- liquidity and implementation constraints.

When a load-bearing factual claim is disputed, derivative, or unverified, route it to Research With Confidence before underwriting the trade.

## Workflow

### 1. Define the event and intended trade

State:

- security and instrument;
- event, source, scheduled or possible time window;
- intended entry window and maximum holding period;
- current market status;
- exact information cutoff;
- whether the analysis is pre-event, live/post-event, or a rumour response.

For a live event, distinguish what was public before the security moved from what became public afterward.

### 2. Reconstruct expectations

Use the frozen catalyst packet when available. Otherwise establish:

- prior company guidance and known facts;
- consensus, market-implied probability, options-implied move, or a clearly labelled proxy;
- pre-event run-up/selloff and positioning evidence when reliable;
- what the market appears to expect in each key variable;
- what result would be genuinely surprising rather than merely positive or negative in absolute terms.

Do not invent consensus or implied probability. When unavailable, state that the expectations gate is weak and lower readiness.

### 3. Verify the information delta

Classify the focal information as:

- genuinely new;
- repeated or previously disclosed;
- independent confirmation;
- acceleration or deceleration;
- contradiction;
- risk disclosure;
- rumour or unsupported assertion;
- ambiguous or incomplete.

Trace derivative reporting to the original source. A social post, screenshot, anonymous claim, or one newswire should not be treated as multiple confirmations.

### 4. Build the event tree

Create mutually exclusive, collectively exhaustive states appropriate to the event. For each state show:

- probability and basis;
- fundamental interpretation;
- immediate tradable-price range;
- later price or value path when relevant;
- time to resolution;
- liquidity or halt conditions;
- main evidence that would move the probability.

Use ranges rather than fake point precision. Probabilities must total 100% when expected value is calculated.

### 5. Calculate break-even and expected payoff

Calculate where inputs permit:

- expected gross return;
- expected net return after costs and slippage;
- downside in the adverse event state;
- upside/downside ratio;
- break-even success probability;
- market-implied probability when a defensible payoff pair exists;
- sensitivity to entry price, delay, probability, and execution cost.

For a simple two-state long trade:

```text
break-even probability = loss if failure / (gain if success + loss if failure)
```

Use the full event tree when outcomes are not binary.

Do not annualize a one-day event trade in a way that implies the opportunity can be repeated continuously.

### 6. Audit market microstructure and execution feasibility

Check:

- bid/ask spread, depth, typical volume, free float, and expected participation;
- market open/closed, after-hours access, auction, halt, circuit breaker, or dissemination timing;
- borrow availability, fee, recall, and squeeze risk for shorts;
- options liquidity, strike/expiry fit, implied volatility, skew, volatility crush, assignment, and maximum loss when options are explicitly requested;
- foreign listing, ADR/local mismatch, currency, settlement, or stale-quote risk;
- information leakage, selective access, or whether the market has already traded on the result;
- whether the user can reasonably enter and exit at the modeled prices.

A positive theoretical expected value is not tradeable when the assumed prices or liquidity are unavailable.

### 7. Define the path and invalidation rules

State:

- entry condition and maximum acceptable price;
- no-trade condition;
- maximum planned holding period;
- event, price, time, or evidence invalidation;
- exit rules for success, partial success, failure, delay, and ambiguous outcome;
- whether the position converts into a medium-term investment only after a separate Full Underwriting—not by default.

Do not use an undefined “wait and see” exit after an adverse event.

### 8. Stress the trade

Test at least:

- probability is wrong;
- the result is favourable but below expectations;
- the event is delayed;
- the security halts or gaps through the exit;
- spread/slippage doubles;
- the market reaction reverses after initial interpretation;
- the source is false or incomplete;
- a correlated macro or sector move dominates the event.

Identify the single strongest reason the apparent edge may be illusory.

### 9. Choose the posture

Choose exactly one:

- **TRADEABLE** — evidence, expectations gap, payoff, execution, and downside support a short-duration allocation review at the current or stated price.
- **TRADEABLE ONLY AT SPECIFIED PRICE / CONDITION** — edge exists only below/above a named entry, after confirmation, or with a specified instrument and risk limit.
- **WAIT FOR CONFIRMATION** — the event may be attractive, but source quality, timing, market status, or a named data point is unresolved.
- **NO TRADE** — no sufficient expectations gap, payoff edge, executable liquidity, or risk-adjusted advantage.
- **REJECT** — premise is false, stale, manipulated, structurally untradeable, or exposes the user to unacceptable loss.

## Required output

### Event-Trade Verdict

**Security / instrument:**  
**Current tradable price / timestamp:**  
**Event / decision window:**  
**Information cutoff:**  
**Intended holding period:**  
**Posture:** TRADEABLE / PRICE OR CONDITION SENSITIVE / WAIT FOR CONFIRMATION / NO TRADE / REJECT  
**Evidence confidence:**  
**Expectations confidence:**  
**Execution confidence:**  

**One-sentence conclusion:**

### What is actually new versus expected?

### Event tree

| State | Probability | Immediate price/return range | Time | Liquidity/halt assumption | Key evidence |
|---|---:|---:|---|---|---|

### Payoff and breakpoint

**Expected gross return:**  
**Expected net return:**  
**Adverse-state loss:**  
**Break-even probability:**  
**Maximum acceptable entry price:**  

### Microstructure and implementation audit

### Entry, no-trade, and exit rules

### Strongest reason the edge may be false

### Allocation handoff

Provide maximum loss, event-gap loss, liquidity, correlation, and implementation inputs for Portfolio Capital Allocation. Do not choose an account-specific size here.

### Next action

Choose one:

- Advance to Portfolio Capital Allocation
- Enter only if the stated condition is met
- Verify the named source or fact through RWC
- Wait for the event or confirmation
- No trade
- Reject

## Boundaries

Do not execute orders, provide account-specific sizing, or present a short-duration trade as a long-term investment without completing Full Underwriting.

Do not recommend leverage, uncovered options, short selling, or complex derivatives unless explicitly requested and fully underwritten for maximum loss, liquidity, borrow or assignment, and path risk.
