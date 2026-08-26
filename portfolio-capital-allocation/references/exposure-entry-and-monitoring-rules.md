# Exposure, Entry, and Monitoring Rules

## Exposure map

Map the portfolio before and after the proposed allocation across the dimensions that can create common downside:

```text
company / issuer
sector and industry
economic thesis or causal mechanism
customer and supplier
commodity and input cost
geography and currency
regulator, payer, court, or policy
technology or clinical modality
interest-rate and financing sensitivity
market-cap and liquidity
factor or style exposure
binary catalyst and expected timing
```

Do not assume two companies are diversified merely because their official sectors differ. A memory supplier, cloud platform, electrical-equipment vendor, and data-centre landlord may all be exposed to the same AI-capex regime.

## Before-and-after portfolio view

Show where data permits:

- current position weights;
- proposed initial and target weights;
- cash before and after;
- cluster weight before and after;
- contribution to underwritten combined Bear loss;
- expected contribution to portfolio return;
- largest single-name, cluster, liquidity, and event concentrations.

If exact connected holdings are unavailable, use only the positions the user supplied and label the map incomplete.

## Funding-source rule

Every funded idea needs an explicit source:

- unused cash;
- sale or reduction of a named position;
- replacement of a weaker correlated expression;
- scheduled contribution;
- no funding because the recommendation is WAIT.

Before recommending a sale or trim, determine whether the funding position's underwriting is current. If it is stale, request or route a refresh rather than assuming its expected return is lower.

Include practical consequences supplied by the user, such as account restrictions, tax friction, currency conversion, or liquidity needs, but do not provide tax advice.

## Entry frameworks

### Immediate target

Use only when:

- the security clears the hurdle at the current price;
- evidence and challenge status are decision-ready;
- liquidity is adequate;
- no near catalyst creates unmodeled gap risk;
- concentration remains acceptable.

### Price-staged entry

Tie tranches to a valuation or expected-return schedule, for example:

```text
initial tranche at current price if expected annualized return clears hurdle
second tranche below a named price where downside/upside improves
final tranche only if the lower price is not caused by a thesis break
```

Recalculate valuation and Bear loss at each price. Do not assume a cheaper stock is automatically safer.

### Evidence-staged entry

Use when the thesis is promising but a named proof point remains:

- first tranche reflects current confidence;
- later tranches require specific customer, clinical, regulatory, margin, financing, production, or utilization evidence;
- negative or delayed evidence cancels the tranche.

### Catalyst-staged entry

Use only when event risk has been explicitly underwritten. State:

- pre-event maximum loss;
- expected versus surprise outcomes;
- whether the security can gap or halt;
- whether the post-event price may offer a better risk-adjusted entry;
- which stage is an investment and which is an event trade.

Do not use a medium-term thesis to justify an unexamined binary event bet.

### Replacement or pair reallocation

When two securities express the same thesis, compare:

- direct economic capture;
- expected annualized return;
- Bear downside;
- evidence confidence;
- liquidity and listing quality;
- financing and dilution;
- time to realization;
- monitoring burden.

The stronger company is not automatically the better security. Reallocate only when the expected improvement exceeds switching costs and uncertainty.

## Monitoring contract

Create an append-only allocation monitor containing:

```text
allocation date and price
initial and target weight
funding source
underwriting and challenge versions
loss budget and binding constraint
entry triggers
add evidence
trim evidence
exit / kill evidence
mandatory re-underwrite date
next catalyst and expected date
portfolio cluster at allocation
```

Do not retroactively change the original allocation rationale. Append revisions and state what new evidence caused them.

## Add rules

Add only when at least one is true:

- expected return rises because price falls without a thesis impairment;
- named evidence increases probability or value;
- financing, dilution, liquidity, or ownership risk falls;
- a challenger concern is resolved;
- portfolio cluster exposure declines, creating risk capacity.

Recalculate the loss-budget ceiling and portfolio cluster before every material add.

## Trim rules

Consider trimming when:

- price appreciation lowers expected annualized return below the hurdle;
- weight or cluster exposure exceeds the justified risk budget;
- evidence confidence declines;
- realization is materially delayed;
- financing or dilution worsens;
- a superior underwritten alternative becomes available;
- liquidity needs or user constraints change.

A trim can be correct even when the thesis remains valid.

## Exit rules

Exit or route for immediate re-underwriting when:

- a measurable kill criterion occurs;
- capital structure or ownership economics are impaired;
- fraud, governance, safety, legal, or liquidity risk becomes unacceptable;
- the thesis reaches its mandatory re-underwrite date and is not explicitly renewed;
- the independent challenge fails;
- the portfolio can no longer hold the risk within a reasonable loss budget.

Price decline alone is not a kill criterion, and price appreciation alone is not proof that the thesis succeeded.

## Post-allocation review

At each review, separate:

- thesis evidence;
- valuation and expected return;
- position and cluster size;
- portfolio loss budget;
- implementation and liquidity;
- opportunity cost.

The correct action may differ across these dimensions. For example, a thesis can strengthen while the position should be trimmed because the price has outrun value and cluster concentration has risen.
