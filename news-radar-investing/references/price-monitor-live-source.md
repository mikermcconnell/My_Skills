# Price Monitor Live-Source Contract — News Radar V3

Reconciled September 21, 2026; combined-monitor patch applied the same day. This file owns the combined monitor universe, source precedence, exact-security de-duplication, visible review actions, quote verification and consumed/re-arm controls. The latest `investment-firm-output/SKILL.md` owns the surrounding news-first report and publication. The price lane supplements news discovery; it is not the boundary of Radar's news universe.

## Place within the scheduled run

At each existing **08:00, 11:00 and 15:00 America/Toronto** daily Radar run, publish this lane's combined action queue as the third section of the news/case-change/stock report. Keep all eleven specialist checks. Do not create another table notification, dashboard or task; do not defer ordinary new news exclusively to the Daily Brief.

Read/attempt urgent monitor/ownership context during bounded preflight. Complete routine all-name quote assembly and ordinary price-trigger review after the protected broad-discovery pass under `v3-run-contract.md`. Genuine urgent risk can preempt discovery with a recorded coverage gap. The field-resolution order below describes the price subroutine, not permission to replace the full run with price checking.

Visible table:

| Action | Stock | Current price | Next trigger | Source | What to do |
|---|---|---:|---|---|---|

This is one action-sorted review queue, including unchanged eligible monitors. The `Action` column uses the controlled review vocabulary below, not automatic BUY/SELL commands. `What to do` explains the practical next step. A separately supported completed downstream recommendation may be summarized in the case/decision narrative, but must not convert a legacy recovery record or defense review trigger into a finished investment verdict. No automatic trading.

## Dynamic source of truth

Query actual available canonical live monitor/underwriting state each run and enumerate currently active price-bearing records, including non-owned candidates. Preserve monitor ID/status, current thresholds/ranges, stored downstream actions, ownership linkage, kill/review state, consumed triggers and re-arm logic. Changes flow into the next run from that source; no skill edit should be needed per ticker.

Never use a fixed ticker/level list, old prompt, analyst target, previous Radar table or remembered underwriting as live membership. Do not retain removed/disabled monitors, miss newly active ones or cache superseded actions/trigger state. Unknown membership is not a checked-empty list. Empty canonical arrays do not end the combined-source check.

## Combined monitor universe

The visible Price Monitor Check is a **combined action queue** built from three distinct source classes:

1. **CANONICAL** — active price-bearing underwriting / monitor state from MikeInvestor. Canonical state remains authoritative for active/inactive membership, thresholds, consumed/re-arm state, ownership-linked action, and downstream workflow.
2. **LEGACY** — explicitly persisted Investment Firm monitor records that have not yet been migrated into canonical underwriting state. A legacy row is eligible only when a supported live research/event store exposes a structured monitor record, for example:
   - `route: LEGACY_PRICE_MONITOR`, and
   - a linked research result with `verdict: LEGACY_MONITOR_ACTIVE`, and
   - `economicBridge.legacyMonitor` containing the source date, ownership state when known, active thresholds, consumed thresholds when known, currency, and migration status.
   Legacy monitor records are **visibility/recovery state**, not canonical underwriting. They must never silently become canonical triggers.
3. **PORTFOLIO DEFENSE** — live owned-position sell/re-underwrite triggers from `sell-discipline-and-closeout.md`, including stored stop/target boundaries, time stops, concentration, instrument failure, thesis-break review, valuation review, and other active sell-discipline conditions that are sufficiently concrete to place in the action queue.

The canonical source remains authoritative whenever a canonical monitor exists for a security. Do not replace or override a readable canonical threshold with a legacy threshold for the same purpose.

Legacy monitor rows exist to prevent valid Investment Firm watchlist names from disappearing during migration. They are allowed only from explicitly persisted legacy monitor state. Do not reconstruct them from memory, a prior visible Radar table, analyst targets, or generic prose.

Portfolio Defense rows do not create or alter price-monitor thresholds. They expose an already-existing live sell/re-underwrite condition from owned-position state.

