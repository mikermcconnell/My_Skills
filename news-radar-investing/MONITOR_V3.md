# News Radar Investing V3 — Scheduled Monitor Instructions

ACTIVE analytical version 3. News-discovery correction and combined-monitor patch approved September 21, 2026. Use `news-radar-investing/SKILL.md`, `references/v3-run-contract.md` and the shared `investment-firm-output/SKILL.md` version 6 or later. Do not layer another output contract over them.

## Schedule and outputs

Keep existing **08:00, 11:00 and 15:00 America/Toronto daily** runs, including weekends, on their existing tasks. Each returns one **Investment Firm — Radar** report containing:

1. **New news and opportunities** — supported material developments, including outside our existing stock list; distinguish new events, new evidence on existing stories, older late detections and uncertain novelty.
2. **Changes to existing investment cases** — meaningful new evidence/status/decision/deadline changes only; not recycled old case summaries.
3. **Stock monitor — Buy / Hold / Wait / Sell** — Event Reaction strategy mechanics first, then one action-sorted combined CANONICAL + persisted LEGACY + PORTFOLIO DEFENSE queue for non-Event-Reaction expressions.

Urgent portfolio risk may lead. Material news must not be suppressed until a BUY/SELL decision exists or deferred exclusively to the Daily Brief. The stock table remains required but does not define the news universe. Compact market context and source-coverage notes belong within this same output. Do not produce a second separate stock notification from the run.

The existing weekday 15:00 Daily Brief synthesizes decisions/research, maintains the existing Decision List and incorporates Friday breadth evidence. It does not reprint the whole Radar news report or stock table. Other specialist/portfolio producers retain internal/urgent-only publication; no new task or newsletter.

## Run sequence

1. Read the current skill, active pointer, run contract, source/routing rules, primary-source feed map, shared output contract and specialist/price/sell/disclosure/AI-efficiency references. All eleven checks remain required; record unchanged lane statuses in the audit, not a mandatory visible dump.
2. Recover the actual window since the last verified completed cutoff, including delayed/advanced/partial/failed gaps. Keep intended slot, actual start/cutoff and receipt separate. Do not advance unsearched broad-source windows merely because a portfolio check succeeded.
3. Make a bounded live-context/seen-history preflight and rapid urgent-risk screen. Read actual holdings, imminent evidence/instrument deadlines and potential P0 risks where available. Missing private state is a limitation, not a reason to abandon public news. Repeated routine connector retries and historic inventory cleanup do not belong before all discovery.
4. **Complete the protected open-universe pass next**, before routine deep case reconciliation, thesis expansion, all-name quote assembly or downstream underwriting. Use actual unseeded broad searches across the four source families in `primary-source-feed-map.md`; record queries/feeds, windows, markets, outcome and limitations. Known-ticker searches alone do not count. No required number of leads or new tickers. A P0 emergency can preempt this, with explicit skipped-window recovery.
5. Complete remaining portfolio defense, source-led active-thesis tests, due evidence/catalysts and all eleven specialist lanes. Load current Mind Model pillars/forecasts/falsifiers and use the run contract's targeted priority; cheaply sweep each readable active thesis rather than deep-diving all of them. Missing live thesis state is not inferred from GitHub seeds or memory.
6. Read all three monitor source classes and enumerate their union under `price-monitor-live-source.md`: active CANONICAL monitors, explicitly persisted structured LEGACY recovery records and concrete live PORTFOLIO DEFENSE conditions. Retrieve exact-instrument quotes near the comparison cutoff. Preserve source IDs/dates, active/inactive status, thresholds, consumed/re-arm and migration state. Canonical supersedes equivalent legacy; higher-priority defense may supersede a buy review. De-duplicate one row per exact security and keep applicable lot/strategy. No generic prose baseline, old table or upload ticker list becomes a live legacy row. Missing-level/disabled/mapping-blocked research remains a coverage note and existing case detail, not an invented monitor. Available quotes survive missing trigger state; unknown ownership/cash is not guessed.
7. Build market context using futures/overnight data at 08:00 and actual regular-session data at 11:00/15:00 when open, otherwise labelled last-session prices. Distinguish observations from attribution; a price move is a search trigger, not proof of company news.
8. Reconcile material observations against original sources, prior public/accepted baselines, canonical Event Ledger AND verified dated fallback/Reporting Journal. Already-detected fallback-only news is not new again because an app save failed. Preserve event/publication/first-detection dates, stable IDs and independence groups. Uncertain history stays unverified; genuinely new evidence on an old theme can still qualify.
9. Apply all five gates, one primary route and one underwriting requirement. A plausible economic question can be surfaced before completed valuation; unknown versus failed gates remain distinct. Include enough security/counterparty mapping to route, strongest failure reason, exact next test/date and up to three stored RWC questions. Do not force new beneficiaries or conflate familiarity with novelty.
10. Enforce the hard depth boundary. Causality/confounders/counterfactuals/capture go to RWC; valuation/capital structure/scenarios/returns/timing to Full Underwriting; discrete payoff/execution to Event-Trade Underwriting; weights/funding to allocation. P0 warnings can precede complete assessment. A route does not start a worker by itself.
11. Retain existing sell discipline: Radar detects/routes, downstream proposes, user/broker executes, and owned Investor Holdings closedPositionId precedes supported reconciliation. Partial close retains residual exposure; full close retains postmortem requirements. No fabricated fills, approved trades or changed thresholds through this correction.
12. Retain disclosed owner/trade/filing/range/option-return safeguards, dynamic expert-role resolution and AI-efficiency fixed cohort, backfill cursor, quality/cost/confounder controls. New specialist evidence may appear in this Radar report. The full weekly AI breadth summary stays in Friday's Daily Brief; first eligible boundary remains September 25, 2026.
13. Save research-only records using supported canonical writes with fresh state/idempotency. After a bounded fresh-state retry, use verified authorized fallback instead of spending the run repairing persistence. Never bypass concurrency or put unsupported diagnostic fields in a strict API payload. Keep original lineage and saving limitations.
14. Append the combined report, compatible stock snapshot and full coverage/discovery/source-class manifest to the existing private Reporting Journal with revision protection and read-back. Radar does not overwrite the Decision List; its existing daily publisher copies the latest completed snapshot with its original cutoff and preserves newer manual snapshots/unresolved cases. Never write private portfolio data or document IDs into public GitHub.
15. Publish the combined report even on quiet or partial runs, with no forced news. Show supported material discoveries promptly, unchanged case details only where needed, and the combined stock queue every time. If saving failed, disclose within this same output. Use exceptional Action Alerts outside scheduled reports only when waiting materially matters; do not duplicate an unchanged outage or consumed trigger.

