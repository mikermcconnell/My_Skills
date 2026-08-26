# Sizing and Risk-Budget Rules

## Start with loss budget

The primary question is not “how much upside is available?” It is:

> How much portfolio capital can be exposed while keeping the underwritten Bear outcome inside the accepted loss budget?

Use:

```text
maximum position weight = maximum portfolio loss budget / underwritten bear-case loss fraction
```

Examples:

| Portfolio loss budget | Bear-case loss | Downside-derived maximum weight |
|---:|---:|---:|
| 0.25% | 25% | 1.00% |
| 0.50% | 40% | 1.25% |
| 0.50% | 75% | 0.67% |
| 1.00% | 20% | 5.00% |

These examples illustrate arithmetic, not recommended risk budgets.

## Define the Bear loss correctly

Use the realistic permanent-loss or thesis-failure outcome from Full Underwriting, including when material:

- dilution and financing;
- debt, leases, preferred claims, royalties, streams, or partner ownership;
- clinical or regulatory failure;
- project delay, cost overrun, commodity normalization, or asset impairment;
- cyclical earnings collapse;
- fraud, safety, legal, governance, or liquidity tail risk;
- inability to exit during a halt or gap.

Do not substitute a historical one-standard-deviation move for a fundamental Bear case.

When Bear value is above zero:

```text
bear-case loss fraction = max(0, 1 - bear value per share / current price)
```

When the thesis can lose more than the initial marked value through leverage, derivatives, capital calls, or other obligations, do not use this simple long-equity formula.

## Missing risk budget

Never infer a personal risk tolerance. When the user has not supplied a maximum acceptable portfolio loss:

1. show several clearly labelled illustrative loss budgets, normally 0.25%, 0.50%, and 1.00%;
2. show how the resulting position changes after portfolio adjustments;
3. identify the decision that cannot be completed without the user's constraint.

Do not select the middle value and present it as a recommendation.

## Confidence adjustment

The downside formula produces a ceiling, not a target. Reduce it when:

- evidence confidence is low or concentrated in one source;
- security-mispricing confidence is materially below mechanism confidence;
- scenario probabilities are subjective or unstable;
- the challenger found unresolved breakpoints;
- the thesis depends on a single customer, regulator, asset, trial, financing, or management decision;
- the outcome distribution is highly skewed, discontinuous, or fat-tailed.

A useful qualitative framework is:

- **High confidence / diversified evidence:** modest or no confidence haircut.
- **Medium confidence:** meaningful haircut or staged entry.
- **Low confidence:** broad sensitivity only, very small risk budget, or WAIT.

Do not convert these labels into fixed universal multipliers unless the user's strategy has validated them.

## Correlation and cluster cap

Identify the economic cluster, not merely the ticker sector. Examples:

- frontier-AI capex and memory scarcity;
- one commodity or shipping route;
- one regulator, clinical modality, payer, or partner;
- one customer, supplier, geography, currency, financing regime, or duration factor.

Stress the combined Bear loss of correlated positions. A new weight may be below its standalone cap and still be unacceptable at the cluster level.

When correlation data is unavailable, use causal exposure mapping and scenario co-movement rather than fabricating a coefficient.

## Liquidity and implementation cap

Reduce the maximum weight when:

- average volume, spread, market hours, foreign listing, or settlement makes entry/exit difficult;
- insider ownership, lockups, float, borrow, or corporate actions can impair liquidity;
- a halt or binary event can prevent orderly exit;
- the proposed order would represent a material share of normal trading volume.

State days-to-exit only when based on a transparent participation-rate assumption. Do not assume the full quoted volume is available to the user.

## Time and delay

Compare annualized expected return, not only terminal upside. Reduce or reject allocation when:

- the valuation gap has no credible realization path;
- delay materially lowers annualized return;
- repeated financing is required during the wait;
- monitoring burden and opportunity cost are high;
- the re-underwrite date may arrive before decisive evidence.

## Kelly as an optional cross-check

Do not use Kelly by default. It is fragile when probabilities, payoffs, independence, and repeatability are uncertain.

When explicitly requested and reasonably supported:

- show the input probabilities and payoffs;
- use fractional Kelly rather than full Kelly as a sensitivity;
- cap the result by downside budget, liquidity, cluster exposure, and practical concentration rules;
- never let Kelly override a failed underwriting or unacceptable permanent-loss path.

## Final sizing hierarchy

The proposed target should not exceed the lowest relevant constraint:

```text
min(
  downside-derived maximum,
  cluster cap,
  liquidity cap,
  event/gap-risk cap,
  confidence-adjusted cap,
  portfolio concentration cap,
  available-capital cap
)
```

Explain which constraint is binding.
