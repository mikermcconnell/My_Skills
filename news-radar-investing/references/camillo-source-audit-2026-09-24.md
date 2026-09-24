# Camillo discovery source audit — September 24, 2026

This is implementation-day evidence, not a live feed-health certificate. No private holdings, credentials, document bindings or source-user data are published here.

## Existing code inspected, not deployed or invoked

Investor source reads:
- src/services/firecrawl_social_sources.py, blob 3d556985a96d0501c0a9a84049ebfb588bc9d369: default searches focus on Chris Camillo, Dumb Money and stock terminology. The retail-test examples also contain stock/public-company wording. The service requires configured credentials, contains credit controls and blocks several social domains. No paid call, configuration change or bypass was performed.
- src/services/social_signal_extractor.py, blob c25c58490932c72fc6758e2bf73ad7ecc0db0c9d: extraction requires a recent dated source, limits the inspected text, drops candidates with no recognized symbols/companies/trend terms, and scores known symbols/trade categories positively. Those are not suitable sole gates for unseeded behaviour/capability discovery or newly significant old facts.

The new Radar path therefore uses public-source retrieval directly and treats the older outputs as supplemental. It does not pretend to patch or redeploy Investor. Search of the available connector directory returned no MikeInvestor integration in this implementation session; authenticated runtime collection and storage endpoints were not verified. No endpoint is called operational solely because it is named in a skill.

## Public source-access probes

The web tool opened the following on September 24:
- https://news.ycombinator.com/shownew — readable chronological index. Product claims/linked demonstrations were not independently tested.
- https://www.producthunt.com/ — readable launch index; promotional context must remain visible. No adoption inference was made.
- https://www.reddit.com/r/BuyItForLife/new/ — readable result, but retrieval metadata indicated a crawl three weeks earlier. Classified PARTIAL_CACHED, not fresh intraday monitoring.
- https://store.steampowered.com/charts/ — index readable; underlying quantitative series and time-window completeness not validated.

These probes establish limited tool access, not a completed four-family Radar discovery pass. They produced no approved investment case, baseline, trade or source-history migration. Native container network access failed on repository cloning; connected GitHub reads/writes remain the configuration path.

## Primary documentation checked

- https://developers.google.com/youtube/v3/docs/search/list — search-index ordering can be delayed/incomplete; use a known channel's uploads playlist for newest uploads when supported. No API credentials or transcript access were assumed.
- https://support.google.com/trends/answer/4365533?hl=en — sampled and normalized search interest, not absolute users/sales.
- https://developers.tiktok.com/products/research-api/ — eligibility/access restrictions; do not assume this investing workflow qualifies for research access.
- https://github.com/HackerNews/API — official API documentation read; this is not evidence that a persistent collector was deployed.

## Validation scope

31 synthetic Python contract tests passed locally for early intake, unknown mappings, no financial/Core-price gate, old source dates, source attribution, future timestamps, duplicate connections, existing-strategy isolation, query plans and source coverage. These exercise the helper's declared inputs, not the truthfulness of model-supplied assertions or real-world performance.

Pending operational verification: first completed scheduled post-change Radar run; actual private-journal read/write receipts; full source coverage and latency; independent discovery yield; source-platform access beyond the probes. Follow the first-five-run calibration in camillo-discovery.md. No claim of guaranteed signal capture or historical investment returns.
