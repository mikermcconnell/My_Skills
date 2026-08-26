# Event Tree and Payoff Rules

## Freeze the information set

Every event-trade analysis must record:

```text
event and security
analysis timestamp and timezone
current tradable bid/ask or defensible price
market status
public information available at the cutoff
pre-event expectation source or proxy
intended entry and holding window
```

Do not use later evidence to improve the pre-event probability without labelling the analysis as an update.

## Define states correctly

States should be:

- mutually exclusive;
- collectively exhaustive enough for the decision;
- economically distinct;
- tied to observable outcomes and time windows.

Avoid a cosmetic Bear/Base/Bull tree where every state is some degree of success.

Examples:

### Regulatory or clinical event

- approval or success with stronger-than-expected label/data;
- expected approval or success;
- approval with restriction, warning, delay, or ambiguous data;
- complete response, hold, failure, or rejection;
- event postponed or information incomplete.

### Earnings event

- beat and raise on the key value driver;
- headline beat but weak quality or unchanged/lowered forward guide;
- in-line result;
- miss or guide-down;
- accounting, financing, or one-time issue that changes interpretation.

### Transaction or legal event

- approval/close on current terms;
- approval with remedy, delay, price change, or financing adjustment;
- extension or vote delay;
- rejection, termination, or adverse ruling;
- alternative bidder or settlement where evidence supports it.

## Probability sources

Label each probability as one or more of:

- `MARKET_IMPLIED`
- `HISTORICAL_BASE_RATE`
- `PRIMARY_EVIDENCE_DERIVED`
- `CONSENSUS_OR_SURVEY`
- `ANALYST_JUDGMENT`
- `UNKNOWN`

A market-implied probability is not automatically correct. It is a comparison point. Adjust for time value, deal spread mechanics, dividends, financing, borrow, option structure, and multiple outcomes when material.

Do not assign precise probabilities merely to make the table total 100%. Use ranges and a sensitivity analysis when evidence is weak.

## Price and payoff states

Use executable or defensible price ranges. Distinguish:

- immediate reaction price;
- settlement or later intrinsic-value path;
- peak intraday print;
- price reachable after the user could reasonably execute.

Do not use an after-hours spike as the success payoff if normal liquidity was unavailable.

For each state identify:

```text
entry price
exit price range
return before costs
probability
spread/slippage/fees/borrow/option cost
net payoff
time to exit
halt or liquidity assumption
```

## Expected value

For states `i`:

```text
expected net return = sum(probability_i * net return_i)
```

Use probability ranges to show sensitivity. A positive expected value does not override unacceptable adverse-state loss or inability to exit.

## Break-even probability

For a two-state long trade with gain `G` and loss `L`, both expressed as positive magnitudes:

```text
p_break_even = L / (G + L)
```

For a short trade, define payoffs from the short entry and include borrow and squeeze loss.

For multi-state trees, solve the probability or entry price that sets total expected net payoff to zero while holding other assumptions fixed. State which assumptions are fixed.

## Maximum acceptable entry price

Solve for the price where the trade no longer meets the required expected payoff or loss limit. Do not assume the current price remains available after confirmation.

A useful output is:

| Entry price | Expected net return | Adverse-state loss | Break-even probability | Posture |
|---:|---:|---:|---:|---|

## Event delay

Include delay when it is plausible. Delay can change:

- time value and annualized opportunity cost;
- cash burn and financing;
- merger spread and borrow cost;
- option expiry and volatility;
- information leakage and positioning;
- regulatory or clinical probability;
- ability to hold the trade.

A delayed event is not automatically the same as the expected state.

## Fundamental versus recognition effect

Classify each state:

- **Fundamental value change:** changes cash flow, asset value, financing, or probability.
- **Recognition event:** reveals or highlights value already present.
- **Sentiment/liquidity effect:** changes price without durable value evidence.

A trade can exploit recognition or sentiment, but the holding period and exit rule must reflect that rather than assuming permanent intrinsic-value creation.

## Post-event conversion rule

An event trade may become a candidate for Full Underwriting after the result, but it never automatically converts into a long-term hold.

Before conversion, require:

- a fresh current price;
- revised factual and expectations baseline;
- capital structure and ownership;
- long-term economic engine;
- reverse valuation and scenarios;
- time-to-resolution and hurdle;
- independent challenge where applicable.
