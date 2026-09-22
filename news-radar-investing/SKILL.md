---
name: news-radar-investing
version: 3
revision: 2026-09-21-emerging-signal-lens
description: Run the high-recall public-equity news front end: protect urgent portfolio risks, search beyond existing holdings and themes, distinguish new developments from new evidence and late detections, test active theses, check all eleven specialized lanes and the combined canonical/legacy/portfolio-defense monitor queue, and route precise research questions. Publish new news, meaningful case changes and the stock table together. Do not use Radar to manufacture valuation, final buy/sell decisions, position sizing or trade execution.
---

# News Radar Investing V3

`Radar -> Research With Confidence -> Full Underwriting or Event-Trade Underwriting -> independent challenge when applicable -> Portfolio Capital Allocation -> Mind Model / monitoring`

Radar owns detection, normalization, novelty memory, risk priority, active-thesis tests, market context, price-monitor checks, preliminary exposure mapping and routing. It is neither a full portfolio-review worker nor a stock-table-only service. **A fixed monitored-stock list is not the boundary of the news search.**

## Authority and read order

Use the latest files from the same current repository revision where practical:

- `ACTIVE_VERSION.md`: active version, cadence and contract pointers.
- `MONITOR_V3.md`: scheduled-task responsibilities.
- `references/v3-run-contract.md`: run sequence, protected broad discovery, manifest, research boundary and quality tests.
- `../investment-firm-output/SKILL.md`: sole user-facing layout, news/stock publication and delivery coordination.
- `references/source-and-routing-rules.md`: source provenance, five gates, priority and freshness rules.
- `references/emerging-signal-lens.md`: global leading-indicator pattern recognition, Signal Sequences, trajectory escalation and confirmation cadence.
- `references/newsletter-intake.md`: registered specialist-newsletter issue detection, claim extraction, deduplication and routing.
- `references/primary-source-feed-map.md`: mandatory broad-search design and source coverage; read on every scheduled run, not just audits.
- `references/specialized-lanes.md`: all eleven required lane definitions. Coverage statuses belong in the persisted manifest; meaningful findings flow into the combined report.
- `references/price-monitor-live-source.md`: combined CANONICAL/LEGACY/PORTFOLIO DEFENSE membership, source precedence, exact-security de-duplication, review actions, quote hierarchy/confirmation, consumed/re-arm state and failure handling.
- `references/event-ledger-schema.md`: supported event fields, delta classes, thesis effects, observation types and deduplication.
- `references/integration-and-persistence.md`: supported TaskTracker, Mind Model, Investor and dated fallback paths.
- `references/sell-discipline-and-closeout.md`: every owned-position sell check and closeout handoff.
- `references/slow-burn-and-catalyst-lanes.md`, `references/social-arbitrage-lane.md`, `references/clinical-radar-overlay.md`, and `EXPERT_SOURCES.md`: relevant specialist depth.
- `references/nancy-pelosi-tracker-lane.md`, `references/ai-efficiency-watch.md`, and `references/ai-efficiency-watch-state.md`: disclosure and AI-efficiency specifics, fixed-cohort state and first-week timing.

There is one current scheduled presentation: **new news and opportunities; changes to existing investment cases; stock monitor**. Do not recreate old mandatory lane-status dumps, routing-wide tables, stock-only reports, or Daily-Brief-only news suppression. Analytical Radar version remains 3; output-contract versioning is separate.

## Operating principle — combined monitor visibility

- **Do not let migration hide the watchlist.** The Price Monitor Check merges canonical monitors, explicitly persisted legacy Investment Firm monitors, and active portfolio-defense triggers. Legacy rows must be visibly labeled and must refresh/migrate underwriting before capital-allocation action.

The uploaded patch's runtime inventory is dated context, not a hard-coded ticker list or proof of a fresh read. A legacy recovery result stored at stage RWC is not a fresh RWC conclusion. Do not create/migrate records, activate disabled monitors, or change investment thresholds as part of this presentation patch.

## Cadence

Existing runs start at **08:00, 11:00 and 15:00 America/Toronto, daily**, including weekends. No additional task. An explicitly requested after-close capture does not replace a scheduled pass. Recover the window since the last actually completed scan cutoff; preserve advanced, delayed, skipped, partial or failed gaps. Scheduled start, actual cutoff and delivery time are separate facts.

## Stage boundaries