A result stored with `stage: RWC`, `verdict: LEGACY_MONITOR_ACTIVE` and `economicBridge.legacyMonitor` preserves monitor state only; it does not establish that fresh RWC, underwriting or allocation work was completed. Read linked event/result identities and structured fields through discovered supported tools. Do not invent unsupported query arguments or write schemas. A headline, upload ticker list or prose baseline alone is not the structured live legacy record.

### Source precedence and de-duplication

Build the visible security universe as the union of CANONICAL + LEGACY + PORTFOLIO DEFENSE, then collapse to one row per security.

For the same security:
- use CANONICAL instead of an equivalent LEGACY threshold whenever both exist;
- preserve a higher-urgency PORTFOLIO DEFENSE action when it outranks the price-monitor action;
- when two source classes materially contribute to the selected row, use a combined source label such as `CANONICAL + DEFENSE`;
- never show duplicate rows solely because the same security exists in more than one source class.

A legacy threshold that has a recorded consumed state must remain consumed. Do not re-fire it unless its persisted legacy record contains an explicit re-arm condition and that condition is satisfied.

A security is the exact tradable instrument, not automatically its parent issuer: different share classes, listings/currencies, CDRs and individual option contracts are not interchangeable. Merge duplicate source records for the same exact security; preserve the applicable lot/strategy in the selected trigger/instruction and all lower-priority conditions in the audit. Do not turn one contract's exit review into an issuer-wide sale or combine its premium with the underlying share price.

Explicit canonical retirement/disablement of a threshold must not be bypassed by an older equivalent legacy row. Distinct non-overlapping legacy conditions are eligible only under the explicit rule below. An independently valid live defense condition remains visible even if a separate canonical price monitor is disabled. Record disablement/migration blockers in coverage, not as newly armed price signals.

### Prose references and coverage gaps

The prior generic `REFERENCE SCREEN — monitor linkage unverified` is not a fourth source class or a substitute for eligible LEGACY records. Actual accepted Library baselines may still provide dated research context and resolving evidence, but cannot populate the combined queue without a qualifying source record. Preserve relevant missing-level holdings, unmigrated prose references and disabled/mapping-blocked baselines in a compact coverage note and existing Decision List details; do not silently erase the unresolved research or label it CANONICAL/LEGACY/DEFENSE without the required state. Do not create a second recurring stock table.

Runtime ticker inventories in an uploaded patch are dated reconciliation inputs, not a fixed future universe or proof of this run's reads. Discover current records each run; never activate a disabled migration-blocked monitor merely to fill the table. This reporting patch neither creates legacy records nor performs a migration.

## Independent data planes

Canonical monitor state owns its membership/status, levels/actions, ownership-linked conditions, trigger history and next valid workflow. Persisted LEGACY state owns its explicitly marked recovery fields only. Live defense state owns the applicable owned-position conditions. Market-price state independently owns price, exact instrument, currency, session, timestamp and provenance. Failure of one must not erase readable values from another.

Fresh price but missing relevant re-arm/trigger: show price, unavailable trigger/action and the exact gap. Readable trigger but unavailable quote: keep the stored level and mark the quote missing; do not activate a price-dependent comparison. Unknown ownership but otherwise valid trigger/quote: use BUY/ADD review without guessing ownership; final personalized allocation remains unverified. Never use UNAVAILABLE as a blanket replacement for a successfully retrieved quote. A supported non-price review can remain visible when it does not require the missing quote; identify its non-price basis.

## Price subroutine sequence

1. Read CANONICAL state, explicitly persisted structured LEGACY records and sufficiently concrete live PORTFOLIO DEFENSE conditions; record availability and scope of each.
2. Resolve exact security/ownership/lot/strategy, record IDs and source dates, current thresholds/actions, consumed/re-arm state, migration status, defense type and review/kill state.
3. Apply source precedence and suppression rules without dropping distinct higher-priority risks. Enumerate the union, not only canonical records.
4. Get the freshest reliable quote for each exact instrument at the actual comparison cutoff using the hierarchy below.
5. Confirm near/crossed or ambiguous observations under the stricter rule below; verify required non-price inputs for defense conditions.
6. Determine valid crossed/near/not-crossed state mechanically. Preserve consumption and explicit re-arm conditions. A relevant LEGACY REUNDERWRITE_REQUIRED record selects RE-UNDERWRITE NOW rather than its lower-priority crossed price condition.
7. Select one highest-priority valid action or closest next valid trigger per exact security; retain all underlying conditions and source/suppression reasons in the audit.
8. Apply visible source labels and LEGACY instruction prefix; keep monitor reviews separate from completed recommendations.
9. Record source/quote as-of times, confirmation, gaps and coverage; publish inside the combined report without modifying any investment or trigger state.

