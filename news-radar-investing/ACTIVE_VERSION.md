# Active News Radar Version

```text
active_version: 3
status: ACTIVE
activated_at: 2026-08-27
analytical_revision: 2026-09-22-pre-pivotal-speculative-pathway
scan_cadence: 08:00, 11:00, 15:00 America/Toronto, daily
skill: news-radar-investing/SKILL.md
monitor_contract: news-radar-investing/MONITOR_V3.md
run_contract: news-radar-investing/references/v3-run-contract.md
source_routing_contract: news-radar-investing/references/source-and-routing-rules.md
source_feed_contract: news-radar-investing/references/primary-source-feed-map.md
emerging_signal_contract: news-radar-investing/references/emerging-signal-lens.md
specialized_lanes_contract: news-radar-investing/references/specialized-lanes.md
price_monitor_contract: news-radar-investing/references/price-monitor-live-source.md
sell_discipline_contract: news-radar-investing/references/sell-discipline-and-closeout.md
event_reaction_mechanics_contract: news-radar-investing/references/event-reaction-strategy-mechanics.md
nancy_pelosi_tracker_contract: news-radar-investing/references/nancy-pelosi-tracker-lane.md
price_monitor_mode: combined_canonical_persisted_legacy_portfolio_defense
price_monitor_audit_format: action_sorted_queue_with_source
price_monitor_rows: generic_queue_one_per_exact_security_not_one_per_source; event_reaction_one_per_exact_security_strategy_lot
price_monitor_visible_columns: Action | Stock | Current price | Next trigger | Source | What to do
event_reaction_visible_columns: Action | Stock / lot | Entry | Current | Stop loss | Target sells | Time exit | What to do
price_monitor_source_classes: CANONICAL; LEGACY; PORTFOLIO DEFENSE
price_monitor_proximity_band: 5_percent
ai_efficiency_watch_contract: news-radar-investing/references/ai-efficiency-watch.md
ai_efficiency_watch_state_contract: news-radar-investing/references/ai-efficiency-watch-state.md
ai_efficiency_watch_activated_at: 2026-09-18
ai_efficiency_watch_weekly_summary: Friday 15:00 America/Toronto, inside the Daily Brief
ai_efficiency_watch_first_weekly_summary: 2026-09-25 15:00 America/Toronto
mandatory_specialized_lane_checks: 11
output_contract: investment-firm-output/SKILL.md
output_contract_version: 9
output_contract_approved_at: 2026-09-21
stock_table_schema: combined_action_queue_v2_with_event_reaction_mechanics
routine_radar_title: Investment Firm — Radar
routine_radar_sections: New news and opportunities; Changes to existing investment cases; Stock monitor — Buy / Hold / Wait / Sell
routine_radar_publication: one combined report with each existing 08:00, 11:00 and 15:00 run
protected_broad_discovery: after bounded urgent-risk triage, before routine deep reconciliation or stock-table assembly
news_universe: not limited to current holdings, watchlists, accepted underwritings or active themes
stock_table_publication: inside each combined Radar report, including unchanged eligible monitor rows
novelty_memory: accessible canonical Event Ledger plus verified dated fallback / Reporting Journal
narrative_publication: one weekday 15:00 Daily Brief for synthesis, not duplicate full news/stock reports
other_publication: exceptional urgent Action Alerts and material unsaved-finding fail-safe
standing_view: existing Investment Firm — Decision List, maintained by Daily Brief with original cutoffs
markdown_artifact_required: false
```

## Single baseline and read order

Every scheduled Radar task reads this pointer, the current skill, monitor/run/source/feed/specialized/price/sell contracts, disclosure/AI-efficiency references and latest shared output skill. The feed map is a required run input, not merely an audit reference. Where practical read from a consistent current commit and record it. Analytical Radar version remains 3; output contract version is 9.

The core skill, run/monitor instructions, source/feed rules, specialized lanes and price lane are reconciled in place. Do not restore obsolete stock-only, always-visible lane-dump or Daily-Brief-only news behavior. All eleven checks, gates, source rules, specialized evidence and execution boundaries remain required. The combined-monitor patch changes the table's source union and schema, not the news-first sequence or cadence.

