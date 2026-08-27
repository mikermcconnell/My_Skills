# Social Arbitrage Lane — V3

Use this lane when the potential edge comes from observable consumer, employee, supplier, developer, community, search, app, product, pricing, inventory, transaction, or cultural behaviour that may reach financial results or analyst estimates with a lag.

A popular stock post, influencer opinion, management claim, ordinary breaking-news item, or unexplained price move is not social arbitrage by itself.

Radar detects and preserves the behavioural observation. Research With Confidence determines authenticity, causality, economic materiality, value capture, and whether an expectations gap survives. Full Underwriting determines whether the security is attractive at the current price.

## Existing evidence sources

When available, reuse the Investing repository's existing social-arbitrage evidence rather than creating a parallel scanner:

- `/ai-efficiency/api/social-arb/evidence`
- `/ai-efficiency/api/social-arb/signals`
- `src/services/social_signal_extractor.py`
- `src/services/firecrawl_social_sources.py`
- the Social Signals page for Chris Camillo and Dumb Money research leads.

## Radar tests

1. **Novelty:** when the behaviour began, whether it is accelerating, and whether investors already discuss it widely.
2. **Velocity and breadth:** change in intensity, independent sources, geography, demographic reach, and persistence.
3. **Authenticity:** organic behaviour versus promotion, bots, affiliate incentives, investor echo chambers, review manipulation, or one viral outlier.
4. **Ticker mapping:** the actual public company, segment, geography, product economics, ownership, and whether a supplier or platform captures more value.
5. **Materiality hypothesis:** units, price, share, revenue exposure, margins, estimate sensitivity, and the likely reporting period.
6. **Expectation question:** narrative saturation, analyst assumptions, and why the behaviour may not yet be reflected.
7. **Confirmation and falsification:** the next app rank, traffic, pricing, inventory, channel, search, transaction, guidance, or earnings evidence and expected date.
8. **Persistence:** whether the behaviour survives long enough to matter rather than appearing only around one promotion or market move.

Treat social activity as a lead until the business bridge is independently supported. Do not mistake attention for purchasing, purchasing for revenue, revenue for profit, or a good behavioural signal for an attractive stock.

## V3 observation record

Persist the smallest useful atomic record:

```text
observation_id
first_seen_at
observation_window
original_source
independence_group
behaviour_observed
geography_and_cohort
breadth_and_velocity
authenticity_flags
linked_security_or_thesis
preliminary_mechanism
main_capture_uncertainty
next_confirmation_or_falsifier
next_evidence_date
route
```

Several independent observations are more valuable than a large raw mention count sharing one origin. Group repeated screenshots, reposts, affiliate content, or coordinated claims under one origin.

## Scheduled cadence

- Append genuinely new atomic observations during scheduled runs.
- Promote only after the behaviour shows enough persistence, breadth, or independent confirmation to matter.
- Review cumulative behavioural patterns on the structured weekly slow-burn cadence.
- Check the named confirming or falsifying evidence when due.

Most social-arbitrage leads should route to RWC over a weeks-to-months horizon, not a one-day trade.

## Price-dislocation boundary

When social posts appear only after a large stock move, first treat the case as `PRICE_DISLOCATION_UNEXPLAINED`. Identify the original source and underlying event before treating the discussion as a behavioural lead.

Do not pass Novelty because many accounts repeat the same explanation.

## Hard depth boundary

Radar may identify the observed behaviour, preliminary ticker mapping, plausible materiality, authenticity concerns, and the exact next evidence.

Radar should not complete representative sampling, causal attribution, revenue sensitivity, consensus comparison, valuation, expected-return, or position-size analysis. Route those questions downstream.
