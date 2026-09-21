# Active News Radar Version

```text
active_version: 3
status: ACTIVE
activated_at: 2026-08-27
analytical_revision: 2026-09-21-news-discovery-correction
scan_cadence: 08:00, 11:00, 15:00 America/Toronto, daily
skill: news-radar-investing/SKILL.md
monitor_contract: news-radar-investing/MONITOR_V3.md
run_contract: news-radar-investing/references/v3-run-contract.md
source_routing_contract: news-radar-investing/references/source-and-routing-rules.md
source_feed_contract: news-radar-investing/references/primary-source-feed-map.md
specialized_lanes_contract: news-radar-investing/references/specialized-lanes.md
price_monitor_contract: news-radar-investing/references/price-monitor-live-source.md
sell_discipline_contract: news-radar-investing/references/sell-discipline-and-closeout.md
nancy_pelosi_tracker_contract: news-radar-investing/references/nancy-pelosi-tracker-lane.md
price_monitor_mode: dynamic_live_source
price_monitor_audit_format: action_sorted_queue
price_monitor_rows: one_per_security_or_distinct_instrument_decision
price_monitor_proximity_band: 5_percent
ai_efficiency_watch_contract: news-radar-investing/references/ai-efficiency-watch.md
ai_efficiency_watch_state_contract: news-radar-investing/references/ai-efficiency-watch-state.md
ai_efficiency_watch_activated_at: 2026-09-18
ai_efficiency_watch_weekly_summary: Friday 15:00 America/Toronto, inside the Daily Brief
ai_efficiency_watch_first_weekly_summary: 2026-09-25 15:00 America/Toronto
mandatory_specialized_lane_checks: 11
output_contract: investment-firm-output/SKILL.md
output_contract_version: 4
output_contract_approved_at: 2026-09-21
routine_radar_title: Investment Firm — Radar
routine_radar_sections: New news and opportunities; Changes to existing investment cases; Stock monitor — Buy / Hold / Wait / Sell
routine_radar_publication: one combined report with each existing 08:00, 11:00 and 15:00 run
protected_broad_discovery: after bounded urgent-risk triage, before routine deep reconciliation or stock-table assembly
news_universe: not limited to current holdings, watchlists, accepted underwritings or active themes
stock_table_publication: inside each combined Radar report, including unchanged rows
novelty_memory: accessible canonical Event Ledger plus verified dated fallback / Reporting Journal
narrative_publication: one weekday 15:00 Daily Brief for synthesis, not duplicate full news/stock reports
other_publication: exceptional urgent Action Alerts and material unsaved-finding fail-safe
standing_view: existing Investment Firm — Decision List, maintained by Daily Brief with original cutoffs
markdown_artifact_required: false
```

## Single baseline and read order

Every scheduled Radar task reads this pointer, the current skill, monitor/run/source/feed/specialized/price/sell contracts, disclosure/AI-efficiency references and latest shared output skill. The feed map is now a required run input, not merely an audit reference. Where practical read from a consistent current commit and record it. Analytical Radar version remains 3; output contract version is 4.

The core skill, run/monitor instructions, source/feed rules, specialized lanes and price lane have been reconciled in place. Do not restore obsolete stock-only, always-visible lane-dump or Daily-Brief-only news behavior. All eleven checks, gates, source rules, specialized evidence and execution boundaries remain required.

## Discover and publish news, not just existing stock status

Do a bounded initial urgent-risk screen, then the protected open-universe discovery pass before routine old-case expansion, thesis deep work or full quote-table assembly. Search current cross-market issuer news, filings/operating/financing, official decisions and industry/customer/supply-demand changes without restricting queries to known tickers. Document actual queries/feeds, windows, markets and gaps. P0 may preempt; record incomplete discovery and recover. Do not imply public-news access requires a working private portfolio connector.

Publish supported material findings in the current combined report, even before RWC/underwriting makes a trade decision. Show NEW DEVELOPMENT, NEW EVIDENCE — EXISTING STORY, LATE DETECTION or NOVELTY UNVERIFIED with original dates and exact next questions. Outside-known-universe status is separate and verified or unknown. Unfamiliar ticker count is not a goal; no story quota or lowered gates.

Keep the new-news section first unless urgent risk leads, changed cases second and the complete stock table third. Include unchanged HOLD/WAIT stock rows but do not retell unchanged old cases as news. Market context and discovery coverage are compact. One combined output per existing slot, not a separate news report plus separate table.

## Memory, source state and action boundaries

Read verified fallback seen-history as well as canonical event records. A fallback-only saved discovery is already seen even when a canonical write failed; preserve its first-detected date and persistence gap. Do not count it as new again. This does not promote fallback prose to an accepted thesis, active monitor, completed research or delivered notification. Missing history means novelty unverified.

Live canonical state owns monitor membership/actions/consumed/re-arm behavior. Exact quotes and stored levels remain separate; missing fields are shown narrowly. Accepted research absent from app monitors can be shown only as labelled reference/unlinked coverage, not silently activated. A price hit is REVIEW until actual current downstream gates support a plain recommendation. Fair value is not automatically a sell threshold; stocks, CDRs, options, currencies and strategies remain distinct.

Use the existing per-slot `stock-monitor:YYYY-MM-DD:HHMM:America_Toronto` issue identity for compatible readers, now with combined report format 4 and both news and stock content. A title change does not justify a duplicate issue. Preserve canonical evidence IDs, original cutoffs, prepared/delivered distinction and the Daily Brief's independent window. Saved/last-run/notification flags are not actual delivery receipts.

Radar appends research and snapshots to the existing private journal; Daily Brief remains the scheduled writer of the existing standing view. Preserve newer manual snapshots and unresolved cases. The simultaneous afternoon report must not be assumed completed. The brief provides synthesis/progress and Friday aggregation without reproducing the full Radar output; it is not the sole place new news appears.

## Specialist and rollout safeguards

Keep official House PTR owner/trade/filing/range/option-return rules, dynamic current expert roles and the AI fixed cohort/backfill/state adapter, costs/quality/confounders and first-week boundary. New specialist evidence may appear intraday; the full weekly AI breadth summary stays in Friday's brief. No new rubric, monitor or task.

Extend the existing first-five-brief comparison with actual discovery-pass completion, outside-known-universe coverage, unique-origin new/evidence/late counts, fallback-aware duplication, same-run inclusion of material news, unchanged-case suppression and stock-row retention. Metrics are diagnostics, not quotas or claims of superior returns. Keep unsupported enrichment in the run manifest/fallback rather than strict production payloads.

No change to investment theses, probabilities, fair values, sizing, thresholds, review dates, holdings, proposals, fills, optional-workflow flags, application deployment or broker authority is authorized by this reporting/search correction. Preserve existing application risk-alert channels until verified replacement. Configuration saved/read-back and actual corrected scan/persistence/delivery are separate evidence; notification-channel limitations remain explicit.
