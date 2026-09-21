# Price Monitor Live-Source Contract — News Radar V3

Reconciled September 21, 2026. This file owns dynamic monitor membership, quote verification, internal trigger classification and consumed/re-arm controls. The latest `investment-firm-output/SKILL.md` owns visible labels and publication. The price lane supplements news discovery; it is not the boundary of Radar's news universe.

## Place within the scheduled run

At each existing **08:00, 11:00 and 15:00 America/Toronto** daily Radar run, publish this lane's simple stock table as the third section of the combined news/case-change/stock report. Keep all eleven specialist checks. Do not create another table notification, dashboard or task; do not defer ordinary new news exclusively to the Daily Brief.

Read/attempt urgent monitor/ownership context during bounded preflight. Complete routine all-name quote assembly and ordinary price-trigger review after the protected broad-discovery pass under `v3-run-contract.md`. Genuine urgent risk can preempt discovery with a recorded coverage gap. The field-resolution order below describes the price subroutine, not permission to replace the full run with price checking.

Visible table:

| Stock / position | Latest price | Buy / add level | Trim / sell-review level | What to do | Why / next step |
|---|---:|---|---|---|---|

Include unchanged HOLD/WAIT names and distinguish exact instruments/strategies where decisions differ. BUY/ADD/HOLD/WAIT/TRIM/SELL/REVIEW means what the shared output contract defines. Internal BUY REVIEW remains REVIEW until required actual current downstream work completes. A plain recommendation can relay a current supported completed decision, not manufacture one from a crossing. No automatic trading.

## Dynamic source of truth

Query actual available canonical live monitor/underwriting state each run and enumerate currently active price-bearing records, including non-owned candidates. Preserve monitor ID/status, current thresholds/ranges, stored downstream actions, ownership linkage, kill/review state, consumed triggers and re-arm logic. Changes flow into the next run from that source; no skill edit should be needed per ticker.

Never use a fixed ticker/level list, old prompt, analyst target, previous Radar table or remembered underwriting as live membership. Do not retain removed/disabled monitors, miss newly active ones or cache superseded actions/trigger state. Unknown membership is not a checked-empty list.

Independently readable actual accepted current Library baselines absent from app monitors can appear only in a **REFERENCE SCREEN — monitor linkage unverified** portion of the same table. Read actual source plus newer decisions and retain original date; a quote comparison is not an active/armed trigger, refreshed underwriting, approved migration or trade-ready decision. Exclude reference-only rows from armed/new-trigger counts. Never reactivate explicitly disabled records. Include actual live holdings with missing recovered levels as missing-level coverage rows, not invented targets. Empty app arrays do not erase accepted research; unavailable sources do not mean empty arrays.

## Independent data planes

Canonical monitor state owns membership/status, levels/actions, ownership-linked conditions, trigger history and next valid workflow. Market-price state owns the price, exact instrument, currency, session, timestamp and provenance. Failure of one must not erase readable values from the other.

Fresh price but missing re-arm/trigger: show price, unavailable trigger/action and REVIEW with the exact gap. Readable trigger but unavailable quote: keep the stored level, mark quote missing and no price comparison. Unknown ownership but otherwise valid trigger/quote: retain the internal BUY/ADD REVIEW classification without guessing ownership; final personalized action/sizing remains unverified. Never use UNAVAILABLE as a blanket replacement for a successfully retrieved quote.

## Price subroutine sequence

1. Read live monitor state and active membership, resolving exact instrument and ownership where supported.
2. Retrieve current threshold/action versions, consumed/re-arm conditions, monitor ID and review/kill state.
3. Get the freshest reliable quote for each exact instrument at the actual comparison cutoff using the hierarchy below.
4. Confirm near/crossed or ambiguous observations under the stricter rule below.
5. Determine currently valid crossed/near/not-crossed state mechanically, respecting consumed/re-arm conditions.
6. Select the highest-priority active review or closest next valid trigger per decision expression; preserve all underlying levels in the audit.
7. Keep completed downstream recommendation separate from trigger state and translate under the output contract.
8. Record monitor/quote as-of times, source tiers, confirmation, gaps and coverage; publish inside the combined report without mutating trigger state.

## Quote-source hierarchy

Use the best appropriate source actually accessible; a preferred provider failure alone is not a reason to declare all prices missing.

**Tier 1 — direct/consolidated/official market data.** Prefer a timestamped direct market-data tool, exchange feed or consolidated/official quote with unambiguous mapping. Examples include U.S. exchange-backed/consolidated feeds, TMX/TSX/TSXV for Canada and the relevant Euronext/local venue elsewhere. One verified Tier 1 observation may support ordinary not-near rows, and may meet the confirmation standard below when clearly current and exact.

**Tier 2 — high-quality aggregator.** For U.S. equities prefer StockAnalysis when direct tooling is unavailable and a same-day timestamped quote is exposed; preserve any stated real-time/delayed/feed provenance rather than assuming it. It is not a source of monitor membership. Use a suitable timestamped local-market provider for other listings.

**Tier 3 — reputable secondary source.** Investing.com, MarketScreener or a comparable provider can fill gaps when exact instrument/currency/session/time are clear. Check fragmented small-cap and international mappings especially carefully.

**Tier 4 — indirect snippets/news, last resort only.** A stale article or unverified search snippet may supply explicitly dated context, not activate current BUY/ADD, TRIM, EXIT, near-trigger or re-underwrite price actions. Preserve the original timestamp and indirect/stale status; do not call the observation executable or current.

## Near/crossed confirmation