## Event Reaction monitor exception

For current positions explicitly tagged to Investor strategy_id `event_reaction` / alias `post_earnings`, read the current Investor strategy manifest and `references/event-reaction-strategy-mechanics.md`.

Do not send those lots to RWC/Full Underwriting/Event-Trade Underwriting/Portfolio Capital Allocation for ordinary strategy stop/target/time mechanics. Display their confirmed entry, current price, calculated stop, +12.5%/85% partial target, +15% runner target, 30-trading-session time exit and mechanical action. Current rule numbers are examples of the September 21 manifest; the manifest remains authoritative.

A material issuer headline can still appear as news. It does not replace the Event Reaction mechanics. If the same ticker is held under another strategy, keep that other expression in the normal combined queue.

## Combined stock table and readiness

| Action | Stock | Current price | Next trigger | Source | What to do |
|---|---|---:|---|---|---|

Use the price contract's ordered review actions: RE-UNDERWRITE NOW; EXIT REVIEW NOW; TRIM REVIEW NOW; COMPELLING BUY/ADD REVIEW; BUY/ADD REVIEW NOW; GETTING CLOSE; NO ACTION; UNAVAILABLE. These are review/monitor states, not final trades. Source labels are CANONICAL, LEGACY, PORTFOLIO DEFENSE, CANONICAL + DEFENSE or LEGACY + DEFENSE when materially contributing. Every legacy-contributing instruction begins `Refresh/migrate underwriting first;`; relevant legacy REUNDERWRITE_REQUIRED selects RE-UNDERWRITE NOW. A recovery record stored at stage RWC is not fresh RWC completion.

Check LEGACY and DEFENSE even when canonical arrays are empty. NO ACTIVE STOCK MONITORS requires all three sources readable with no visible row. Missing material source coverage is PARTIAL; preserve reliable rows. Retain disabled/migration blockers in coverage without reactivation. A fair-value estimate is not a sell trigger; one option-exit review is not an issuer-wide sale; missing fields are not a reassuring HOLD or all-clear. Completed reviewed portfolio advice stays separate in the decision narrative. No automatic trading or migration.

## Diagnostics

Extend the existing run manifest with actual protected-discovery source coverage, unique new developments, new evidence on old stories, late detections, outside-known-universe candidates or unknown membership, unchanged follow-ups, fallback-aware duplicate groups and material discovery IDs included in output. These are diagnostics, not quotas, false hit rates or delivery receipts. A private-state outage may coexist with a successful public news scan; an unsearched source cannot be called no update.

For each stock row retain source class, legacy event/result/date and migration/consumed/re-arm fields where applicable, defense trigger type/position scope and canonical-over-legacy suppression reason. Keep exact-security IDs and per-source coverage. Do not hard-code the dated runtime inventory in an uploaded patch.

Maintain original per-slot snapshot IDs for compatibility, with report_format_version 5 and stock_table_schema combined_action_queue_v1. Do not emit another issue for the same slot solely because its title/schema changed. Saved, prepared, delivered and implemented are independent states; never infer delivery from task success or notification settings.

Use the existing first-five-completed-brief validation to inspect coverage, novelty labels, outside-universe searching, same-run news inclusion, unchanged-case suppression, combined-source stock retention/precedence/legacy prefix/defense priority, fallback dedup, actual cutoffs, failed saves and notification delivery. No new validation newsletter. Saved configuration is not proof that the next corrected scan or its notification has succeeded.
