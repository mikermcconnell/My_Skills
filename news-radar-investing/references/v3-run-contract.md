# News Radar Investing V3 Run Contract

Reconciled September 21, 2026, including the combined-monitor patch. Radar is the high-recall detection, memory, risk-priority, thesis-testing, market-context and routing layer. `investment-firm-output/SKILL.md` owns the combined visible report; `source-and-routing-rules.md` owns gate/provenance detail; `primary-source-feed-map.md` owns broad-source coverage; `emerging-signal-lens.md` owns cross-sector leading-indicator pattern recognition and trajectory memory; `specialized-lanes.md` owns eleven-lane membership; `price-monitor-live-source.md` owns combined monitor sources, precedence, review actions and quote/trigger controls. Do not maintain another competing presentation template here.

## Cadence and independent windows

Existing scheduled runs: **08:00, 11:00 and 15:00 America/Toronto, daily**. Morning covers overnight/international and premarket evidence; midday covers fresh North American/international intraday evidence; afternoon covers pre-close developments and time-sensitive decisions. All three include broad discovery, targeted checks and the stock table. Explicit after-close capture is additional only when requested; it does not replace a scheduled run.

Record intended slot, actual start/cutoff and scan status separately. Recover advanced, delayed, skipped, partial and failed windows from the last verified completed cutoff. A task last-run timestamp is not necessarily an evidence cutoff. If cutoff cannot be recovered, state it and use a labelled overlapping recovery window; do not assert gap-free coverage. Track source-family gaps so a completed narrow holdings check cannot advance a missing broad-discovery window.

Detection, successful persistence, actual research progress and delivered-report state are separate. The Daily Brief has an independent since-last-confirmed-delivered window. A periodic stock row or prepared Radar report neither consumes a trigger nor proves user delivery.

## Required execution order

1. **Bounded preflight and urgent-risk triage.** Load/attempt minimum live ownership/identity, last cutoff, urgent cases/deadlines and seen-event memory. Identify possible material permanent-loss or imminent instrument risk. P0 can interrupt every later step and must be surfaced promptly. Routine history cleanup is not an emergency.
2. **Protected broad discovery.** Before routine deep case reconciliation, full quote-table assembly or thesis expansion, complete the feed-map's unseeded cross-market/source-family search and apply the Emerging Signal / Leading Indicator lens. Searching only existing tickers, named counterparties, old event IDs or the active thesis list does not satisfy this step. Preserve public-news scanning even when private connectors fail.
3. **Targeted continuation.** Finish portfolio defense, exact-instrument sell checks, cheap active-thesis sweeps, evidence-due/catalysts, all eleven specialist lanes and the combined canonical/legacy/defense monitor check. Deep targeted work follows risk/evidence priority without retroactively erasing missing broad coverage.
4. **Classify and route.** Compare original sources and prior evidence, deduplicate against canonical AND verified fallback memory, apply five gates, map sufficient public-security exposure, assign one route and underwriting requirement, and stop at the depth boundary.
5. **Record and publish.** Save supported research-only state and manifests, with bounded retry/fallback. Return one combined news/case-change/stock-table report under the output contract, even when parts are unavailable. Verify saves separately from delivery.

A normal successful run needs each mandatory coverage step completed or accurately qualified. P0 emergencies or external feed outages may preempt discovery; record PARTIAL/NOT_RUN, exact skipped families/windows and reason, then recover at the next scheduled pass. No forced story or unfamiliar-ticker quota. Do not certify a broad scan just because all portfolio lanes were visited.

## Protected discovery acceptance

Use `primary-source-feed-map.md` each scheduled run. Record an explicit short plan with current windows and four source-family passes: broad issuer/market news not constrained to known tickers; filing/exchange/operating/financing changes; official regulatory/court/policy/clinical decisions; and industry/customer/supply-demand/technology shifts. Use relevant U.S., Canadian and international sources as accessible and disclose scope rather than claiming global completeness. These are process requirements, not a required count of interesting results.

For every family retain actual query/feed, retrieval time, market/category, oldest/newest evidence assessed where determinable, original-source follow-through, and COMPLETE/PARTIAL/UNAVAILABLE/NOT_RUN status. A failed source attempt is not a completed sweep; try an appropriate differentiated source within the bounded budget and preserve remaining limitations. Routine connector troubleshooting, archived baseline migration and unchanged-case expansion must not take this entire pass.