Require confirmation when a first quote is within **5% of the next valid trigger**, appears through any valid entry/add/compelling/trim/exit/kill/review threshold, shows a classification-sensitive unusual move or has ambiguous symbol/share class/currency/venue/session.

Use **two current observations from differentiated sources**, or **one clearly timestamped direct/consolidated/official Tier 1 quote** with unambiguous mapping. Differentiated sources need not be independent economic data generators, but must help detect stale caches, wrong symbols, currencies or sessions. Record both sources/timestamps when used; do not portray different-time quotes as simultaneous.

If disagreement could change classification, do not average. Investigate exact instrument, session/time, corporate action/split, currency and delay. Keep a clearly superior quote visible if justified; unresolved disagreement leaves internal action UNAVAILABLE and visible REVIEW. Preserve reliable fields without issuing a guessed comparison.

## Internal review queue

Retain the audit format `Action | Stock | Current price | Next trigger | What to do`. This is not a competing scheduled user report. Controlled order:

1. **RE-UNDERWRITE NOW** — active canonical material review/kill trigger; run the required existing review before a portfolio decision.
2. **EXIT REVIEW NOW** — active stored exit/kill-price workflow; refresh and decide downstream, never automatic exit.
3. **TRIM REVIEW NOW** — valid valuation/trim boundary; refresh valuation before a reduction recommendation.
4. **COMPELLING BUY REVIEW / COMPELLING ADD REVIEW** — deeper attractive valid threshold crossed; review underwriting then allocation if still supported.
5. **BUY REVIEW NOW / ADD REVIEW NOW** — normal valid entry/add threshold crossed; same downstream gates.
6. **GETTING CLOSE** — no valid trigger crossed, within 5% of the next valid trigger. Display only; no new underwriting/action solely from proximity.
7. **NO ACTION** — no valid crossing/proximity; this means no new price-trigger action, not no thesis/portfolio risk.
8. **UNAVAILABLE** — required state cannot support a reliable classification.

Use ADD for verified owned, BUY for verified unowned and BUY/ADD review where ownership is unknown. Within equal priority sort meaningful severity/proximity then ticker. User-facing stock decisions follow the shared contract's priority and plain labels.

If multiple thresholds are crossed, display the highest-priority valid action for that expression, not duplicate rows. A deeper nested compelling threshold supersedes ordinary entry. Between upside/downside levels show the active valid condition, otherwise nearest next valid trigger. Different options/strategies may need distinct rows; do not collapse incompatible decisions into an issuer-wide recommendation.

A consumed trigger is inactive until its explicit canonical re-arm condition is satisfied. Do not infer re-arm logic, consume it through publication or revive it because price stays beyond it. Its price relationship can remain visible as already reviewed. If missing trigger history changes the action, retain price but mark trigger/action unavailable. An old fallback observation can establish already-seen news for reporting, but cannot establish missing canonical re-arm state.

## Failure and timestamp rules

If only one field fails, show the smallest missing field. If some membership/records/quotes are missing, label PARTIAL and retain valid rows. If no canonical membership can be read, say live active monitor membership/state unavailable and do not rebuild it from prior tables. Separately readable accepted-source reference rows remain reference-only. If a source is checked-empty, say NO ACTIVE PRICE MONITORS IN THIS SOURCE, not no historical research or no held securities.

A stale fallback may be shown only when useful, with its original cutoff and STALE FALLBACK label; it cannot establish a current valid crossed/armed trigger. Quote fallbacks follow the source hierarchy within reasonable time; unknown prices cannot become BUY/SELL or an all-clear.

At 08:00 use verified premarket or labelled previous close. At 11:00 and 15:00 use fresh actual regular-session prices when the relevant venue is open, otherwise explicitly dated last-session data. Never substitute a stale premarket value when a reliable regular-session one is available. Quote retrieval time is not necessarily trade time. Weekend/holiday data remain last-session, not fabricated live marks.

## Instrument and action boundary

Verify security/company, share class, intended venue, currency, ADR/CDR versus ordinary share, corporate actions and session. Preserve strategy/lot and each option's underlying, premium, strike, expiry and direction. An underlying price cannot be compared with an option-premium trigger or a different currency/listing without a valid explicit mapping. Missing delta means no invented delta-adjusted exposure; missing cash means no inferred total NAV.

`PRICE TRIGGER -> existing underwriting refresh -> if valid, allocation review -> human portfolio decision`.

A crossing itself changes no thesis, fair value, position size, monitor boundary or holding. Fair value, dividend-inclusive target-date total value and consensus analyst estimates are not automatic sell thresholds. A sourced current completed downstream recommendation can be shown plainly only under the shared output gates. This never authorizes orders, shorts, fills, holdings mutation, optional workflow activation or history migration.

## Persistence and regression checks

Save in supported research/manifest/fallback: canonical source/read time; monitor ID/status; ownership; all threshold/action versions; consumed/re-arm state; exact listing/currency/session and quote provenance/tier/time; stricter confirmation sources; conflicts/resolution; crossed/near/not-crossed state; selected internal action/next valid trigger; visible supported recommendation provenance; source dates for accepted references; linkage/missing-field gaps and coverage.

Snapshots are audit history, not tomorrow's source of truth when live sources are readable. Keep the compatible stock snapshot within the same combined Radar issue; its publication neither consumes/re-arms a trigger nor proves delivery. Radar appends to the existing journal; the Daily Brief maintains the standing view using original cutoffs, without duplicating the full table in chat.

Validate no missed intended names, no invented targets from memory, no missing-price BUY/SELL, no consumed-trigger repeat, correct currency/options, and reference-only separation. Also verify this subroutine did not silently displace protected news discovery. Keep failures in the existing run audit, not a new reporting service.
