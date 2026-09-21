# Active News Radar Version

```text
active_version: 3
status: ACTIVE
activated_at: 2026-08-27
scan_cadence: 08:00, 11:00, 15:00 America/Toronto, daily
scan_cadence_updated_at: 2026-09-21
skill: news-radar-investing/SKILL.md
monitor_contract: news-radar-investing/MONITOR_V3.md
run_contract: news-radar-investing/references/v3-run-contract.md
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
output_contract_version: 3
output_contract_approved_at: 2026-09-21
stock_table_publication: with each existing 08:00, 11:00 and 15:00 Radar run, daily, even when unchanged
narrative_publication: one Daily Brief, Monday-Friday 15:00 America/Toronto, without a duplicate complete stock table
other_publication: exceptional urgent Action Alert only, plus material unsaved-finding fail-safe
standing_view: Investment Firm — Decision List, maintained by the Daily Brief with original snapshot cutoffs
markdown_artifact_required: false
```

## Read order and presentation precedence

Every scheduled Radar task loads the latest skill, this pointer, `MONITOR_V3.md`, the run contract, specialized lanes, dynamic price-monitor source, sell discipline, disclosure tracker, AI-efficiency lane and its state adapter. It also loads `investment-firm-output/SKILL.md` before deciding how to publish.

**The latest Investment Firm output contract owns scheduled presentation and notification criteria.** Its version 3 amendment moves the required simple stock table from Daily-Brief-only publication to the existing 08:00, 11:00 and 15:00 Radar runs. The midday slot replaces 11:30; it is not another run. This pointer and the actual updated schedules supersede older 11:30 references in run/monitor files. Preserve the full scan window and recover gaps rather than inventing retroactive completed runs.

Each of these three scheduled runs returns the stock table and a brief change/coverage summary, even on quiet days. This explicitly supersedes older internal-only or urgent-only wording for the scheduled stock outputs. It does not reinstate complete lane-status dumps or separate reports from every research stage. All eleven checks, full manifests, research quality, source rules, novelty controls and analytical boundaries remain in force. Explicit requests for full research remain full reports.

The broader weekday Daily Brief remains at 15:00 but does not reprint the full stock table. It summarizes consequential decisions/research and references the latest completed stock snapshot with its original cutoff. A simultaneous 15:00 stock scan might not yet be complete; never pretend its results or delivery exist. Portfolio and Disclosure tasks retain internal/urgent-only publication. No new tasks are created by this amendment.

## Specialized lanes

`references/specialized-lanes.md` controls membership and count. Its current **11-lane** definition supersedes older nine-/ten-lane wording. Check all lanes each run; preserve UPDATE, NO UPDATE, UNAVAILABLE and partial coverage in the manifest. NO UPDATE requires an actual check. Visible stock updates and the brief do not require a full lane-status dump.

## Dynamic price monitoring

Query canonical live price-monitor/underwriting state each run. Dynamically enumerate active monitors, thresholds/actions, consumed triggers and re-arm state, then retrieve current prices. Never use a static Radar ticker list or prior report as today's source. Additions, removals and edited boundaries flow from canonical state. Missing application records do not erase independently readable accepted baselines: the output contract permits a separately labelled reference screen without treating it as active or armed monitoring.

Retain the complete action-sorted internal audit queue. Controlled internal actions remain RE-UNDERWRITE NOW, EXIT REVIEW NOW, TRIM REVIEW NOW, COMPELLING BUY/ADD REVIEW, BUY/ADD REVIEW NOW, GETTING CLOSE, NO ACTION and UNAVAILABLE. A price crossing starts the existing review, not an automatic trade.

The user-facing stock table is `Stock / position | Latest price | Buy / add level | Trim / sell-review level | What to do | Why / next step`. Include unchanged HOLD/WAIT names and preserve exact instrument/currency distinctions. BUY/ADD/TRIM/SELL requires a current completed supporting review under the output contract; a raw price trigger is REVIEW, not a renewed trade instruction. Preserve readable fields and disclose unknown state. A fair-value estimate is not a sell threshold. `references/price-monitor-live-source.md` owns underlying trigger/quote controls; the latest Investment Firm output contract overrides its older publication-frequency wording.

## Disclosure and AI-efficiency safeguards

The official House Clerk PTR remains the disclosed-transaction source. Preserve transaction versus filing dates, owner codes, reported ranges and disclosed options detail. Never equate a disclosure with exact current ownership, personal actual returns, informational advantage or a BUY/SELL instruction. Detailed verified research and material narrative updates feed the shared brief.

Preserve AI-efficiency adoption/target/operating/financial/repeated evidence stages, quality and total-cost checks, fixed cohort and two-earnings-cycle baseline backfill. Do not change the Investor rubric. `references/ai-efficiency-watch-state.md` still controls the Library fallback at `/News Radar/AI Efficiency Watch`, snapshot reconciliation and activation-aware timing. Initial baseline completion is not assumed. First weekly summary remains September 25, 2026 at 15:00 Toronto; prepare evidence within normal scans and deliver that weekly narrative only in the Daily Brief.

## Persistence and authority boundaries

Canonical research stores and supported dated fallbacks retain full research. The private reporting journal transports/indexes findings and per-slot stock snapshots; the Decision List is a reporting view, not a financial baseline. Radar appends snapshots; the Daily Brief remains the scheduled writer of the standing view and must preserve original snapshot cutoffs, newer manual snapshots and unresolved cases. Verify writes/read-back, distinguish prepared from delivered and implemented, and do not put private portfolio details or document bindings in this public repository.

Use per-slot stock issue IDs and the independent weekday brief window from the output contract. A periodic table does not consume a trigger, and an unchanged row is not a new alert. Scheduled starts do not guarantee completed research or delivery at that minute. Disabled notification flags remain a delivery limitation; prompt/schedule edits alone cannot enable them.

Radar detects and routes. Downstream workflows may create only proposed TRIM/EXIT actions; the user/broker executes, Investor Holdings records the confirmed sale, and supported reconciliation requires the owned closed-position record. This output amendment does not change theses, probabilities, valuation, sizing, thresholds, review dates, holdings or application deployment authority. Preserve existing application risk-alert delivery until replacement integration is verified.
