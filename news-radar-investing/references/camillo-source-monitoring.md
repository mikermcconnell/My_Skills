# Camillo source monitoring: rankings, searches, reviews and retail

Approved September 24, 2026. Read camillo-discovery.md and camillo-market-source-pack.json alongside the existing source register. This adds data collection and comparable history to the existing observation-first pass. It creates no new strategy, task, portfolio risk limit, subscription or trade authority. Core and Event Reaction rules remain unchanged.

## What is now required

Use two modes: **discovery** scans the declared chart/topic/category universe for unfamiliar products and use cases; **tracking** follows selected observations with the sources most likely to change the conclusion. Do not turn the app or product list into a permanent whitelist. Missing ticker/valuation/retention still does not suppress a credible EARLY observation.

At each existing Radar slot check source versions and due collection windows under the pack. Reuse a source retrieved in the existing four Camillo checks instead of adding repetitive searches. Protect Core discovery and all existing specialist obligations. Bound failures: one alternative method, then an explicit gap; do not spend the run retrying restricted platforms. Follow slower datasets at their actual update cadence, not the report cadence.

Apple top-free US/CA/GB is the initial structured chart universe, requested depth 100. Paid charts are separate daily checks distributed across the slots. Device scope is **provider_unspecified** unless actually stated; do not assume a generic Apple feed is iPhone-only. Android begins with a readable US applications chart and separately verified country expansion. An AppBrain fallback is explicitly third-party and is never spliced into an Apple or direct-Play historical stream. Free, paid, grossing, overall, apps-only, games and category ranks are distinct.

Check Google Trending Now for unknown product/category/use-case leads; retain irrelevant trends as skipped rather than inventing investment relevance. Explore/related-query tracking is a separate sampled-index dataset requiring actual access. Ordinary web search finds sources; it is not a Google search-volume API. Use the actual engine/tool provenance and never access private search history.

Use Amazon Best Sellers/Movers & Shakers, Pinterest Trends and exact retailer pages within the rotating non-AI pass. Sources requiring accounts or unavailable to tools remain explicit gaps, not promises of coverage. No paid data, CSV purchase, API registration or business-account creation is approved by this source configuration.

## Comparable records, not screenshots of a rank

For a chart capture retain:

`schema; provider; platform; country; device; category; chart; source_url; source_time; source_time_precision; collected_at; capture_method; requested_depth; captured_prefix_depth; rows[{stable id, name, developer, rank}]; snapshot_id; stream_id; research_only`.

Use scripts/camillo_source_snapshots.py to validate and compare when execution is available. It accepts complete Apple JSON bodies or normalized, independently checked chart excerpts. The optional fetch-apple command uses a fixed allowlist and fails closed on network errors/redirects; it neither changes canonical state nor deploys a continuous service. In a tool-only run, retrieve with authorized web/connector tools, normalize the inspected rows and apply the same rules manually. Manual extraction must be labelled. An unexecuted parser is not a tested collector.

A complete top-five excerpt of a top-100 request has captured_prefix_depth=5, not 100. Noncontiguous observed rows have null prefix depth. Stable IDs are source-specific app IDs/package IDs/canonical provider URLs, not guessed names or tickers. Verify identity before cross-source/country matching; mismatched product links are quarantined for mapping, not joined into a false trend. App renaming alone is not a new product.

Compare only matching provider/platform/country/device/category/chart definitions and forward-moving source versions. A repeated retrieval of the same daily table is SAME_SOURCE_VERSION, not another confirmation. A changed table at the same source timestamp is a SOURCE_REVISION_OR_SCOPE_CHANGE, not measured acceleration. Unknown or changed timestamp precision cannot support a timed-growth assertion. A newly stamped but unchanged chart is UNCHANGED_RANKS.

Report movement as ordinal positions, never inferred download/revenue multiples. A missing item is NOT_OBSERVED_IN_CURRENT_PREFIX, not zero activity or a known rank of 101. Entry/exit inference needs equal, completely observed prefixes; changed or partial scopes permit only comparisons of IDs actually observed in both. A first capture is BASELINE_ONLY. It can still motivate a qualitative investigation, but it is not evidence of a climb, acceleration or persistence.

For Google/Pinterest indexed series preserve provider, query/topic definition, geography, category, search type/metric, window, granularity, normalization/scaling group, source date and collection time. Separate exports normalized to their own maximum must not be stitched together. Save the full comparison window when using normalized website data, preserve censored '<1' as a bound/null plus raw string, and distinguish unavailable from zero. Trending Now volume buckets and source-reported percentage changes are separate from Explore's 0–100 index. Do not transform search interest, pin saves, chart position or review sentiment into customer counts.

