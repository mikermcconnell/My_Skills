# Return Hurdle, Opportunity Cost, and Portfolio Handoff

## Required-return rule

Use the user's or strategy's actual required-return rule when it is available from the prompt, current project, or authorized portfolio context.

Do not invent a personal hurdle. If none is supplied:

1. state `Required-return hurdle: not supplied`;
2. report expected annualized return and downside;
3. show sensitivity to reasonable illustrative hurdles such as 10%, 15%, and 20% annualized when useful;
4. state the price or operating assumptions required to clear each hurdle;
5. avoid implying that the illustrative hurdle is Mike's policy.

For event-driven or binary ideas, also show the break-even success probability and the probability required to meet the hurdle.

## Opportunity-cost comparison

Choose the closest realistic alternative, not an arbitrary benchmark. It may be:

- cash or short-duration government securities;
- a broad index;
- a sector ETF;
- a directly comparable company;
- an existing holding competing for incremental capital;
- another active underwritten idea.

Compare:

- expected and annualized return;
- Bear-case loss and permanent-loss mechanism;
- evidence confidence;
- time to resolution;
- liquidity and gap/event risk;
- correlation and thematic concentration;
- currency, listing, and implementation complexity.

A lower-return idea may still be preferable if confidence, liquidity, duration, or downside is materially better. Explain the tradeoff rather than ranking only by point-estimate return.

## Portfolio handoff fields

Provide:

```text
security
posture
price_and_date
entry_condition
expected_return
expected_annualized_return
bear_downside
base_return
bull_upside
probability_confidence
expected_holding_period
target_realization_date
mandatory_reunderwrite_date
liquidity_and_spread
event_or_gap_risk
financing_and_dilution_risk
factor_and_thematic_exposures
customer_supplier_or_macro_dependencies
correlation_concerns
currency_and_listing_issues
closest_alternative
hurdle_premium_or_shortfall
add_evidence
trim_evidence
exit_or_kill_evidence
```

The portfolio workflow owns exact size, account, concentration, hedges, tax, entry implementation, and trade execution.

## Price-sensitive conclusions

When the thesis is sound but the hurdle is not met, calculate one or more of:

- maximum entry price for the Base case to clear the hurdle;
- maximum entry price for probability-weighted value to clear the hurdle;
- operating milestone required at the current price;
- lower-risk evidence that would justify accepting a smaller return premium.

State the condition precisely enough to monitor.
