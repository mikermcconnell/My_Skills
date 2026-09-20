# Active News Radar Version

```text
active_version: 3
status: ACTIVE
activated_at: 2026-08-27
scan_cadence: 08:00, 11:30, 15:00 America/Toronto
skill: news-radar-investing/SKILL.md
monitor_contract: news-radar-investing/MONITOR_V3.md
run_contract: news-radar-investing/references/v3-run-contract.md
specialized_lanes_contract: news-radar-investing/references/specialized-lanes.md
price_monitor_contract: news-radar-investing/references/price-monitor-live-source.md
sell_discipline_contract: news-radar-investing/references/sell-discipline-and-closeout.md
nancy_pelosi_tracker_contract: news-radar-investing/references/nancy-pelosi-tracker-lane.md
price_monitor_mode: dynamic_live_source
price_monitor_audit_format: action_sorted_queue
price_monitor_rows: one_per_security
price_monitor_proximity_band: 5_percent
ai_efficiency_watch_contract: news-radar-investing/references/ai-efficiency-watch.md
ai_efficiency_watch_state_contract: news-radar-investing/references/ai-efficiency-watch-state.md
ai_efficiency_watch_activated_at: 2026-09-18
ai_efficiency_watch_weekly_summary: Friday 15:00 America/Toronto, inside the Daily Brief
ai_efficiency_watch_first_weekly_summary: 2026-09-25 15:00 America/Toronto
mandatory_specialized_lane_checks: 11
output_contract: investment-firm-output/SKILL.md
output_contract_version: 1
output_contract_approved_at: 2026-09-20
routine_publication: one Daily Brief, Monday-Friday 15:00 America/Toronto
other_publication: urgent Action Alert only, plus material unsaved-finding fail-safe
standing_view: Investment Firm — Decision List
markdown_artifact_required: false
```

## Read order and presentation precedence

Every scheduled Radar task loads the latest skill, this pointer, `MONITOR_V3.md`, the run contract, specialized lanes, dynamic price-monitor source, sell discipline, disclosure tracker, AI-efficiency lane and its state adapter. It also loads `investment-firm-output/SKILL.md` before deciding whether or how to publish.

**The Investment Firm output contract is the sole authority for scheduled presentation and notification criteria.** It replaces older requirements to print every lane, every unchanged monitor, internal routing tables, and a separate complete Radar report at each scan. Those requirements now describe the internal audit record, not mandatory chat output. All eleven checks, full manifests, research quality, source rules, novelty controls, and analytical stage boundaries remain in force. Explicit requests for a full research report remain full reports.

The established scan cadence is not the publication schedule. Routine findings are recorded for the one designated weekday Daily Brief. Other scans publish only a genuinely urgent Action Alert, or the contract's material unsaved-finding fail-safe. The Daily Brief retains findings since the previous confirmed delivered brief, late arrivals, and unresolved decisions; a successful scan or saved report is not a delivery receipt.

## Specialized lanes

`references/specialized-lanes.md` controls mandatory membership and count. Its current **11-lane** definition supersedes older nine-/ten-lane wording. Check all lanes every run; preserve UPDATE, NO UPDATE, UNAVAILABLE and partial-coverage qualifications in the manifest. NO UPDATE is valid only after an actual check. The user's brief displays material findings, not a mandatory lane-status dump.

## Dynamic price monitoring

Query canonical live price-monitor/underwriting-monitor state each run. Dynamically enumerate active monitors, thresholds/actions, consumed triggers and re-arm state, then fetch current prices. Never use a static Radar ticker list or a prior report as the source of truth. Additions, removals and edited boundaries must flow from that canonical state.

Preserve the complete action-sorted audit queue, one row per security: `Action | Stock | Current price | Next trigger | What to do`. Controlled audit actions remain RE-UNDERWRITE NOW, EXIT REVIEW NOW, TRIM REVIEW NOW, COMPELLING BUY/ADD REVIEW, BUY/ADD REVIEW NOW, GETTING CLOSE, NO ACTION and UNAVAILABLE. Ownership determines BUY versus ADD. A trigger starts the existing underwriting/allocation review; it is not an automatic trade. The brief shows newly relevant decisions/triggers rather than every unchanged row. `references/price-monitor-live-source.md` owns the underlying trigger logic; the Investment Firm contract owns its scheduled presentation.

## Disclosure and AI-efficiency safeguards

The official House Clerk PTR remains the disclosed-transaction source. Preserve transaction versus filing dates, owner codes, reported amount ranges, and options details only when disclosed. Never equate a disclosure with exact current holdings, personal actual returns, informational advantage or a BUY/SELL instruction. Detailed verified updates remain in research; material changes feed the shared brief.

Preserve AI-efficiency adoption/target/operating/financial/repeated evidence stages, quality and total-cost checks, the fixed comparison cohort and two-earnings-cycle baseline backfill. Do not change the Investor rubric. `references/ai-efficiency-watch-state.md` still controls the Library fallback at `/News Radar/AI Efficiency Watch`, snapshot reconciliation, and activation-aware weekly timing. Initial baseline completion must not be assumed. First weekly summary remains September 25, 2026, 15:00 Toronto. Prepare its evidence within normal runs; only the Daily Brief publisher delivers the routine weekly summary.

## Persistence and authority boundaries

Canonical research stores and supported dated fallbacks retain the complete research record. The private reporting journal transports/indexes findings for the brief; the standing Decision List is a reporting view, never a second financial baseline. Verify writes/read-back and distinguish saved, delivery unconfirmed, and confirmed implementation. Do not store private portfolio details or private document bindings in this public repository.

Radar detects and routes. Downstream workflows may create only proposed TRIM/EXIT actions; the user/broker executes, Investor Holdings records the confirmed sale, and supported MikeInvestor reconciliation requires the owned closed-position record. This output migration does not authorize changes to theses, probabilities, valuation, sizing, thresholds, review dates, holdings, or application deployment. Preserve existing application alert delivery until replacement integration is verified.