- Radar finds and routes leads; it does not prove causality, approve theses, value companies or execute monitor actions.
- RWC independently verifies facts, counterfactuals, confounders, economic materiality, value capture and whether an expectations gap survives.
- Full Underwriting owns current price, dilution/capital structure, reverse valuation, scenarios, expected return, opportunity cost, timing, kill criteria and security posture.
- Event-Trade Underwriting owns discrete payoff, break-even odds, execution, liquidity, halt/gap, borrow, options and slippage.
- Portfolio Capital Allocation owns loss budgets, weights, funding, clusters and staged implementation.
- Mind Model owns approved theses/pillars/forecasts, evidence and proposal history. A pending proposal is not an approved change.

A supported new lead can be shown before full underwriting. **Newsworthy and BUY-ready are different states.** Never demand a complete value-capture or valuation model merely to surface a credible researchable development.

## Registered newsletter feeds

Read `references/newsletter-intake.md`. High-signal newsletters are expert-source inputs inside the existing Radar architecture, not another lane.

Tier-A sources are checked for new issue identity on every scheduled Radar run. For each material issue, separate observable facts/data from expert interpretation/forecast and from investment mapping; deduplicate all wrappers to one issue origin; route important load-bearing claims to RWC rather than underwriting the newsletter itself.

Do not create a long routine newsletter summary. Show only decision-relevant new claims inside `New news and opportunities`, with the source, uncertainty, mechanism and next verification.

## Global Emerging Signal / Leading Indicator lens

Radar must look for **things that rhyme**, not only named historical setups.

Apply `references/emerging-signal-lens.md` during protected broad discovery and the Social / Alternative Data lane. For credible observations ask whether there is an unusual change in magnitude, velocity, persistence, breadth or independent confirmation; whether a plausible business bridge exists; whether expectations may lag; and what next fact would confirm or falsify the hypothesis.

Use the pattern library across sectors: adoption acceleration, demand inflection, pricing power/weakness, capacity/bottleneck shifts, operating leverage/deleverage, distribution advantage/failure, competitive displacement, behavior-to-financial conversion, narrative/evidence divergence and promise-to-measurement.

When the edge depends on a developing trajectory, preserve a Signal Sequence / parent hypothesis and compare each new observation with the prior trajectory. Do not wait for reported revenue or profit before surfacing a credible upstream signal; route missing conversion/expectations proof to P2 or P1 RWC as appropriate. Do not create a numeric score, quota, new lane, or new automation.

## Event Reaction strategy override

For a live position explicitly tagged to Investor strategy_id `event_reaction` or a current manifest alias such as `post_earnings`, use `references/event-reaction-strategy-mechanics.md` before generic underwriting or Portfolio Defense routing.

Event Reaction is a frozen mechanical sleeve. Ordinary stop-loss, partial-profit, runner-target and maximum-hold decisions for that lot have `Underwriting Required? = NO` and are handled by strategy mechanics, not RWC / Full Underwriting / Event-Trade Underwriting / Portfolio Capital Allocation. The current authoritative rule values come from Investor `config/strategy-manifest.json`, not this skill or memory. As of September 21, 2026 the manifest uses a 10% stop, +12.5% partial target selling 85%, +15% runner target on the remaining 15%, and 30 trading sessions maximum hold.

News about the issuer can still surface and be researched. It does not change the Event Reaction lot's mechanical action unless the strategy contract itself says so. Preserve a separate non-Event-Reaction position in the same issuer under normal underwriting/defense rules.

## Run workflow

### 1. Bounded preflight and urgent defense

Read/attempt current investor context, last successful cutoff, existing event identity, verified reporting fallback and imminent risk/evidence deadlines. Discover the authorized live Investor connection at runtime; keep fresh returned state versions for supported writes, not reusable historical tokens. Resolve serious security contexts separately when needed.

Load the relevant holdings, accepted underwritings/monitors, exact options/lots, kill/review criteria, catalysts, open P0/P1/P2, proposals, closeouts, live Mind Model state and feed outages. For the monitor queue read **every active CANONICAL price-bearing monitor; every readable persisted LEGACY Investment Firm monitor awaiting migration; every concrete PORTFOLIO DEFENSE sell/re-underwrite trigger; each source's stored threshold/range/action/consumed state; and the freshest reliable quote available for each monitored security** at its comparison cutoff. Preserve linked event/result IDs, source dates and migration/defense fields. Their full reconciliation can continue after the protected discovery pass; do not block all public-news searching on missing private state or recreate the whole research estate every scan. Mark missing fields/coverage honestly and bound connection retries.