On a credible new lead use prior public guidance/disclosure for comparison even when no accepted underwriting exists. Novelty/capture may remain unknown; name a resolving test and route appropriately. Do not require owning the company, an existing monitor, completed RWC or a BUY recommendation to surface supported news. Do not manufacture a beneficiary or claim of mispricing.

## Preflight inventory and coverage

Load relevant state when supported and mark unavailable fields, not false empty inventories:

```text
last_successful_run_at and verified evidence cutoff
open_event_ledger_records and independence groups
verified dated fallback / Reporting Journal seen-event records
open_P0_P1_P2_items and next_evidence_due_queue
open_emerging_signal_sequences_and_due_confirmation_checks
known_catalyst_calendar and frozen packets
active_holdings, exact lots/options and issuer mappings
active_underwritings_and_monitors
active_price_monitors_and_stored_actions
Event_Reaction_strategy_tagged_positions_and_current_manifest_exit_rules
persisted_legacy_price_monitors_and_migration_status
portfolio_defense_price_time_stop_concentration_instrument_triggers
current_kill_criteria_and_review_dates
live_Mind_Model_overview and active_nonretired_theses
Mind_Model_review_queue, thesis_diagnostics and open_thesis_forecasts
thesis_evidence_ledger, watchlist exposures and linked investor research
pending_thesis_proposals and open_trim_exit_proposals
position_closeouts_and_residual_exposure
broker_confirmed_sales_awaiting_closeout_reconciliation
full_closeouts_awaiting_postmortem
same_day_market_context and available_source_feeds_and_outages
```

Load quotes during their actual comparison step so earlier cached marks are not falsely labelled current. Do not finish every historical reconciliation before starting discovery. GitHub source/seeds describe schema, not confirmed production thesis/holdings state. Missing cash is not zero cash; holdings-only exposure is not cash-inclusive NAV. Respect current authentication/schema/version checks.

## Event Reaction strategy-mechanics routing

When live strategy/position state explicitly tags a lot to Investor strategy_id `event_reaction` or a current alias such as `post_earnings`, read `references/event-reaction-strategy-mechanics.md` and the current Investor `config/strategy-manifest.json`.

Event Reaction's ordinary per-position stop/target/time-exit mechanics are outside the fundamental underwriting path. Do not assign YES/CONDITIONAL underwriting solely because an Event Reaction lot approaches or hits its strategy stop, partial target, runner target, or 30-session time exit. Use internal `Underwriting Required? = NO` with strategy-mechanics rationale and render the separate Event Reaction mechanics table under the output contract.

Current September 21 baseline from the manifest: 10% stop; +12.5% partial target selling 85%; +15% runner target on the remaining 15%; 30 trading-session maximum hold. Calculate from confirmed entry fill/date and authoritative remaining quantity/partial-sale state. If those are missing, mark ER DATA NEEDED / ER MECHANICS REVIEW. Do not infer from old reports.

The same issuer's separate non-Event-Reaction position remains eligible for normal RWC/underwriting/Portfolio Defense. Issuer news may still surface in Radar without changing the Event Reaction lot's mechanical action.

## Emerging Signal / trajectory requirement

Read `references/emerging-signal-lens.md` on every scheduled run.

During protected broad discovery and Social / Alternative Data coverage, test credible observations for generalizable leading-indicator patterns rather than only discrete headline events. Look for magnitude, velocity, persistence, breadth, independent confirmation, a plausible business bridge, expectations lag and a decisive next test.

When an observation may develop over time, create or reuse a stable Signal Sequence / parent hypothesis in supported storage. Preserve atomic evidence IDs and first-seen dates; update the trajectory instead of resetting the case every run. If strict production schemas do not support sequence fields, retain them in the run manifest or verified fallback rather than inventing unsupported payloads.

At the start of targeted continuation, also check **due Signal Sequences**. Fast-moving signals may be due at the next scheduled run or within roughly 1–2 days; medium-speed operating/channel signals generally several days to a week; slower KPI/financial conversion aligns to the named reporting/catalyst date. These are defaults, not mandatory timers.

Use current P3/P2/P1/P0 routes. “Not yet revenue” is not a reason to discard a credible upstream signal with a plausible financial bridge. Escalate to P1 RWC when cumulative evidence materially strengthens acceleration/deterioration, persistence/breadth, independence, business transmission or the expectations question. RWC then tests causality, representativeness, capture, confounders and consensus.

This is not a new lane, score, quota or strategy.

## Underwriting monitoring handoffs

During preflight / targeted continuation, read unresolved `UNDERWRITING_MONITOR_HANDOFF` records from supported canonical research stores or the verified Reporting Journal.