## Discover and publish news, not just existing stock status

Do a bounded initial urgent-risk screen, then the protected open-universe discovery pass before routine old-case expansion, thesis deep work or full quote-table assembly. Search current cross-market issuer news, filings/operating/financing, official decisions and industry/customer/supply-demand changes without restricting queries to known tickers. Document actual queries/feeds, windows, markets and gaps. P0 may preempt; record incomplete discovery and recover. Do not imply public-news access requires a working private portfolio connector.

Publish supported material findings in the current combined report, even before RWC/underwriting makes a trade decision. Show NEW DEVELOPMENT, NEW EVIDENCE — EXISTING STORY, LATE DETECTION or NOVELTY UNVERIFIED with original dates and exact next questions. Outside-known-universe status is separate and verified or unknown. Unfamiliar ticker count is not a goal; no story quota or lowered gates.

Keep the new-news section first unless urgent risk leads, changed cases second and the combined stock action queue third. Include unchanged eligible monitor rows with plain wait/review next steps but do not retell unchanged old cases as news. Market context and discovery coverage are compact. One combined output per existing slot, not a separate news report plus separate table.

## Combined monitor sources and action boundaries

The table is the union of **CANONICAL + explicitly persisted LEGACY + PORTFOLIO DEFENSE**. Canonical controls its live membership/thresholds/consumed/re-arm state and supersedes equivalent legacy conditions. Legacy eligibility requires actual structured recovery records from supported live research/event storage, such as LEGACY_PRICE_MONITOR, LEGACY_MONITOR_ACTIVE and economicBridge.legacyMonitor. Stage RWC on such a record is preservation metadata, not fresh completed RWC/underwriting. Generic prose, memory, old visible tables and dated upload ticker lists do not establish active legacy membership.

Live concrete defense stop/target/time/concentration/instrument/thesis/valuation review conditions may supply or supersede the selected action, without creating thresholds or final sells. De-duplicate one row per exact security, preserving listing/currency/option contract and applicable lot/strategy. Combined Source labels CANONICAL + DEFENSE or LEGACY + DEFENSE require material contribution to the selected row. A distinct legacy threshold is eligible only when canonical explicitly lacks that non-overlapping condition and the record remains migration-pending. Disabled equivalent canonical conditions cannot be revived through legacy.

Use `Action | Stock | Current price | Next trigger | Source | What to do`. Visible actions remain review-only under the price contract's urgency order. Every legacy-contributing instruction begins `Refresh/migrate underwriting first;`; a relevant legacy REUNDERWRITE_REQUIRED record selects RE-UNDERWRITE NOW ahead of its separate price hit. Preserve source IDs/dates, migration status, consumed/re-arm history and defense trigger types. Read all three classes before saying NO ACTIVE STOCK MONITORS; all must be readable and contain no eligible row. Material missing-class coverage is PARTIAL, not zero. Keep missing-level/unstructured/disabled/migration blockers visible in coverage and retained case detail without inventing active rows.

Exact quotes and stored conditions remain separate; missing fields are shown narrowly. Same quote confirmation/5% proximity controls apply across all classes. Fair value is not automatically a sell threshold; stocks, CDRs, options, currencies and strategies remain distinct. This is review routing, not automatic migration, allocation, approval or trading.

## Emerging Signal / leading-indicator baseline

The protected discovery pass now includes a cross-sector Emerging Signal lens. It is not a new lane or task.

Radar looks for acceleration/deterioration patterns that may lead reported fundamentals, stores/reuses Signal Sequences for trajectory-shaped evidence, and escalates with existing P3/P2/P1/P0 routes. It does not require reported revenue/profit before surfacing a credible testable upstream signal, but it also does not convert attention or one datapoint into an investment conclusion.

Pattern archetypes include adoption acceleration, demand inflection, pricing power/weakness, capacity/bottleneck shifts, operating leverage/deleverage, distribution advantage/failure, competitive displacement, behavior-to-financial conversion, narrative/evidence divergence and promise-to-measurement.

