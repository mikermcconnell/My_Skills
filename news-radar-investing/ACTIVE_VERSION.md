# Active News Radar Version

```text
active_version: 3
status: ACTIVE
activated_at: 2026-08-27
analytical_revision: 2026-09-25-unified-radar-trigger-only-er
routine_publisher: Investment Firm — Radar
routine_task_count: 1
scan_cadence: 08:00, 11:00, 15:00 America/Toronto, daily including weekends
separate_daily_brief: false
daily_synthesis: integrated into 15:00 Radar
weekly_synthesis: integrated into Friday 15:00 Radar
standing_view_owner: unified Radar, newest verified completed snapshot only
event_reaction_display: confirmed-trigger alerts only; no routine table or quiet placeholder
skill: news-radar-investing/SKILL.md
strategy_contract: investment-strategy-lanes/SKILL.md
monitor_contract: news-radar-investing/MONITOR_V3.md
output_contract: investment-firm-output/SKILL.md
output_contract_version: 14
publication_policy: news-radar-investing/references/radar-publication-policy.json
camillo_discovery_contract: news-radar-investing/references/camillo-discovery.md
camillo_source_register: news-radar-investing/references/camillo-source-register.json
camillo_market_source_pack: news-radar-investing/references/camillo-market-source-pack.json
camillo_source_monitoring_contract: news-radar-investing/references/camillo-source-monitoring.md
google_trends_connection: news-radar-investing/references/google-trends-connection.md
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
routine_radar_title: Investment Firm — Radar
routine_radar_sections: New news and opportunities; Changes to existing investment cases; Stock monitor — Buy / Hold / Wait / Sell
protected_discovery: bounded urgent risk -> Core broad pass plus Camillo observation pass -> routine continuation
news_universe: not limited to holdings, tickers, known brands, AI or investing personalities
novelty_memory: source/observation identity AND connection identity; canonical plus verified dated fallback
price_monitor_source_classes: CANONICAL; LEGACY; PORTFOLIO DEFENSE
price_monitor_proximity_band: 5_percent for eligible non-ER monitor rows only
price_monitor_rows: strategy_case + exact_security + applicable_lot; no ticker-only collapse
stock_table_schema: combined_action_queue_v2_with_event_reaction_mechanics
report_format_version: 9
presentation_filter: omit ER inventory; use separate verified trigger alert cards
strategy_annotations: compatible presentation/manifest metadata only; no new backend enums implied
routine_radar_publication: one integrated report per slot, including unchanged eligible non-ER monitor rows
standing_view: existing Decision List; preserve unresolved actions, manual notes and original cutoffs
markdown_artifact_required: false
```

## Authority

Read current SKILL.md and required references from one consistent revision where practical. Output version 14 and MONITOR_V3 own consolidated publication, integrated synthesis, sole standing-view ownership and ER alert-only presentation. They supersede older separate-brief/publisher and mandatory ER-table instructions in inherited source/strategy/baseline prose. Historical BASELINE_WORKFLOW.md files remain preserved; unrelated source, analytical, clinical, execution and security safeguards still apply.

Do not declare that a reporting-version change introduces backend schema support. The retained stock_table_schema value is a compatibility identifier only; the current display excludes routine ER rows. Preserve older reports' actual schema/cutoff and retain detailed audit data privately. Use only accepted write fields; do not relabel historical snapshots as version 9.

## Single run and persistence

One routine task covers all three local-time slots, including weekends. The separate Midday Checks and Daily Brief publishers are retired after their responsibilities transfer; do not recreate or re-enable them during routine runs. Internal Disclosure/Portfolio Defense producers keep their schedules and feed the next unified Radar. Urgent risk channels and the mechanical system remain unchanged.

Maintain one per-slot report identity plus existing stock-monitor:YYYY-MM-DD:HHMM:America_Toronto linkage. Reconcile same-slot work and source versions before fetching/publishing again. Append to the existing private Journal, then refresh the Decision List with fresh revision protection/read-back and only the newest verified completed snapshot. Preserve unresolved decisions, user notes, trigger history and original cutoffs. A late/duplicate completion cannot overwrite newer state. Do not create a second brief:YYYY-MM-DD report for the same run.

At 15:00 include concise daily decision synthesis and next evidence inside the same report; Friday includes existing AI-efficiency breadth and calibration. Nonurgent late findings move to the next slot. Scheduled start is not guaranteed delivery; 15:00 is not market close. Saved, delivered and executed are separate states.

## Event Reaction reporting only

No recurring ER table, hold rows, near-target reminders, target inventories or no-trigger placeholders. Check actual engine/verified mechanical events; surface a new applicable stop, partial target, runner target or time exit as a compact deduplicated alert. Do not route mechanical exits to underwriting or mutate the current manifest, thresholds, broker alerts, lots or fills. Keep ordinary data gaps internal; preserve exceptional urgent operational-risk alerts. Quiet display is not proof of checked safety. Same-issuer Core/Camillo holdings remain separate and exposure is counted once.

## Preserved discovery and safeguards

Both protected discovery passes, all eleven specialist checks, Tier-A newsletter intake, source receipts/normalization, bounded Google worker, pre-pivotal clinical controls, disclosure provenance and AI-efficiency fixed-cohort/backfill/cost/quality checks remain. Camillo can surface one traceable early signal without a ticker, earnings proof, price trigger or Core discount. Source uncertainty is explicit. No fabricated fresh observations from unchanged datasets.

Keep actual source-health receipts, evidence histories and portfolio context in existing supported private state/fallback, not public GitHub. Source registration, tests, job submission or changed task configuration do not prove live collection, source truth or delivery. No accepted-thesis, probability, fair-value, holding, risk-budget, threshold, review-date, proposal, fill, migration or application-deployment changes are authorized by this reporting cleanup.