## Quote-source hierarchy

Use the best appropriate source actually accessible; a preferred provider failure alone is not a reason to declare all prices missing.

**Tier 1 — direct/consolidated/official market data.** Prefer a timestamped direct market-data tool, exchange feed or consolidated/official quote with unambiguous mapping. Examples include U.S. exchange-backed/consolidated feeds, TMX/TSX/TSXV for Canada and the relevant Euronext/local venue elsewhere. One verified Tier 1 observation may support ordinary not-near rows, and may meet the confirmation standard below when clearly current and exact.

**Tier 2 — high-quality aggregator.** For U.S. equities prefer StockAnalysis when direct tooling is unavailable and a same-day timestamped quote is exposed; preserve any stated real-time/delayed/feed provenance rather than assuming it. It is not a source of monitor membership. Use a suitable timestamped local-market provider for other listings.

**Tier 3 — reputable secondary source.** Investing.com, MarketScreener or a comparable provider can fill gaps when exact instrument/currency/session/time are clear. Check fragmented small-cap and international mappings especially carefully.

**Tier 4 — indirect snippets/news, last resort only.** A stale article or unverified search snippet may supply explicitly dated context, not activate current BUY/ADD, TRIM, EXIT, near-trigger or re-underwrite price actions. Preserve the original timestamp and indirect/stale status; do not call the observation executable or current.

## Near/crossed confirmation

Apply the same quote freshness and **5% GETTING CLOSE** rules across all three source classes. Require confirmation when a first quote is within 5% of the next valid trigger, appears through any valid entry/add/compelling/trim/exit/kill/review threshold, shows a classification-sensitive unusual move or has ambiguous symbol/share class/currency/venue/session.

Use **two current observations from differentiated sources**, or **one clearly timestamped direct/consolidated/official Tier 1 quote** with unambiguous mapping. Differentiated sources need not be independent economic data generators, but must help detect stale caches, wrong symbols, currencies or sessions. Record both sources/timestamps when used; do not portray different-time quotes as simultaneous.

If disagreement could change classification, do not average. Investigate exact instrument, session/time, corporate action/split, currency and delay. Keep a clearly superior quote visible if justified; unresolved disagreement leaves the price-dependent action UNAVAILABLE. Preserve reliable fields without issuing a guessed comparison. Non-price conditions require their own reliable current evidence, such as the correct cash-inclusive concentration denominator where the rule calls for it.

## Visible combined action queue

| Action | Stock | Current price | Next trigger | Source | What to do |
|---|---|---:|---|---|---|

### Source labels

Use exactly one of these visible source labels unless two materially contribute:
- `CANONICAL`
- `LEGACY`
- `PORTFOLIO DEFENSE`
- `CANONICAL + DEFENSE`
- `LEGACY + DEFENSE`

Legacy rows use the same user-facing action vocabulary so the queue stays easy to scan, but their `What to do` instruction must begin with:

`Refresh/migrate underwriting first;`

A crossed LEGACY buy/add/trim threshold therefore means:
`Refresh/migrate underwriting first; if the thesis/valuation and threshold remain valid, continue through the normal downstream review.`

It must **not** directly create a capital-allocation or trade instruction.

When `migrationStatus: REUNDERWRITE_REQUIRED`, the selected visible action is `RE-UNDERWRITE NOW` if the legacy record remains decision-relevant, even if a separate legacy price threshold is also crossed.