No numeric score, idea quota, twelfth lane or additional automation is introduced.

## Pre-pivotal clinical pathway

The Clinical / Medical lane now supports a pre-readout pathway:

`PRE-PIVOTAL WATCH -> EVIDENCE BUILDING -> RWC NOW -> POSITIONING REVIEW -> probability-weighted Full Underwriting -> loss-budgeted speculative starter when justified`.

Phase 3 success is not required before RWC or Full Underwriting when the probability distribution, pivotal translatability, financing and failure case can be modeled honestly. A speculative starter remains deliberately small, evidence-staged and constrained by the pivotal-failure portfolio loss budget. No universal position percentage is embedded in Radar.

Portfolio Capital Allocation may still choose zero. Additional size requires named evidence and a refreshed risk/valuation check.

## Event Reaction mechanical sleeve

Event Reaction / post_earnings positions are strategy-mechanics exceptions. Read current Investor `config/strategy-manifest.json` and the Event Reaction mechanics contract. Ordinary stop/partial-target/runner-target/time-exit decisions for that exact strategy lot do not enter fundamental underwriting.

Render Event Reaction positions in a separate mechanics subtable before the generic combined monitor queue. Current September 21 baseline: 10% stop; +12.5% sell 85%; +15% runner on remaining 15%; 30 trading-session maximum hold. Entry fill/date and prior partial-sale state must be authoritative. Missing data produces ER DATA NEEDED/ER MECHANICS REVIEW, not RE-UNDERWRITE NOW.

Same-ticker non-Event-Reaction expressions remain independently eligible for normal underwriting/defense monitoring.

## Memory, source state and compatible reporting

Read verified fallback seen-history as well as canonical event records. A fallback-only saved discovery is already seen even when a canonical write failed; preserve its first-detected date and persistence gap. Do not count it as new again. This does not promote fallback prose to an accepted thesis, active monitor, completed research or delivered notification. Missing history means novelty unverified.

Use the existing per-slot `stock-monitor:YYYY-MM-DD:HHMM:America_Toronto` issue identity for compatible readers, now with report_format_version 7, stock_table_schema combined_action_queue_v2_with_event_reaction_mechanics and both news and stock content. A title/schema change does not justify a duplicate issue. Older snapshots remain dated with their actual schema and must not acquire invented source labels. Preserve canonical evidence IDs, original cutoffs, prepared/delivered distinction and the Daily Brief's independent window. Saved/last-run/notification flags are not actual delivery receipts.

Radar appends research and snapshots to the existing private journal; Daily Brief remains the scheduled writer of the existing standing view. Preserve newer manual snapshots and unresolved cases. The simultaneous afternoon report must not be assumed completed. The brief provides synthesis/progress and Friday aggregation without reproducing the full Radar output; it is not the sole place new news appears.

## Specialist and rollout safeguards

Keep official House PTR owner/trade/filing/range/option-return rules, dynamic current expert roles and the AI fixed cohort/backfill/state adapter, costs/quality/confounders and first-week boundary. New specialist evidence may appear intraday; the full weekly AI breadth summary stays in Friday's brief. No new rubric, monitor or task.

Extend the existing first-five-brief comparison with actual discovery-pass completion, outside-known-universe coverage, unique-origin new/evidence/late counts, fallback-aware duplication, same-run inclusion of material news, unchanged-case suppression, all three monitor sources, legacy-prefix/migration priority, canonical suppression/defense precedence, all-three-empty/partial handling and exact-security de-duplication. Metrics are diagnostics, not quotas or claims of superior returns. Keep unsupported enrichment in the run manifest/fallback rather than strict production payloads.

No change to investment theses, probabilities, fair values, sizing, thresholds, review dates, holdings, proposals, fills, optional-workflow flags, application deployment or broker authority is authorized by this reporting/search patch. No legacy migration, monitor activation or runtime inventory creation is performed by editing these skills. Preserve existing application risk-alert channels until verified replacement. Configuration saved/read-back and actual corrected scan/persistence/delivery are separate evidence; notification-channel limitations remain explicit.