Perform a rapid explicit urgent-risk screen: financing/liquidity, dilution/covenants, auditor/internal controls/fraud, safety/legal/regulatory/clinical risk, operational/customer issues, threatened kill criteria, hard imminent instrument deadlines and serious common-factor risk. P0 can interrupt any step and must not wait for table construction or broad discovery. Routine unchanged concentration, old unresolved proposals and long-range review-calendar cleanup are not reasons to starve discovery.

### 2. Protected open-universe discovery

Complete the source-feed map's broad discovery pass **after urgent triage and before routine deep reconciliation, thesis expansion, all-stock quote assembly or downstream valuation**. Use actual current queries/feeds not restricted to existing tickers, themes, counterparties or saved cases. Cover cross-market issuer/filing/operating/financing developments; regulator/court/clinical/policy decisions; and industry demand/supply/technology/customer shifts. Include relevant U.S., Canadian and international coverage as accessible and record the exact boundaries; do not imply exhaustive global coverage.

Portfolio-specific searches complement, not replace, this pass. Inspect useful unfamiliar counterparties and beneficiaries, not automatically the familiar holding. Record queries/feeds, categories, windows, primary-source retrievals, rejected/duplicate leads and coverage gaps. The source-feed map specifies minimum process coverage, not a required number of discoveries. Do not manufacture new tickers, stories or positive/negative balance.

A P0 emergency or unavailable external sources can leave discovery partial, but record the skipped families/window and reason. Resume missing coverage at the next pass. Missing holdings/underwriting state limits portfolio attribution, not the ability to report supported public developments. A new issuer without a saved baseline can be investigated against its prior public guidance; unknown novelty remains explicit, not a false pass or automatic rejection.

### 3. Complete targeted thesis, case and specialist checks

After the protected pass, complete remaining portfolio defense, exact-instrument sell checks, due evidence/catalyst checks, active-thesis tests, all eleven specialist lanes and combined price/legacy/defense monitoring. Do not skip required coverage silently; label partial work rather than claiming completion.

For live Mind Model, cheaply sweep every readable non-retired thesis: baseline, assumptions, strongest opposing case, falsifiers, next-highest-value test; pillars' claim/mechanism/metric/baseline/target/date/source/falsifier; forecasts' statements, dates and confirm/warning/break indicators; watchlist mechanisms/evidence needs and linked readiness; diagnostics such as stale, concentrated, conflicted, missing challenge/forecast/pillars. GitHub schemas/seeds or remembered prose are not live state.

Within targeted thesis work, deeper priority stays: owned `requiresReunderwrite`; EVENT_TRIGGERED; owned OVERDUE; other OVERDUE; DUE; BLOCKED/CONFLICTED; then timely tests of other active theses. Do not perform three full thesis deep dives daily. Each delta retains thesis/pillar/forecast IDs where supported, test, evidence, SUPPORT/CHALLENGE/CONTEXT, what it proves/does not prove, gates, route, underwriting requirement and next test.

All eleven lanes remain required, and the Emerging Signal lens applies across them where relevant: prices; slow-burn fundamentals; catalysts/evidence due; social/alternative data; clinical/medical; expert/industry; TTWO; AMZN; HOOD; Pelosi household disclosures; AI Efficiency Watch. Record UPDATE, NO UPDATE, UNAVAILABLE or partial qualifications for each; NO UPDATE requires actual checking. Use current accepted baselines, not permanently hard-coded financial assumptions in a skill. New material findings appear in this run, not just the afternoon brief.

The Price Monitor Check produces one action-sorted table under `price-monitor-live-source.md`:

| Action | Stock | Current price | Next trigger | Source | What to do |
|---|---|---:|---|---|---|

Combine the three readable source classes, de-duplicate one row per exact security, let canonical supersede equivalent legacy and let higher-urgency defense override a buy review. Every legacy-contributing instruction begins `Refresh/migrate underwriting first;`; a decision-relevant legacy REUNDERWRITE_REQUIRED record selects RE-UNDERWRITE NOW. Use only explicitly persisted structured legacy state, not generic prose or old tables. All-three-readable-and-empty alone permits NO ACTIVE STOCK MONITORS; preserve readable rows when a class fails and qualify material coverage. Disabled/mapping-blocked records remain disabled, with their unresolved status recorded rather than an invented active signal. A defense row is a review, not a sale.

Freeze catalyst/forecast expectations before results when practical. Compare cumulative slow-burn evidence over comparable periods and preserve atomic observations. Check missing, delayed or removed expected evidence; absence is an observation, not automatic deterioration. An unusual price move or monitor crossing is a search/review trigger, not a fundamental Novelty pass.

