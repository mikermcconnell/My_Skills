# Google Trends: real collection, bounded refresh, honest coverage

Revision: September 25, 2026. Scoped supplement to camillo-source-monitoring.md. This replaces the previously missing Google data-fetch path; it does not replace Core discovery, the other Camillo sources or investment gates.

## Verified starting point

At 2026-09-25 12:27 UTC the public-source GitHub job for commit e434e16fa6a7b51b56b9b4e4833ab0e4fd954b95 retrieved ten U.S. RSS trend items and a 31-date U.S. interest-over-time response for the literal search terms PineDrama and Ray-Ban, August 25–September 24. Run 36134991858 / job 108070820816; source receipt and actual JSON were read, not inferred from green tests. This was a connection test, not a complete Radar run or proof of an investment edge. The local chat execution environment failed DNS and the web reader failed to expose those data bodies; a network-enabled GitHub runner succeeded. Do not generalize those local failures into a Google outage.

## Two distinct data sources

1. Public Trending Now RSS: https://trends.google.com/trending/rss?geo=US (country configurable). Returns a rolling selection, not every trending topic and not a product's history. Keep original item dates and censored traffic text such as 20K+; do not infer exact volume or no demand when an item disappears. Continue the existing UI discovery samples where useful; RSS does not certify full coverage.
2. Public Explore website timeseries: scripts/camillo_google_trends.py uses the anonymous website JSON requests and scripts/camillo_trends_worker.py normalizes the result. This is an **undocumented public website interface**, NOT Google's application-gated official alpha API or a guaranteed production SLA. No Google login, paid provider, private account access, IP rotation or CAPTCHA bypass. Stop on 401/403/429 and respect request/time budgets.

Google primary references: https://developers.google.com/search/apis/trends ; https://developers.google.com/search/blog/2025/07/trends-api ; https://support.google.com/trends/answer/4365533?hl=en . Website responses have their own normalization; actual alpha access requires separate verification.

## How the existing Radar obtains data

Prefer running the current worker in an available, authorized network-enabled runtime. Example:
`python news-radar-investing/scripts/camillo_trends_worker.py --terms-json '["PineDrama","Ray-Ban"]' --country US --output-dir <new-local-directory>`.
Custom public terms and explicit start/end are supported by the CLI; the default ends yesterday and includes the preceding 30 days. This default seed is a connection/tracking scope, not a whitelist for all independent Camillo discovery. Uncollected candidate terms remain NOT_CHECKED, not no growth.

When the chat runtime cannot reach Google, use the repository's existing `.github/workflows/camillo-trends-probe.yml` job. It has **no schedule**. It is manually dispatchable and can be refreshed through supported GitHub `rerun_workflow_job` for an eligible completed live-probe job. A rerun uses that job's frozen code/inputs: it does NOT add a newly discovered term or update to a later code revision. Inspect the original event, code revision, terms, geography and live-step condition. A tests-only job is not an eligible live source worker. To use different terms, use an actually supported dispatch with explicit public inputs or the CLI, not a fictitious dispatch action. Do not publish private case state in workflow inputs or logs.

At each existing Radar slot, first inspect matching snapshots/receipts and GitHub job state. Reuse source data fetched for that slot; do not trigger twice. When due, allow at most one bounded invocation of this read-only-source workflow (never a trading/deployment workflow). An HTTP access/rate block pauses automatic retries until its stated retry interval or at least the next day; a local DNS failure is separately classified. No identities, proxies or credentials are changed. If execution is pending, record COLLECTION_PENDING, continue the protected broader scan, and inspect once again before publication. Do not create another automation, wait indefinitely or call a submitted job completed. Task schedules and report format remain unchanged.

Read actual completed job logs or the attempt-specific artifact, check the public-source live step, then validate the receipt and data. A green unit-test job alone is not connection success. Preserve job/run/attempt, code SHA, retrieval times, requested terms/window, actual row count and source limitations. Artifacts expire after seven days; a link alone is not permanent history. Copy verified relevant records into the existing authorized private source store/Reporting Journal. No new investment database, Core baseline overwrite or dummy ticker.

## Interpretation and comparison

The worker keeps provider values and hasData flags. hasData=false is null for analysis, NOT zero searches. '<1' remains censored/null with original text. Partial-period flags remain explicit; absent flags are unknown rather than claimed finality. A generic Ray-Ban search is not specific to smart glasses; terms are not topics and names can be ambiguous.

Keep terms/order, country, category, search type, timezone, absolute window, bin timestamps and normalization together. Each complete response has a content-derived ID and scaling group. Unchanged data fetched later is SAME_DATA, not corroboration. A changed definition is INCOMPARABLE_DEFINITION; a revised response in the same window is REVISED_OR_EXTENDED_RESPONSE, not automatically increased demand. Analyze time movement WITHIN one full current response; never concatenate independently normalized exports. New RSS items and changed RSS membership are different from product growth.

The raw first connection test used parser-level rows with hasData=false beside a displayed 0. Later worker records null those observations while retaining provider_values. Treat that as an extraction/normalization revision, not a market change; preserve the original raw result. Two distinct retrieval times do not prove a new source version. A later same-data result is still a valid repeat-connection test.

## Durable receipts and visible status

Append `CAMILLO_GOOGLE_TRENDS_SNAPSHOT_V1` for schema camillo_google_trends_v1 and `CAMILLO_GOOGLE_TRENDS_RECEIPT_V1` for successes/failures/repeats, using stable content IDs and fresh revision protection/read-back. Preserve compatibility with the existing CAMILLO_SOURCE_* envelope if its actual supported schema allows the Google kind; never coerce a time series into a rank table. Read both Google-specific and older source receipts during recovery. Keep full source rows or an actual durable content attachment, not only an expired artifact URL.

Report separately: RSS discovery status/scope; product-history collection status/terms/window; persistence status; and whether a later comparable version exists. Initial data can support an EARLY research question but not a claimed acceleration relative to a nonexistent earlier capture. Introduce unfamiliar products in plain language before metrics. Read current source receipts rather than permanently inheriting a dated NOT_RUN flag or a one-time success.

A source check cannot change portfolio risk, holding strategy, price thresholds, underwriting conclusions or execution permissions. No data subscription or authenticated alpha connection is created by this repair. Keep actual future scheduled execution and notification delivery UNVERIFIED until observed.