These records exist to preserve **named evidence and review dates from working underwriting that was not promoted to an accepted baseline**.

For each unresolved handoff:

- check whether the named evidence/date is due or has newly arrived;
- preserve the original underwriting date, readiness/challenge state and source;
- route genuinely new evidence through normal Radar/RWC gates;
- keep unchanged future items in evidence-due state without presenting them as fresh news every run;
- if the review backstop arrives with unresolved evidence, route a refresh and retain the original date rather than rolling it forward;
- if a later canonical baseline supersedes the handoff, stop using the handoff as active research guidance and retain it only as history.

**Do not convert analytical price sensitivities in a non-canonical handoff into the live Stock Monitor queue.** Only accepted/activated canonical, structured eligible legacy, portfolio-defense, or separate authorized strategy mechanics may create active stock-monitor actions under their own contracts.

Unresolved handoffs should still be visible to the Daily Brief / Decision List as `Waiting for evidence`, `Research needed`, or `Monitoring` so their next evidence does not disappear.

## Active Thesis Research

After urgent triage and the protected discovery pass, cheaply sweep all readable non-retired theses; do not do a mini deep-dive on each three times daily. Test stored baseline, assumptions, hypothesis, strongest opposing case, falsifiers and next-highest-value test. For pillars retain claim/mechanism/metric/baseline/target/date/source/falsifier; for forecasts retain statements/resolution dates/metrics and confirm/warning/break indicators; for watchlist exposures retain mechanism/evidence needs/falsifiers/position status and linked security/underwriting readiness.

Within targeted search, deeper priority remains owned requiresReunderwrite; EVENT_TRIGGERED; owned OVERDUE; other OVERDUE; DUE; BLOCKED/CONFLICTED; timely tests of otherwise normal theses. Diagnostics such as STALE, CONCENTRATED, CONFLICTED, MISSING_CHALLENGE, MISSING_FORECAST and MISSING_PILLARS guide testing, not automatic thesis changes.

For each material delta save supported thesis_id, pillar_id, forecast_id, what_was_tested, new_evidence, SUPPORT/CHALLENGE/CONTEXT, what_it_proves/does_not_prove, delta_class, thesis_effect, detection_status, five_gates, primary_route, underwriting_requirement and next_test/evidence. Retain unsupported enrichment in the manifest rather than invalid API payloads. Radar may save research-only evidence or a pending proposal, never approve it or change approved thesis/forecast state.

## All eleven specialist lanes

Complete the lane definitions in `specialized-lanes.md`:

1. **Price Monitor Check** — one action-sorted table merging readable CANONICAL monitors, persisted LEGACY Investment Firm monitors, and active PORTFOLIO DEFENSE triggers under `price-monitor-live-source.md`.
2. Slow-Burn Fundamentals.
3. Catalysts / Evidence Due.
4. Social Arbitrage / Alternative Data.
5. Clinical / Medical.
6. Expert / Industry Sources.
7. TTWO.
8. AMZN.
9. HOOD.
10. Pelosi disclosures.
11. AI Efficiency Watch.

They supplement, not replace, broad discovery. Record UPDATE, NO UPDATE, UNAVAILABLE and partial qualifiers; NO UPDATE requires actual checking. Narrative findings surface in the combined report when material. Unchanged per-lane status lists remain in the audit, not mandatory chat. The combined stock queue remains visible even unchanged. Keep disclosed trade/filing/owner/amount-range distinctions, current expert-role lookup, clinical source caution and the AI fixed-cohort/backfill/state-adapter requirements. Friday's full AI breadth summary belongs in the existing Daily Brief; first eligible boundary remains September 25, 2026.

## Combined prices, defense queue and market context

| Action | Stock | Current price | Next trigger | Source | What to do |
|---|---|---:|---|---|---|

- `price-monitor-live-source.md` controls source precedence and supersedes older wording in this file.
- The table universe is CANONICAL + persisted LEGACY + PORTFOLIO DEFENSE.
- A legacy row is not a canonical trigger and must route through underwriting refresh/migration before capital allocation.
- A portfolio-defense row is a review trigger only; it is not a final sell/trim decision.

Read all three sources independently each run, including linked structured legacy event/results, original dates and migration state. Stage RWC plus LEGACY_MONITOR_ACTIVE/economicBridge.legacyMonitor denotes monitor preservation, not newly completed research. Do not populate from a fixed list, prior table, memory, generic prose baseline or dated upload inventory.