### 4. Reconcile novelty using durable evidence, not just successful app writes

For every serious observation identify original source, publication and underlying event time; search the canonical Event Ledger, verified dated fallback/Reporting Journal and relevant prior public/accepted baseline. Use existing event/independence-group IDs where known. Several articles repeating one origin are one observation.

A finding previously saved only in fallback is already detected for reporting. Preserve its first-seen date and app-save limitation; do not call it new or late again merely because the app array is empty. A materially new observation on that story can still qualify. Fallback memory does not approve an investment baseline, activate a monitor or prove delivery/work completion.

Preserve supported `delta_class`, `thesis_effect` and `detection_status`. Output distinguishes NEW DEVELOPMENT, NEW EVIDENCE — EXISTING STORY, LATE DETECTION and NOVELTY UNVERIFIED. Outside-existing-universe status is separately verified, not inferred from an unfamiliar name. If history is unavailable, mark novelty uncertainty and route the missing comparison where worthwhile.

Backfill genuinely late first detections with original dates, latency, likely missed-feed cause and reduced usefulness if relevant. An older transaction newly disclosed now is not late merely because the transaction date is old. Recycled coverage and unchanged due items are not discoveries. Retain unresolved decisions without repeatedly presenting them as news.

### 5. Apply five gates and route

Assess separately: Novelty; Materiality; Capture; Expectation; Researchability. A plausible financial mechanism and a named resolving test suffice for research triage; RWC owns proof. Fail versus unknown are different. False/repeated/immaterial/no-exposure claims are rejected; a worthwhile credible lead with a resolvable unknown can be P2/P3 rather than falsely passed or rejected.

Assign one primary route:

- **P0 — HOLDINGS / THESIS RISK**: credible potential permanent-loss or thesis-breaking risk; investigate promptly, preserving unavailable exposure qualifications.
- **P1 — RESEARCH WITH CONFIDENCE NOW**: material, plausibly novel, economically traceable and potentially misunderstood or incomplete.
- **P2 — TARGETED EVIDENCE**: name the missing fact/document/denominator/counterparty/comparison and expected check date or explain unknown timing.
- **P3 — MONITOR**: real but insufficient current materiality, capture, expectations gap or researchability; state next evidence or why no further work is warranted.
- **REJECT / DUPLICATE**: false, stale without a delta, repeated/circular, immaterial, non-comparable or unsupported with no credible research path.

Map only enough exposure to route: direct holding/security, related thesis/pillar/forecast/underwriting, DIRECT/DERIVATIVE/READ_THROUGH/NONE_IDENTIFIED, preliminary mechanism, main capture uncertainty, cluster and readiness where supported. Aggregate issuer exposure only with verified mappings and preserve exact shares/CDRs/options/lots, currency, contracts, strike, expiry, direction and nonlinearity separately. Do not fabricate option delta or cash-inclusive NAV.

For P1 opportunity, industry/policy/bottleneck/class events or cross-company transmission, check a plausible second-order candidate and non-beneficiary/comparator where accessible. Mark unresolved, not invented; do not delay P0 for a complete beneficiary map.

### 6. Classify underwriting and hand off

Each surfaced material event/thesis delta retains exactly one internal `Underwriting Required?` classification:

- `NO`: evidence monitoring; no security work currently needed.
- `CONDITIONAL — AFTER RWC`: causal/materiality/capture/expectations questions remain; normal new-P1 state.
- `YES — RE-UNDERWRITE EXISTING`: current accepted security work may materially change and valuation/posture is the main remaining step; use actual re-underwrite triggers or live `requiresReunderwrite`.
- `YES — NEW FULL UNDERWRITING`: enough independent causal/capture evidence is established to move to security valuation, not merely an exciting headline.
- `YES — EVENT-TRADE UNDERWRITING`: adequate factual support for a discrete event whose unresolved questions are payoff/execution.

Explain YES/CONDITIONAL in one sentence. Translate into plain next steps in chat instead of an acronym chain. A route does not claim a running worker, approved recommendation, saved proposal or fill.

Stored P0/P1 handoffs preserve event/parent IDs, source/lane/cutoff and original dates, prior baseline, delta/thesis effect/detection status, thesis/pillar/forecast links, original hypothesis, preliminary mechanism, exposure/capture uncertainty, visible confounders, market state/reaction, frozen packet, strongest failure reason, sell-reason/gate if relevant, underwriting classification/rationale, up to three decisive RWC questions and next evidence/date. Ask RWC to challenge and verify, not prove Radar right. Normally show one primary question, at most two independent ones, in chat.

