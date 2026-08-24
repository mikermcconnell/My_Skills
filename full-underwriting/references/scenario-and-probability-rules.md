# Scenario, Probability, Return, and Time Rules

## Scenario construction

Every full underwriting needs genuine Bear / Base / Bull economic cases unless the structure of the security requires a more appropriate event tree.

Scenarios must differ in business outcomes, not just in valuation multiples.

### Bear

Describe a plausible failure mechanism. Examples:

- demand disappoints
- margins fail to scale
- resource conversion is poor
- financing becomes punitive
- clinical efficacy or safety disappoints
- regulatory approval is delayed or denied
- competition reduces market share or pricing
- capex or opex materially overruns

The Bear case should answer what equity remains if an important part of the thesis fails.

### Base

Use the outcome best supported by the current weight of evidence. Do not hide optimistic assumptions in the Base case simply because they are possible.

### Bull

Specify what must go unusually well and which assumptions require new evidence. Do not combine every conceivable upside into one unrealistic case.

## Required scenario fields

For each case include where meaningful:

- key operating / project / clinical assumptions
- financing and dilution
- valuation method
- enterprise and equity value
- value per fully diluted share
- return from current price
- expected date / time to realization
- annualized return
- evidence that would make the case more likely

## Probability discipline

Probabilities are analyst judgments unless externally implied or supported by a well-defined reference class.

Rules:

- label them as assumptions
- probabilities must total 100% when expected value is calculated
- do not use false precision such as 37.4% without a real basis
- prefer ranges when evidence is weak
- do not force probabilities when market-implied thresholds are more informative

Useful alternatives to subjective probabilities:

- market-implied probability
- break-even success probability
- probability required to achieve a chosen return hurdle
- maximum Bear-case probability consistent with an attractive entry

## Expected value

When appropriate:

`Expected value = sum(probability_i × value_i)`

Show the probability-weighted value separately from the Base-case value.

A positive expected value is not sufficient if:

- permanent-loss risk is unacceptable
- liquidity is poor
- financing can impair equity before thesis resolution
- the expected return takes too long
- downside is highly asymmetric

## Annualized return

When a scenario has an approximate time horizon, calculate an annualized return where useful:

`Annualized return = (terminal value / current price)^(1 / years) - 1`

Do not annualize very short event outcomes in a way that implies the resulting extreme annualized number is a realistic repeatable return. For days/weeks, show absolute return and event duration first.

## Time-to-Resolution Gate

Time is a required underwriting variable.

Every final posture must specify:

- expected holding period
- target realization date
- mandatory re-underwrite date
- the reason for those dates
- measurable evidence expected by those dates

### Practical horizon labels

Use the closest useful description rather than forcing exact categories:

| Horizon | Typical use |
|---|---|
| Days / event | binary or near-binary dated catalyst |
| 1-4 weeks | short event/reaction trade |
| 1-3 months | near-term catalyst sequence |
| 3-12 months | earnings, operational, regulatory, drilling, or normalization thesis |
| 1-3 years | operating transformation or development thesis |
| 3-5+ years | structural compounder / long-duration buildout |

### Target realization date

The calendar date by which the main valuation gap should reasonably begin or largely complete closing if the Base case is correct.

Tie it to a mechanism such as:

- earnings revisions
- regulatory decision
- clinical readout
- resource update
- PFS/FS
- construction / production milestone
- margin normalization
- capital return
- multi-year compounding

If no plausible value-recognition mechanism exists within the proposed horizon, reduce actionability.

### Mandatory re-underwrite date

The date when the original underwriting expires and must be refreshed regardless of share-price performance.

Rules:

- event trades: at or immediately after the event / decision window
- 1-12 month theses: usually at the decisive catalyst or no later than the end of the stated horizon
- multi-year theses: normally re-underwrite at least annually unless the user specifies a tighter cadence

The re-underwrite date is not necessarily a sell date. At that date explicitly choose to renew, revise, downgrade, or end the thesis.

### What must happen by the date

State measurable progress requirements.

Examples:

- revenue growth remains above X and margins reach Y
- resource reaches / converts to a defined level
- financing is secured within an acceptable dilution range
- FDA hold is lifted or defined evidence is submitted
- project moves from PEA to PFS with economics inside a specified range
- AI capacity utilization / cloud growth confirms expected returns

If the required evidence fails to arrive by the re-underwrite date, do not silently extend the thesis. Re-underwrite the reason for delay and its valuation cost.

## Duration-adjusted comparison

When comparing ideas, consider both absolute upside and time.

A 30% upside expected in six months and a 30% upside expected in three years are not equivalent.

Where the inputs are sufficiently reliable, compare:

- absolute expected return
- annualized expected return
- downside
- probability of permanent loss
- timing uncertainty
- catalyst dependence

Do not use duration-adjusted precision when outcome timing is inherently unknowable.

## Breakpoints

Prefer decision-relevant thresholds over decorative sensitivity tables.

Examples:

- share price at which expected return becomes attractive
- resource size needed to justify current EV
- margin needed to justify current multiple
- success probability needed to justify current biotech value
- dilution level at which upside disappears
- commodity price at which project NPV falls below EV

These breakpoints should feed the final conditional action rules.