De-duplicate one row per exact security, preserving contract/listing identity and applicable lot/strategy. Canonical overrides equivalent legacy; a distinct legacy threshold is allowed only when canonical explicitly lacks it and it is clearly migration-pending. Higher-urgency defense may override a buy review. Use CANONICAL, LEGACY, PORTFOLIO DEFENSE, CANONICAL + DEFENSE or LEGACY + DEFENSE only according to material contribution. Every legacy-contributing What to do begins `Refresh/migrate underwriting first;`. Decision-relevant legacy REUNDERWRITE_REQUIRED selects RE-UNDERWRITE NOW before its separate price hit.

Preserve active/inactive status, source versions, all thresholds/actions and each source's consumed/re-arm conditions. No re-fire without satisfied explicit re-arm. A canonical disabled condition cannot be revived through equivalent legacy state. A distinct live defense condition remains eligible. Record missing-level/unstructured/disabled/mapping-blocked cases as coverage gaps and retained case details, not invented source-labelled active rows.

Canonical-empty must continue to LEGACY and DEFENSE. Show NO ACTIVE STOCK MONITORS only if all three are readable with no eligible row. Preserve readable classes, mark PARTIAL when unavailable state could materially change membership/action, and state specific gaps. Unknown is not zero. Price and source state are independent; retain readable fields if another fails. Non-price reviews require concrete current rule/evidence and can remain valid without a quote they do not depend on.

Use the same quote hierarchy and stricter confirmation within 5% of or through a valid threshold across all source classes. Follow review-action urgency RE-UNDERWRITE NOW, EXIT REVIEW NOW, TRIM REVIEW NOW, COMPELLING BUY/ADD REVIEW, BUY/ADD REVIEW NOW, GETTING CLOSE, NO ACTION, UNAVAILABLE. A source/price hit is not a finished trade recommendation. Fair value/dividend-inclusive total value is not automatically a sell boundary. USD shares, CAD CDRs and option-premium conditions are not interchangeable. Unknown cash or denominator cannot establish a concentration breach.

At 08:00 use overnight/futures and reliable premarket quotes or labelled previous close; at 11:00/15:00 use actual same-day regular-session prices when open. Check S&P 500, Nasdaq/large-cap growth and TSX when useful; rates, oil, FX, volatility, credit or commodities only when materially relevant. Keep observed movement separate from inferred/reported drivers. Unclear attribution stays unclear. No price reaction is invented on closed markets. Compact market context normally stays within 80–100 words and never replaces discovery.

A large price move may initiate PRICE_DISLOCATION_UNEXPLAINED investigation: inspect primary sources, peers/counterparties, factors, flows, options/short-interest and false attribution. A move or monitor crossing is not itself a fundamental Novelty pass.

## Novelty, fallback memory and evidence due

Every material observation retains schema-supported delta_class, thesis_effect and detection_status. Existing detection statuses include ON_TIME, LATE_DETECTION, FOLLOW_UP, DUPLICATE, EXPECTED_EVIDENCE_MISSED, DISCLOSURE_REMOVED, MILESTONE_DELAYED, PROMISE_UNCONFIRMED and PRICE_DISLOCATION_UNEXPLAINED. Do not add unsupported enums to production writes.

Before assigning first detection, search both canonical Event Ledger and verified dated fallback/Reporting Journal for the underlying event, source-origin group and evidence delta. A failed app save with a successful fallback is already-seen evidence for reporting, not new again next run. Preserve first detection, fallback key and canonical-save limitation without promoting it to a registered monitor or accepted investment conclusion. A genuinely different new fact can still advance the same case.

Classify older first-public information first detected now as LATE_DETECTION only when no earlier detection is found in accessible durable memory. Record public date, event date, first detection, latency, likely missed-feed/process reason and decision usefulness. If seen-history is missing, novelty is unverified, not a made-up ON_TIME/first discovery. An older transaction disclosed publicly now is newly available evidence, not automatically late. A new article repeating an old source is not new evidence.

Check next-evidence dates, pillar/forecast target dates, catalyst windows and missing promised disclosures. Record absent readouts/filings/financing/permits/launches, changed registry dates/endpoints/enrollment, removed KPIs/tables and unsupported promises past their evidence date. Absence is not automatically negative; unchanged absence is not a new observation every run. Do not rewrite frozen expectations or historical observations once outcomes are known.

## Gates, priority and minimum mapping

Use the five gates and routes in `source-and-routing-rules.md`. Radar needs a plausible materiality/capture/expectations question and research path, not complete proof. Unknown is not failure, and a P2 observation is not a P1 or trade-ready idea. Keep a no-lead run valid.