### 7. Enforce analytical and execution boundaries

Stop after exact delta, source/independence, timestamps, plausible mechanism, affected exposures, gates, strongest failure reason, route, underwriting requirement and next evidence. Defer full causality/counterfactuals/capture, variant perception, reverse valuation, dilution, scenarios/returns, clinical-commercial economics, event microstructure and allocation/hedging to their stages. Limited exceptions: urgent P0, comparing a frozen catalyst/forecast, retrieving one time-sensitive classification document or an explicit combined-workflow request. Do not let a price review consume broad-discovery coverage.

Apply controlled sell reasons and `sell-discipline-and-closeout.md` to every relevant owned News Radar/ChrisCamillo expression. Radar records review triggers, not final sells. Downstream may create only a PROPOSED TRIM/EXIT under its authorized workflow. User/broker executes; owned Investor Holdings `closedPositionId` is required for reconciliation. Partial closure retains residual exposure; full closure requires the supported postmortem. Missing tool/record means CLOSEOUT_PERSISTENCE_UNAVAILABLE or AWAITING_HOLDINGS_RECORD, not closure.

### 8. Save, publish and verify

Persist supported research-only events, evidence, observation history, catalyst/forecast packets, routes/underwriting requirements, specialist/combined-monitor coverage, sell-review lineage and full run manifest. Preserve each visible row's source class, linked legacy event/result/date/migration/consumed/re-arm state, defense type/position scope and canonical-over-legacy suppression reason. Respect ownership, schema, idempotency and fresh-state concurrency. After a bounded fresh-state retry fails, use verified authorized dated fallback and continue coverage; do not bypass version checks or spend the scan repeatedly repairing saves. Never place diagnostic fields into unsupported strict API payloads.

Publish **new news and opportunities + meaningful case changes + the complete combined stock action queue** in the same requested Radar report under `investment-firm-output/SKILL.md`. Critical warnings can lead; qualifying new news normally precedes recurring prices. Market context is compact and clearly attributed. Unchanged cases are not mini-reports; unchanged eligible monitor rows remain visible. A supported completed downstream recommendation can be relayed separately in decision context, never invented from a price hit, defense condition or legacy preservation record.

Read prior canonical and fallback records before classifying or saving; preserve original detection separately from saved/report-prepared/delivered status. Append the combined report and stock snapshot to the existing private journal, not public GitHub. Retain existing per-slot IDs, with report_format_version 5 and stock_table_schema combined_action_queue_v1; read prior schemas honestly rather than fabricating source labels for old rows. Avoid duplicate output on exact retries. A failed report save does not suppress important news; disclose it in the same output. Do not mutate the standing Decision List from Radar; its existing publisher owns scheduled refresh.

The weekday Daily Brief synthesizes, tracks research progress and updates the standing view; it must not be the only place fresh news is allowed to appear. Friday's AI-efficiency aggregation remains there, with the existing fixed cohort, backfill cursor and September 25 first eligible boundary. Material AI/disclosure news still appears in normal Radar as warranted with provenance and no automatic investment inference.

## Completion checks

Record actual completion or limitations for urgent defense, the protected unseeded discovery pass, all eleven lanes, targeted thesis/evidence/catalyst work, quotes/all three monitor source classes and supported persistence. Missing private state must not be called checked-empty or suppress public news.

Use the existing run manifest to record source families/queries/time windows, unique new developments, new evidence, late detections, outside-universe candidates/unknown membership, unchanged follow-ups, material discoveries included in output and blocked coverage. These are diagnostic counts, not quotas or fabricated performance statistics. Preserve separate overlapping dimensions and actual event IDs.

Check that fallback-only previously detected news is not recounted; genuinely new evidence is not incorrectly suppressed; first-publication and event dates are distinct; no unsearched universe receives an all-clear; monitor reviews are separate from completed decisions; canonical-empty does not hide valid legacy/defense records; canonical precedence and one-row-per-security de-duplication hold; LEGACY instructions have the required prefix and REUNDERWRITE_REQUIRED priority; consumed triggers do not re-fire; disabled records stay disabled; currencies/options/lots stay distinct; P0 was not delayed; routes do not invent work; and no financial baseline, thesis, threshold, holding or trade authority changed through Radar.

A quiet run is legitimate only within stated searched coverage. A scan that never completed broad discovery is PARTIAL, not evidence that no new opportunities exist. Configuration/read-back checks alone are not a successful corrected live scan or confirmed delivery.
