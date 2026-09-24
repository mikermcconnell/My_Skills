# Active News Radar Version

```text
active_version: 3
status: ACTIVE
activated_at: 2026-08-27
analytical_revision: 2026-09-24-camillo-observation-first
scan_cadence: 08:00, 11:00, 15:00 America/Toronto, daily
skill: news-radar-investing/SKILL.md
strategy_contract: investment-strategy-lanes/SKILL.md
camillo_discovery_contract: news-radar-investing/references/camillo-discovery.md
camillo_source_register: news-radar-investing/references/camillo-source-register.json
monitor_contract: news-radar-investing/MONITOR_V3.md
run_contract: news-radar-investing/references/v3-run-contract.md
source_routing_contract: news-radar-investing/references/source-and-routing-rules.md
source_feed_contract: news-radar-investing/references/primary-source-feed-map.md
emerging_signal_contract: news-radar-investing/references/emerging-signal-lens.md
newsletter_intake_contract: news-radar-investing/references/newsletter-intake.md
specialized_lanes_contract: news-radar-investing/references/specialized-lanes.md
price_monitor_contract: news-radar-investing/references/price-monitor-live-source.md
sell_discipline_contract: news-radar-investing/references/sell-discipline-and-closeout.md
event_reaction_mechanics_contract: news-radar-investing/references/event-reaction-strategy-mechanics.md
nancy_pelosi_tracker_contract: news-radar-investing/references/nancy-pelosi-tracker-lane.md
ai_efficiency_watch_contract: news-radar-investing/references/ai-efficiency-watch.md
ai_efficiency_watch_state_contract: news-radar-investing/references/ai-efficiency-watch-state.md
ai_efficiency_watch_activated_at: 2026-09-18
ai_efficiency_watch_first_weekly_summary: 2026-09-25 15:00 America/Toronto
mandatory_specialized_lane_checks: 11
output_contract: investment-firm-output/SKILL.md
output_contract_version: 12
routine_radar_title: Investment Firm — Radar
routine_radar_sections: New news and opportunities; Changes to existing investment cases; Stock monitor — Buy / Hold / Wait / Sell
protected_discovery: bounded urgent risk -> Core broad pass plus Camillo observation pass -> routine continuation
news_universe: not limited to holdings, tickers, known brands, AI or investing personalities
novelty_memory: source/observation identity AND connection identity; canonical plus verified dated fallback
price_monitor_source_classes: CANONICAL; LEGACY; PORTFOLIO DEFENSE
price_monitor_proximity_band: 5_percent
price_monitor_rows: strategy_case + exact_security + applicable_lot; no ticker-only collapse
stock_table_schema: combined_action_queue_v2_with_event_reaction_mechanics
report_format_version: 8
strategy_annotations: additive presentation/manifest metadata only; no new backend enums implied
routine_radar_publication: one combined report per existing slot, including unchanged eligible monitor rows
narrative_publication: existing weekday Daily Brief at its actual task schedule; no cadence change
standing_view: existing Decision List; Daily Brief retains original cutoffs
markdown_artifact_required: false
```

## Authority and read order

Read the current SKILL.md and its full mandatory read order from a consistent current repository revision where practical. The shared strategy contract and camillo-discovery.md precede inherited Camillo-specific restrictions in the run/source/social/emerging references. The original Core workflow, four broad source families, all eleven specialist checks, newsletter intake, clinical overlays, quote/legacy/defense controls and sell rules remain required. This pointer no longer duplicates their changing details.

## Discovery and publication

Every scheduled scan must protect BOTH Core broad discovery and Camillo's four differentiated observation checks before routine holdings expansion. A P0 emergency can preempt, with a recorded skipped source/category/window and recovery. Native public-web discovery continues when private state or the older social collector is unavailable. No fixed number of signals or new tickers is required.

Surface credible Camillo EARLY observations before financial confirmation. A capability-led or single-origin signal can qualify with a plausible consequence and next check. Keep facts, claims and speculation separate. Unknown public-company mapping or a stock above a Core entry target is not a discovery veto. A new consequence connected to an old public fact is not automatically a duplicate announcement.

Both strategies appear in the existing three sections. Research-only Camillo cases are not active trade monitors. Core and Camillo conclusions, clocks and exact instruments remain separate; actual exposure is counted once. Event Reaction retains its own manifest mechanics before the other monitoring queues. No retagging or strategy conversion is inferred.

## Source, state and persistence

Use actual source receipts, observed publication windows and defined samples; distinguish COMPLETE_FOR_DECLARED_SAMPLE, PARTIAL, UNAVAILABLE and NOT_RUN. Registration, test fixtures, a query plan, task success and saved configuration do not prove actual collection, organic demand, investing skill or delivery. Preserve fallback-seen history and original first detection; do not revive consumed price triggers or disabled monitors.

The source register's implementation-day audit is dated context, not a live feed-health record. Reverify access each run. Keep actual source-health receipts, cases and portfolio context in existing private supported state/fallback, not public GitHub. A missing backend ticker/metadata field cannot justify dummy tickers or Core-baseline overwrite.

Preserve existing per-slot stock-monitor:YYYY-MM-DD:HHMM:America_Toronto identities and the actual schema/cutoff of older reports. Version 8 adds Camillo discovery receipts/cards and connection metadata in compatible reporting only. It does not declare API support for new fields. Current native write schemas always control payloads.

Radar appends to the existing private Reporting Journal; the existing Daily Brief owns Decision List updates with revision protection/read-back. Preserve Friday AI-efficiency fixed-cohort/backfill/quality controls and the first eligible boundary above. The source-access and first-five-post-change-run check belongs in existing calibration/brief work, not a new audit task.

## Unchanged authority

No change to accepted theses, probabilities, fair values, holdings, risk budgets, thresholds, review dates, trade proposals, fills, optional-workflow flags or deployed application code is authorized by this discovery configuration. Existing urgent risk channels, clinical safeguards, disclosed-trade provenance rules, price validation and user/broker execution remain. Full research stays available. Readiness, saved state, a running worker and actual delivery are separate facts.