The prefix also applies to LEGACY + DEFENSE. A combined source label means both sources materially contribute to the selected row, not merely that another record exists. If the selected condition is a distinct permitted legacy threshold, use LEGACY rather than mislabelling it canonical. `Refresh/migrate` names the next gated workflow; it is not permission to migrate, approve or change records in a Radar pass.

### Controlled visible actions and sort order

1. **RE-UNDERWRITE NOW** — active material re-underwrite/kill review or decision-relevant LEGACY REUNDERWRITE_REQUIRED; run the required existing review before a portfolio decision.
2. **EXIT REVIEW NOW** — valid stored exit/kill/time-stop/instrument-failure workflow; refresh and decide downstream, never automatic exit.
3. **TRIM REVIEW NOW** — valid valuation/trim/concentration review; verify its actual evidence and denominator before a reduction recommendation.
4. **COMPELLING BUY REVIEW / COMPELLING ADD REVIEW** — deeper attractive valid threshold crossed; review underwriting then allocation only if supported, with the additional LEGACY prerequisite.
5. **BUY REVIEW NOW / ADD REVIEW NOW** — normal valid entry/add threshold crossed; same downstream gates and LEGACY prerequisite.
6. **GETTING CLOSE** — no valid trigger crossed, within 5% of the next valid price trigger. Display only; no new underwriting/action solely from proximity.
7. **NO ACTION** — no valid currently triggered review or price proximity. What to do: wait under this monitor; this is not proof that all thesis/portfolio risks are clear.
8. **UNAVAILABLE** — required state cannot support a reliable action classification. Retain readable price/trigger/source fields and name the gap.

Use ADD for verified owned, BUY for verified unowned and BUY/ADD review where ownership is unknown. COMPELLING BUY/ADD REVIEW and BUY/ADD REVIEW NOW are the corresponding unknown-ownership forms. Within equal priority sort meaningful severity/proximity then ticker. A non-price defense trigger maps to the review named by the sell-discipline workflow; do not invent numeric price levels for it.

### Selecting the one visible trigger per security

- Evaluate CANONICAL, LEGACY, and PORTFOLIO DEFENSE candidates together, then show the highest-urgency valid row.
- If a canonical monitor exists for a ticker, suppress equivalent legacy monitor thresholds for that ticker.
- A legacy monitor may still supply a distinct non-overlapping threshold only when the canonical monitor explicitly does not contain that threshold and the legacy record is clearly labeled as migration-pending; otherwise prefer canonical state.
- Portfolio Defense may supersede a buy/add row when an exit, trim, re-underwrite, time-stop, concentration, or instrument-failure review is more urgent.
- If multiple conditions are crossed, do not duplicate the security. A deeper nested compelling threshold supersedes ordinary entry; between upside/downside levels show the highest-priority valid active condition, otherwise the closest next valid trigger. Preserve all lower-priority conditions in audit state.
- Keep exact contract/listing identity and applicable lot/strategy explicit. Different instruments are different securities; records from multiple source classes are not additional securities.
- A consumed condition is inactive until its own explicit persisted re-arm condition is satisfied. Never infer re-arm, consume through publication or revive a condition because price stays beyond it. If missing history changes the action, retain price but mark the decision-dependent fields UNAVAILABLE.
- Prior fallback observations establish already-seen news, not missing canonical or legacy trigger-history state. Do not treat generic prose as an active LEGACY monitor.

## Failure and timestamp rules

If CANONICAL state contains no active price-bearing monitors, continue checking the persisted LEGACY monitor overlay and PORTFOLIO DEFENSE queue.

Show `NO ACTIVE STOCK MONITORS` only when all three source classes are readable and none contains a visible row.

If canonical state is empty but legacy rows exist, render them with `Source = LEGACY`; do not describe them as canonical active monitors.

If one source class is unavailable, preserve rows from readable source classes and label the table `PARTIAL` only when the missing class could materially change membership/action. State the missing class and its impact; when that impact is unknown, do not assert complete coverage. An unavailable quote or trigger field affects only the dependent row/decision. No readable universe means UNAVAILABLE, not an invented list or no-active result.

