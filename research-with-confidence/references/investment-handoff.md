# Investment Handoff Contract

Use this structure whenever Research With Confidence may advance a lead to Full Underwriting.

For sectoral, macro, commodity, regulatory, thematic, cross-company, or other leads with multiple plausible tradable implementations, also use `expression-selection.md`. The expression gate is mandatory before any single stock can advance to Full Underwriting.

## Required handoff

### Identity

```text
event_id
security_or_candidate_set
information_cutoff
current_price_context_if_available
research_route
```

### Thesis development

1. **Original Radar hypothesis** — preserve the starting claim.
2. **Corrected RWC hypothesis** — state the best current formulation, even when materially different.
3. **Genuinely new information** — specify the delta.
4. **Previously known or expected information** — include prior guidance, scheduled milestones, and pre-event anticipation.

### Evidence and causality

5. **Primary-source confirmation** — original documents and what they do or do not prove.
6. **Mechanism** — event to operational/probabilistic variable to company economics.
7. **Counterfactual** — what likely occurs without the event.
8. **Confounders and competing explanations** — observations that could create the same apparent result.
9. **Strongest disconfirming fact** — the single most important challenge.

### Economic map

10. **Materiality bridge** — order-of-magnitude effect on units, revenue, margins, FCF, assets, financing, probabilities, or timing.
11. **Obvious beneficiary** — direct exposure and why.
12. **Second-order beneficiary or alternative expression** — less obvious capture path.
13. **Non-beneficiary / false friend** — related company that lacks sufficient capture or is already fully obvious.
14. **Potential loser or comparator** — when useful.

### Expression / security selection

15. **Expression-gate applicability** — state `MANDATORY` or `NOT REQUIRED` and why.
16. **Candidate-set comparison** — when mandatory, compare viable individual stocks, ETF/ETN/listed funds or commodity pools, baskets, direct underlying/futures, options when timing supports them, and `NO TRADE` using the common dimensions in `expression-selection.md`.
17. **Best direct expression** — or `NONE / UNAVAILABLE`.
18. **Best equity expression** — or `NONE / UNAVAILABLE`.
19. **Best diversified expression** — or `NONE / UNAVAILABLE`.
20. **Chosen expression and why** — identify where the actual mispricing sits, not merely where thematic exposure is highest.
21. **Flip condition** — what evidence, price, duration, or structure change would make another expression superior.

A thematic lead cannot advance a single stock while items 15–21 are incomplete.

### Expectations

22. **Pre-event expectation evidence** — guidance, consensus, known catalyst date, positioning, or run-up.
23. **Price and estimate context** — timestamped and limited to periods when the market could react.
24. **Plausible expectation gap** — what the market may be missing: magnitude, duration, ownership economics, probability, timing, attribution, or the relative pricing of alternative expressions.

### Confidence and next action

25. **Evidence confidence** — by load-bearing claim.
26. **Mispricing confidence** — separate from evidence confidence and specific to the chosen expression.
27. **Three remaining unknowns maximum** — only decision-relevant gaps.
28. **Next decisive evidence and date**.
29. **Stopping decision** — Advance, Targeted Research, Wait, Monitor, or Reject.
30. **Exact Full Underwriting question** — current price, horizon, chosen expression, and the market-implied outcome to test.

## Underwriting readiness test

Advance only when:

- the core mechanism survives;
- the effect could be material;
- a plausible expectations gap exists;
- the selected security or instrument captures enough of the economics;
- when the expression gate is mandatory, viable ETF/fund/basket/direct-instrument/options/no-trade alternatives have been compared and the chosen expression wins for a stated reason;
- the remaining decisive work is valuation, financing/dilution, scenarios, timing, or risk/reward.

Do not advance simply because the world thesis is true, the company is high quality, the stock was named first, the stock is already owned, or an equity is easier to underwrite than the alternatives.

## Stopping rules

Choose `TARGETED RESEARCH` or `WAIT` rather than Full Underwriting when:

- a named primary document, earnings release, trial dataset, fixture book, financing term, or regulator decision is imminent;
- one missing denominator determines whether the effect is material;
- current security price or capital structure cannot be established reliably;
- the causal attribution remains dominated by confounders;
- the best expression may depend on unresolved wrapper, roll, basis, liquidity, options, or implementation economics.

Choose `MONITOR` or `REJECT` when:

- no public security has material capture;
- the effect is too small relative to enterprise value;
- the thesis is already broadly visible and no variant remains;
- the evidence cannot become observable in a useful horizon;
- the thesis may be true but every viable expression is already fully priced or structurally unattractive;
- further work is unlikely to change a decision.