Portfolio-defense priority governs urgency within targeted work, not permission to put broad discovery last behind all routine administration. Time-critical permanent-loss risk goes first. Then prioritize genuinely changed material evidence/deadlines, owned re-underwrite requirements, catalyst results, open-event deltas, thesis/evidence needs and slow-burn changes. An unchanged case gets no artificial novelty priority.

Map direct holding/security, linked thesis/pillar/forecast/underwriting, DIRECT/DERIVATIVE/READ_THROUGH/NONE_IDENTIFIED, preliminary mechanism, capture uncertainty, cluster and readiness where supported. New candidates need not already be held or underwritten. For P1 opportunities and class/policy/bottleneck/cross-company events assess an appropriate second-order candidate and comparator/non-beneficiary if feasible; unknown stays unknown. Do not delay P0 for a full map or claim independent observations from syndicated sources.

Every surfaced event/thesis delta receives one internal underwriting requirement: NO; CONDITIONAL — AFTER RWC; YES — RE-UNDERWRITE EXISTING; YES — NEW FULL UNDERWRITING; or YES — EVENT-TRADE UNDERWRITING. Preserve rationale and the actual live readiness/review inputs. Translate these into plain next steps in chat. Transmission-map membership alone does not make a security decision-ready.

## Hard depth and execution boundary

Stop normal Radar work after exact delta/baseline, original source/claim status/independence, timestamps/market context, plausible mechanism/materiality, affected exposures, gates, strongest failure reason, primary route, underwriting requirement and up to three decisive RWC questions plus next evidence/date. Visible output normally uses one primary question, at most two independent ones. Do not ask RWC to prove the initial hypothesis; ask whether it survives verification.

Full causality/counterfactuals/confounders/capture belong to RWC; reverse valuation, dilution/scenarios/returns, timing and security posture to Full Underwriting; discrete event payoff/microstructure to Event-Trade Underwriting; loss budgets/weights/funding/hedges to allocation. Exceptions remain urgent P0, comparing a frozen packet, one time-sensitive classification document or explicit combined-workflow authorization. Routine downstream reviews do not take the protected discovery slot.

Radar records controlled sell-review reasons and routes them under `sell-discipline-and-closeout.md`; it does not finalize sells. Only an authorized downstream PROPOSED TRIM/EXIT is permitted. User/broker executes, and an owned Investor Holdings closedPositionId is required for supported reconciliation. Partial closure retains residual exposure; full closeout retains postmortem requirements. Missing tool/record means CLOSEOUT_PERSISTENCE_UNAVAILABLE/AWAITING_HOLDINGS_RECORD, not closure. A proposal is not a fill. A legacy refresh/migrate instruction is not migration authorization.

## Research-only records and concurrency

Persist supported Event Ledger additions/updates, original/first-seen dates, duplicate/rejected observations, atomic slow-burn evidence, thesis tests/evidence, explicit research questions, pending thesis proposals, underwriting routes/rationale, P2 due evidence, frozen packets, market/specialist/combined-monitor coverage, sell lineage, late detections/outages and the complete manifest.

Use fresh authorized state and exact retry/idempotency semantics. After one appropriate fresh-state bounded retry still fails, use verified authorized fallback and continue the search; do not bypass optimistic concurrency. A saved fallback is not successful app persistence, worker execution or delivery. If no save path works, disclose PERSISTENCE_FAILED in the same requested output and preserve material findings there. Internal-only producers use the shared reporting-gap fail-safe when justified.

Do not approve/change Mind Model theses or forecasts, fair values, entry/exit levels, monitor actions, kill/review dates, positions or strategy through Radar persistence. This patch does not create/migrate legacy records or enable disabled monitors. Reporting diagnostics stay in supported manifests/fallback, not new production schema fields. Public repositories must not contain private portfolio information, document bindings or credentials.

## Run manifest and discovery diagnostics

Retain existing fields plus diagnostic enrichment in supported storage:

```text
run_id; radar_version=3; report_format_version=7; stock_table_schema=combined_action_queue_v2_with_event_reaction_mechanics
scheduled_slot; actual_start; scan_window_start; scan_window_end
run_status SUCCESS|PARTIAL|FAILED|ADVANCED|DELAYED
last_successful_run_at and evidence cutoff provenance
markets_and_event_categories_covered
holdings_checked; active_underwritings_checked; price_monitors_checked
price_monitor_quotes_as_of; price_monitor_state_unavailable
monitor_source_class_coverage: CANONICAL, LEGACY, PORTFOLIO DEFENSE
visible_source_class_per_row; exact_security_deduplication_key
legacy_monitor_event_result_ids; legacy_original_source_date
legacy_migration_status; legacy_consumed_rearm_state
portfolio_defense_trigger_type; applicable_position_lot_strategy
canonical_over_legacy_suppression_reason; contributing_record_ids
disabled_or_migration_blocked_monitor_gaps
active_theses_loaded; theses_researched; review_queue/forecasts_due_checked
thesis_state_unavailable; known_catalysts_checked; evidence_due_checked
market_tape_checked/as_of/sources
specialized_lanes_checked and per-lane status
primary_feeds_searched_successfully
expert_social_and_alternative_lanes_checked
feeds_unavailable_delayed_or_not_connected
state_sources_unavailable; material_blind_spots
underwriting_requirements_assigned
sell_reviews_checked; closeout_reconciliation_status
canonical_persistence_status; fallback_persistence_status
next_scheduled_slot; skipped_windows_to_recover
broad_discovery_status COMPLETE|PARTIAL|UNAVAILABLE|NOT_RUN
broad_discovery_queries_or_feeds with source family, scope, windows, retrieval time
broad_discovery_completed_families; skipped_families_and_reason
new_development_event_ids; new_evidence_existing_story_ids
emerging_signal_sequence_ids; emerging_signal_trajectory_updates; emerging_signal_escalations
late_detection_event_ids; novelty_unverified_ids
outside_known_universe_candidate_ids; universe_comparison_status
unchanged_followup_ids; duplicate_origin_groups
material_discovery_ids_included_in_output; omitted_material_ids_and_reason
first_detected_at; original_publication_at; underlying_event_at
report_prepared_id; included_record_ids; delivery_status_and_actual_receipt
```

Counts derive from deduplicated IDs, not articles, ticker wrappers, failed write retries or number of mapped beneficiaries. Freshness categories and outside-universe membership are separate overlapping dimensions; do not sum them as total discoveries. If comparison history is unavailable, use unknown, not zero. Included-in-output is not delivered. Metrics are diagnostic only: no minimum story count, target outside-universe hit rate or fabricated success metric.

## Visible completion and regression checks

Under the shared output contract, return one combined Radar report: **New news and opportunities; Changes to existing investment cases; Stock monitor — Buy / Hold / Wait / Sell**. Urgent risk can lead. New facts are shown promptly with uncertainty, not held until trade-ready or the afternoon brief. Cases without a meaningful change are not repeated news; eligible combined-monitor rows remain visible. Market context and a short coverage line fit inside this report, not another newsletter.

Preserve legacy per-slot stock snapshot IDs for compatibility and the Daily Brief's separate delivery window. Read canonical plus fallback seen-history before exact retries. Scheduled tasks append journal snapshots; the existing Daily Brief alone owns scheduled Decision List refresh. Original quote/event cutoffs remain intact; an earlier report cannot be relabelled current. Older schema snapshots remain dated and do not acquire invented source-class labels through formatting alone.

Check these cases during the existing first-five-brief rollout comparison: an early leading indicator saved as a sequence and rechecked; a sequence that accelerates/persists is escalated without waiting for reported revenue; a noisy one-off is not escalated solely on attention; a negative leading indicator receives the same treatment; fresh unfamiliar issuer surfaced for research without inventing a target; fresh event in a familiar company labelled new; new evidence on old theme not repeated as a new thesis; fallback-only previously detected event not rediscovered; older public event labelled late; unknown history explicitly qualified; unchanged old risk absent from new-news section but retained where needed; genuine urgent risk preempts discovery with a recorded gap; private connector outage still permits public news; quiet completed scan has no forced leads; combined stock queue retains all eligible source classes and exact-security identity; canonical-empty plus legacy/defense remains visible; all-three-checked-empty alone produces NO ACTIVE STOCK MONITORS; partial material source coverage stays PARTIAL; equivalent legacy suppressed by canonical; higher-priority defense overrides a buy review; legacy instructions carry the prefix; REUNDERWRITE_REQUIRED priority survives; generic prose/RWC stage alone never creates an active legacy row; disabled canonical stays disabled; no price-only BUY/SELL; no currency/option confusion; no consumed-trigger re-fire; no duplicate scheduled report.

Static contract validation, actual corrected scan behavior, verified persistence and delivered notifications are separate tests. Never claim a future run has passed.
