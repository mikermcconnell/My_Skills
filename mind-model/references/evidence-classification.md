# Evidence Classification Guide

## Four separate questions

Before assigning SUPPORT, CHALLENGE, or CONTEXT, classify:

1. **Event novelty:** what changed relative to the prior baseline?
2. **Thesis effect:** probability, timing, intrinsic value, confidence, monitoring, or no change?
3. **Evidence stance:** does this atomic claim support, challenge, or contextualize the exact thesis?
4. **Investment effect:** does any company capture material value and is it attractively priced?

Do not use one label to answer all four.

## Event novelty

Use:

- `GENUINELY_NEW`
- `REPEATED_GUIDANCE`
- `INDEPENDENT_CONFIRMATION`
- `ACCELERATION`
- `DECELERATION`
- `CONTRADICTION`
- `RISK_DISCLOSURE`
- `UNKNOWN`

A new publication date does not establish novelty. Compare the underlying claim with filings, guidance, prior reporting, trial records, forecasts, and the current thesis baseline.

## Thesis effect

Use:

- `INTRINSIC_VALUE_CHANGE`
- `PROBABILITY_CHANGE`
- `TIMING_CHANGE`
- `CONFIDENCE_ONLY`
- `MONITOR_ONLY`
- `NO_CHANGE`

Examples:

- A contract that adds expected cash flow may change intrinsic value.
- A trial result may change approval probability.
- A construction delay may change timing and annualized return.
- Independent customer confirmation may strengthen confidence without changing the forecast yet.
- Repeated guidance normally produces no change.

## Stance starts with the exact thesis

The same claim can support one thesis and challenge another.

Example: `Mandatory safety testing raises the cost of releasing frontier open-weight models.`

- It challenges `open weights rapidly replace proprietary models`.
- It may support or contextualize a defined coexistence thesis.
- It is not automatically a challenge merely because it is negative for one technology.

### SUPPORT

Use when the claim makes the exact thesis or measurable forecast materially more likely.

Test: Would a rational analyst raise probability if this claim were trusted?

### CHALLENGE

Use when the claim lowers thesis probability or raises a named competing outcome.

Test: Which alternative becomes more likely, and why?

### CONTEXT

Use when the claim changes mechanism, scope, timing, uncertainty, or interpretation without clearly moving probability.

Context is not a holding category for inconvenient evidence. State why the claim does not discriminate among outcomes.

## Hybrid and coexistence theses

Define scenario boundaries before evaluating evidence. For each outcome record:

- what it predicts;
- distinguishing operational or market measures;
- falsifiers;
- current probability range;
- resolution date.

Do not call coexistence confirmed merely because both categories continue to exist. Require the material adoption or economics specified in the thesis.

## Counts and independence

- Do not target equal stance counts.
- Do not infer conviction from raw record totals.
- Several claims from one source remain one origin unless they rely on independent underlying evidence.
- Repeated media coverage of one statement is one independence group.
- One high-quality disconfirming fact can outweigh many weak opinions.
- A duplicate event should link to the original evidence rather than create a new probability vote.

## Examples

### New event, no thesis change

A company repeats a long-standing target in a new press release. Classify `REPEATED_GUIDANCE / NO_CHANGE`. It may be CONTEXT or no new evidence record at all.

### Independent confirmation

A customer independently confirms deployment volume previously claimed by the supplier. Classify `INDEPENDENT_CONFIRMATION`. It may SUPPORT and change `CONFIDENCE_ONLY` until financial materiality is quantified.

### Timing challenge

A regulator delays a decision without changing the apparent ultimate probability. The atomic claim may CHALLENGE a dated forecast and have `TIMING_CHANGE`, while the long-run thesis probability remains unchanged.

### Entirely supporting source

Record the supported claims. Do not invent a challenge from methodological limitations unless the source contains a claim that actually opposes the thesis.

### Qualification, not opposition

A source confirms a carrier benefits operationally but shows the earnings impact is immaterial. It can SUPPORT the operational mechanism, CHALLENGE a material-profit forecast, and CONTEXTUALIZE a no-trade conclusion. Classify each atomic claim against the statement it tests.
