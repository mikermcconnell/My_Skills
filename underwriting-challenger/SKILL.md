---
name: underwriting-challenger
description: Independently challenge a completed or near-complete public-equity Full Underwriting before capital allocation. Reconstruct what the price implies, audit capital structure and model logic, test the most sensitive assumptions and strongest failure mechanism, and conclude whether the original case survives, needs revision, is not decision-ready, or fails. Use after Full Underwriting or when the user asks for an independent red team. Do not use for first-pass research, short-duration event trades, routine company summaries, or position sizing.
---

# Underwriting Challenger

Provide an independent decision-quality check, not another supportive summary.

The preferred sequence is:

1. receive the evidence ledger, source pack, capital structure, model assumptions, current price, hurdle, and closest alternative;
2. form an independent view before seeing the original final verdict or probability-weighted target when practical;
3. compare and reconcile only after the independent assessment is written;
4. hand a surviving reconciled case to Portfolio Capital Allocation rather than sizing it inside the challenge.

If the original verdict cannot be hidden, explicitly bracket it and do not use it as an anchor.

## Reference

Read `references/challenge-checklist.md` for the full audit checklist and reconciliation format.

## Independence rules

- Start from raw sources, factual claims, and model inputs rather than the author's narrative.
- Reconstruct the security, fully diluted capitalization, and price-implied outcome independently.
- Do not change assumptions merely to be contrarian.
- Do not manufacture a bearish case. One decisive flaw can matter more than a long list of generic risks.
- Separate disagreement about facts, mechanisms, probabilities, valuation, timing, opportunity cost, and portfolio-fit inputs.
- Preserve the information cutoff. Do not use later facts to criticize an earlier decision without labelling them as ex-post evidence.
- Do not alter the original model, thesis, portfolio, or records. Recommend changes for the primary underwriter to reconcile.
- Do not infer holdings, cash, risk tolerance, or an account-specific position size.

## Inputs

Use what is available, but identify missing items:

- current price and date;
- basic and fully diluted capital structure;
- source and claim ledger;
- RWC handoff;
- thesis map and market-implied view;
- Bear/Base/Bull assumptions and probabilities;
- valuation model and cross-check;
- financing, dilution, ownership, royalty, or other claims;
- holding period, realization date, re-underwrite date;
- return hurdle and closest alternative;
- proposed portfolio-handoff risk inputs, if already drafted.

A missing load-bearing input may itself justify `NOT DECISION-READY`.

## Workflow

### 1. Reconstruct the priced-in outcome

Without using the original conclusion, estimate what operating path, asset value, normalized earnings, probability, or duration the current price appears to discount.

State where your implied view materially differs from the original and why.

### 2. Audit the security and cash-flow ownership

Check:

- share count, options, warrants, convertibles, and expected issuance;
- cash, debt, leases, preferred claims, royalties, streams, milestones, and non-recourse financing;
- ownership by territory, indication, subsidiary, project, or asset;
- post-financing rather than pre-financing value per share;
- cash flows temporarily assigned to creditors or partners;
- double-counting between revenue, royalties, milestones, asset values, and terminal value.

### 3. Audit the causal thesis

For every load-bearing claim ask:

- does the evidence actually prove the mechanism?
- is the metric using the correct denominator?
- is the benchmark appropriate?
- could a confounder explain the result?
- does the company capture the economics?
- is the claim already reflected in expectations?
- is the falsifier measurable and timely?

### 4. Identify the sensitivity breakpoint

Find the one or two assumptions that contribute most to expected value or downside. Calculate where the conclusion changes, such as:

- normalized rate, margin, multiple, adoption, price, volume, resource, capex, launch share;
- success probability, delay, dilution, or terminal value;
- entry price or time-to-realization.

Prefer breakpoint analysis over vague statements that an assumption is uncertain.

### 5. Build the strongest failure path

Trace the most credible sequence from initial problem to permanent capital impairment. Include timing and financing interactions.

Test whether the Bear case captures this path or merely assumes slower growth and a lower multiple.

### 6. Audit return hurdle and opportunity cost

Check whether expected annualized return, downside, duration, liquidity, confidence, and correlation inputs justify the conclusion relative to the stated hurdle and closest alternative.

Flag an apparently attractive value that fails because realization is too slow, the hurdle was invented, or a superior alternative was ignored.

Do not decide exact portfolio fit without current Portfolio Capital Allocation inputs. Instead identify the cluster, liquidity, event, financing, or concentration issues that the allocation gate must test.

### 7. Audit time and catalysts

Distinguish fundamental, recognition, and monitoring events. Test whether:

- the realization mechanism can plausibly close the gap;
- target and re-underwrite dates are tied to evidence;
- delay is modeled;
- the thesis can be falsified before capital is trapped indefinitely.

### 8. Conclude and reconcile

Choose exactly one:

- **SURVIVES** — no material change; original posture remains supported.
- **SURVIVES WITH REVISIONS** — case remains viable but price, probability, valuation, timing, posture, or portfolio-handoff input must change.
- **NOT DECISION-READY** — a load-bearing fact, model input, or challenge remains unresolved.
- **FAILS** — core thesis, valuation, downside, hurdle, or realization path does not survive.

Do not average the two views. Identify which evidence or calculation resolves each disagreement.

For a surviving case, state the reconciled Bear loss, expected return, horizon, liquidity/event risks, closest alternative, and unresolved constraints that Portfolio Capital Allocation must use. Do not assign the position weight.

## Required output

### Independent Challenge Verdict

**Security / price / date:**  
**Original posture:** include only during reconciliation  
**Challenge verdict:** SURVIVES / SURVIVES WITH REVISIONS / NOT DECISION-READY / FAILS  
**Confidence:**  

**One-sentence conclusion:**

### Independent priced-in view

### Capital-structure and ownership audit

### Load-bearing claim audit

| Claim | Original assumption | Independent view | Breakpoint | Evidence needed |
|---|---|---|---|---|

### Strongest failure path

### Hurdle and opportunity-cost audit

### Timing and catalyst audit

### Required revisions

List only changes that affect value, probability, timing, posture, monitoring, or allocation inputs.

### Reconciliation

State whether the original Full Underwriting posture remains, changes, or must wait.

### Portfolio Capital Allocation handoff impact

State the reconciled inputs and any new constraint. Do not size the position.

### Next action

Choose one:

- Advance to Portfolio Capital Allocation
- Return to Full Underwriting for revision
- Run targeted research
- Wait for named evidence
- Reject the capital-allocation case

## Boundaries

Do not provide exact portfolio sizing or execute a trade. Do not rewrite the original underwriting silently. The primary underwriter owns the reconciled conclusion and model update; `portfolio-capital-allocation` owns the loss budget, position range, funding source, cluster exposure, and staged entry.