## Persistence and start-up

Use the current authorized source/sequence storage if its schema can represent these observations. Otherwise append structured **CAMILLO_SOURCE_SNAPSHOT_V1** blocks to the existing private Reporting Journal with a stable snapshot_id and fresh revision protection/read-back. Append source failures separately as **CAMILLO_SOURCE_RECEIPT_V1**. No new database, public portfolio record, dummy ticker or issuer-wide Core baseline overwrite. Local JSON is a transfer artifact, not durable shared history.

Before each collection, find the latest verified matching stream records, their original source time and captured scope. Two or more comparable, distinct source versions establish an observed history; two calls to the same version do not. No backfilling guessed historical rankings from current results or provider movement arrows. Preserve raw source references, source updates and extraction limitations; do not rewrite old observations after a provider correction. Use a new revision-linked snapshot.

The implementation bootstrap deliberately stores small verified excerpts, not claimed full-chart captures. Subsequent runs should expand towards requested depth as access permits and label scope changes. Do not count configuration tests or this bootstrap as a completed broad Radar scan. If journal saving fails, provide the readable artifact/report, preserve PERSISTENCE_UNVERIFIED and do not claim cross-run memory works.

## From an anomaly to a useful connection

Look for unfamiliar entrants, unusual climbs, cross-country/platform observations with verified identity, reversals, category clusters and changes in practical use. No universal numeric score or minimum source count. A new series, a small sample or a provider outage must not suppress other strong qualitative evidence. Avoid explaining every tiny rank shuffle or turning the chart into a routine long app list.

When a candidate merits follow-up, read recent reviews and release notes. Start with a bounded chronological sample and deliberately inspect disconfirming accounts; record the actual n, date range, country/language, version, retrieval/sort method and whether the sample was selected rather than representative. Separate attention, trial, purchase, repeated use, payment, switching, reliability and abandonment. Do not produce a population sentiment percentage from a convenience sample. Ratings totals are not the number of written reviews actually inspected.

Check promotions, featured placement, seasonality, supply restriction and common causes. Search interest, chart rank and video activity driven by one campaign are not three independent causes. Two analytics vendors may describe the same underlying store data. Distinguish dataset corroboration, origin independence and causal independence.

Then ask who benefits, who must spend or supply more, what existing relationship becomes important, what may be displaced, and what investors may notice next. Keep the chain simple. Verify product-to-owner-to-security and supplier relationships; source labels are not proof of ownership or economic capture. First-hand reviews do not establish undisclosed infrastructure sourcing. Old facts can become newly consequential without becoming new announcements.

## Visible reporting and handoffs

Within CAMILLO — New news and opportunities show only meaningful candidates under the existing EARLY/BUILDING/RWC NOW format. Include the exact observed metric and scope, baseline-only versus measured delta, public-source or provider provenance, simple connection, uncertain bet, next check and falsifier. Research-only observations remain distinct from active trade monitors and completed underwriting.

Add one compact coverage line: which datasets were retrieved, carried forward unchanged, partial, blocked or awaiting access. Do not label all registered sources 'monitored' without receipts. Research and underwriting inherit these limitations and distinguish information-edge judgment, instrument/payoff and portfolio permission. Core buy prices are not Camillo discovery gates; current price/payoff still matters to a trade decision.

The existing Daily Brief synthesizes only consequential source findings, case progress and access gaps. It does not duplicate full chart histories. Use the existing first-five-run review for source-version deduplication, unknown-ticker retention, complete-prefix handling, false promotion signals, detection/surfacing delay, and journal recovery. No scheduled tests are reported passed in advance.

## Documentation and tested access

Implementation-day web probes found ordered Apple free-app entries for US/CA/GB and their source timestamps; a US paid-feed header; a dated AppBrain US applications table; Google Trending Now UI rows (first page only). Google RSS and Amazon Movers & Shakers retrieval failed; Pinterest returned a shell without usable metrics. Quantitative Google Explore data, CA/GB Android/paid coverage, full charts and paid-provider credentials are not verified. These are dated observations, not permanent access states.

Primary documentation: https://developers.google.com/search/apis/trends ; https://support.google.com/trends/answer/4365533?hl=en ; https://help.pinterest.com/en/business/article/pinterest-trends ; https://developers.google.com/android-publisher/reply-to-reviews . Review APIs for one's own app do not imply competitor-data access. Google Trends alpha access must be verified, not assumed. Recheck current provider terms and tool access before adding paid/API adapters.