Report disabled/mapping-blocked records and missing-level/unstructured research separately in a compact coverage note where relevant. An all-three-empty queue does not establish that no research exists or no other portfolio risk exists. Retain unresolved research in its established view without manufacturing source-labelled rows.

A stale fallback may be shown only when useful, with its original cutoff and STALE FALLBACK label; it cannot establish a current valid crossed/armed trigger. Quote fallbacks follow the source hierarchy within reasonable time; unknown prices cannot become actionable price crossings or an all-clear.

At 08:00 use verified premarket or labelled previous close. At 11:00 and 15:00 use fresh actual regular-session prices when the relevant venue is open, otherwise explicitly dated last-session data. Never substitute stale premarket when a reliable regular-session value is available. Quote retrieval time is not necessarily trade time. Weekend/holiday data remain last-session, not fabricated live marks.

## Instrument and action boundary

Verify security/company, share class, intended venue, currency, ADR/CDR versus ordinary share, corporate actions and session. Preserve strategy/lot and each option's underlying, premium, strike, expiry and direction. An underlying price cannot be compared with an option-premium trigger or a different currency/listing without a valid explicit mapping. Missing delta means no invented delta-adjusted exposure; missing cash means no inferred total NAV or unsupported concentration breach.

`CANONICAL price review -> existing underwriting refresh -> if valid, allocation review -> human portfolio decision`.

`LEGACY review -> refresh/migrate underwriting first through its authorized workflow -> if validated, normal downstream review`.

`PORTFOLIO DEFENSE condition -> sell-discipline review -> downstream proposed decision when supported -> human execution`.

A crossing itself changes no thesis, fair value, position size, monitor boundary or holding. Fair value, dividend-inclusive total value and consensus targets are not automatic sell thresholds. A defense row is a review, not a final trim/sell. No orders, shorts, fills, holdings mutation, optional-workflow activation or history migration is authorized here. Closed-position reconciliation still requires an owned confirmed Holdings record under the sell contract.

## Persistence and regression checks

Save in supported research/manifest/fallback: canonical source/read time; monitor ID/status; ownership; all threshold/action versions; consumed/re-arm state; exact listing/currency/session and quote provenance/tier/time; stricter confirmation sources; conflicts/resolution; crossed/near/not-crossed state; selected action/next valid trigger; source dates; missing-field gaps and per-class coverage.

Also preserve:
- visible source class for each row;
- legacy monitor event/result identifier and original source date when Source = LEGACY or LEGACY + DEFENSE;
- legacy migration status and consumed/re-arm state when available;
- portfolio-defense trigger type and applicable position/lot/strategy when Source includes DEFENSE;
- de-duplication/suppression reason when canonical state supersedes a legacy threshold;
- exact-security de-duplication key and all materially contributing record IDs;
- disabled/migration-blocked conditions and reasons excluded from active queue membership.

Snapshots are audit history, not tomorrow's source of truth when live sources are readable. Retain compatible per-slot issue IDs with `report_format_version: 5` and `stock_table_schema: combined_action_queue_v1`; keep unsupported enrichment in the manifest/fallback rather than invalid API payloads. Publication neither consumes/re-arms a trigger nor proves delivery. Radar appends to the existing journal; the Daily Brief maintains the standing view using original cutoffs, without duplicating the full table in chat.

Regression cases: canonical empty + valid legacy still shows LEGACY; all three checked-empty alone allows NO ACTIVE STOCK MONITORS; missing material class produces PARTIAL; equivalent canonical/legacy uses canonical once; distinct legacy requires explicit absence and migration-pending state; higher-priority defense overrides a buy review without a sale; consumed legacy without satisfied explicit re-arm does not re-fire; relevant legacy REUNDERWRITE_REQUIRED outranks its price hit; disabled canonical is not revived via equivalent legacy; generic prose or stage RWC alone does not qualify as LEGACY; missing quote preserves valid non-price reviews but cannot activate a price comparison; exact currencies/contracts/lot scopes survive de-duplication. Verify the subroutine did not silently displace protected news discovery. Keep failures in the existing audit, not a new reporting service.
