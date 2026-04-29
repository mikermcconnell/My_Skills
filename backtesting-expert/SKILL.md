---
name: backtesting-expert
description: Repo-specific backtesting and strategy-validation workflow for the Investing app. Use when working in this Investing repo on raw alpha vs sleeve alpha, benchmark choice, event studies, capacity limits, overlapping trades, hedged sleeves, costs, robustness, lookahead bias, survivorship bias, sample-size concerns, or when deciding whether a backtest result is actually strong enough to trust.
---

# Backtesting Expert

Use this skill only for the **Investing** repo when the task is about whether a strategy result is real, tradable, robust, or decision-worthy.

This skill is for:
- strategy validation
- event studies
- raw alpha vs sleeve alpha interpretation
- long-only vs hedged sleeve design
- benchmark choice
- capacity and overlap effects
- robustness and sensitivity testing
- honest backtest summaries

## Core repo stance

In this repo:
- **raw alpha** and **sleeve alpha** are different numbers with different meanings
- positive raw alpha does **not** prove a good tradable sleeve exists
- simulated sleeve results can fail because of overlap, holding-period path, capacity limits, market beta, and clustered events
- conclusions must stay honest about whether the result is:
  - exploratory
  - research-only
  - monitor-worthy
  - forward-testable
  - actually strong

## Start here

Before making claims:
1. Read the latest relevant report under `reports/`
2. Read the current summary doc if one exists under `docs/`
3. Check the actual script or code path that produced the result
4. Use the report wording only if it still matches the code and latest reruns

## Required workflow

### 1. Define the exact question

Pin down:
- what is being tested
- signal study or tradable sleeve
- long-only or hedged
- event date or effective date
- hold period
- capacity rule
- costs
- benchmark

If any of those are unclear, state the assumption before proceeding.

### 2. Separate the metric types

Always distinguish:

- **Raw alpha**
  - matched event average
  - usually stock return minus SPY over a fixed horizon
- **Accepted alpha**
  - only the names that survive the sleeve rule
- **Skipped alpha**
  - names blocked by capacity or ranking
- **Sleeve alpha**
  - path-based portfolio result after overlap, timing, and constraints
- **Hedged sleeve return**
  - long signal basket offset by short SPY or another hedge

Never treat these as interchangeable.

### 3. Check the backtest honesty risks

Always scan for:
- lookahead bias
- survivorship bias
- stale or incomplete event dates
- benchmark mismatch
- unrealistic entry timing
- unrealistic fill assumptions
- cost omission
- hidden concentration in a few trades or years
- tiny sample size disguised by large returns

Call these out directly.

### 4. Run the minimum useful diagnostics

When practical, review:
- raw target-hold alpha
- accepted vs skipped alpha
- year splits
- outlier dependence
- capacity pressure
- time in market
- average active positions
- drawdown
- whether the edge survives hedging

If a result fails one of these badly, say so plainly.

### 5. Decide what the result means

Use clear labels:

- **Fail**
  - sleeve result does not support the strategy objective
- **Exploratory**
  - interesting but too weak, too unstable, or too sparse
- **Research-only**
  - signal may be real but not yet monetizable
- **Forward-test candidate**
  - good enough to monitor live, not proven
- **Lead candidate**
  - strongest current branch, but still state limitations

Prefer conservative labels.

## Repo-specific interpretation rules

### Raw alpha vs sleeve alpha

If raw alpha is positive but sleeve alpha is negative, likely explanations include:
- the edge is too small
- the edge is too concentrated
- the edge is relative rather than absolute
- the long-only vehicle is wrong
- the holding period is mismatched
- same-day intake is selecting the wrong names
- effective-date entry is too late

Do not force a bullish conclusion from raw alpha alone.

### Hedged results

If long-only is negative but hedged is positive:
- interpret the branch as **relative alpha**, not a strong standalone long sleeve
- treat it as a different strategy family, not just a better version of the same long-only desk

### Small-sample results

If the result depends on very few trades:
- call it sparse
- do not present it as validated
- do not let large percentages override low sample size

## Output style

When reporting findings, prefer:
- direct conclusion first
- small table or bullets
- plain English explanation
- exact numbers for 2Y and 5Y when available
- explicit note on whether the branch passed or failed the stated objective

Good structure:
- Objective
- What was tested
- What the numbers say
- Plain-English interpretation
- Recommendation

## What to avoid

- overstating weak edges
- mixing raw and sleeve numbers
- calling a branch “validated” because one subwindow looked good
- hiding sample-size problems
- tuning endlessly after repeated failure
- confusing “beats cash” with “good enough”
- ignoring whether SPY itself was very strong over the same window

## Default next moves

When a branch fails as long-only but raw alpha stays positive, likely next moves are:
1. test hedged sleeve
2. test whether the event date is too late
3. test whether unused cash should be benchmarked differently or parked in SPY
4. test whether the branch is regime-specific
5. write an honest summary before more tuning

## Good prompts for this skill

- Why is raw alpha positive but sleeve alpha negative?
- Does this backtest actually prove anything?
- Is this strategy exploratory, monitor-worthy, or dead?
- Compare long-only and hedged versions of this branch
- Write a clear summary of these backtest reruns for the repo
