# Source reliability, sector balance and capture audit

Approved October 5, 2026. Apply this overlay during existing Radar runs and the existing internal Portfolio Checks task. It changes collection and calibration, not Core/Camillo gates, the eleven lanes, investment thresholds, subscriptions or trading authority.

## Contents

1. Collection and source health
2. Specialist coverage
3. Consumer evidence
4. After-hours intake
5. Weekly missed-event audit
6. Public worker and persistence

## 1. Collection and source health

Read `source-reliability-register.json`. Use the narrowest source closest to the event; reuse fresh receipts before collecting again. A configured source is not a live connection. For every due source retain source ID, exact scope/URL, attempted/retrieved times, source version/date, captured depth, access status, last full success and next due/retry. Preserve the last good snapshot during an outage, explicitly dated; never represent it as a new observation.

For material holdings/catalysts, resolve the actual issuer, SEC CIK where relevant, designated IR/news index, regulator/registry and next disclosure window from verified current state. Keep this private mapping in the existing Journal/supported store; do not publish the holdings universe. Scan SEC current filings beyond holdings as part of protected discovery when accessible. Use issuer submissions/filing documents for targeted follow-through; use SEDAR+/Canadian issuer/exchange originals for Canadian cases. A company page, EDGAR help page or search hit is not proof the current filing feed was inspected.

For important primary documents use authorized direct/API/connector access first, then one differentiated public-search/issuer fallback. Record any remaining filing, regulator, clinical, court or IR gap. Stop after access/rate blocks rather than changing identities. Declared SEC contact is runtime configuration, never fabricated or printed; lack of it leaves scripted SEC collection UNAVAILABLE while authorized public-source alternatives remain eligible.

Health states distinguish HEALTHY for a defined verified scope, PARTIAL, STALE_DATA, OVERDUE, UNAVAILABLE and UNVERIFIED. COMPLETE collection describes the requested feed/snapshot only, not every event on the platform. A provider's unchanged version is not a collection failure or new independent observation. A missing source timestamp prevents claiming data freshness even when retrieval succeeded.

Source outages affecting a material imminent holding/catalyst receive a bounded P0/P1 evidence-gap review according to actual risk. Ordinary outages remain internal plus a compact source-health note. Do not add a full source dashboard to routine reports.

## 2. Specialist coverage

Use the sector pairs in the register alongside SemiAnalysis and existing technical/lab sources. Check the four independent sector indexes once at 08:00, incrementally at 11:00/15:00 only when new publication evidence or a due case warrants it. Check the relevant primary counterpart when a decision-relevant lead appears. Do not read every full article on every run.

The initial pairs cover power/energy, shipping/logistics, fintech/payments and consumer/retail. Keep source incentives explicit: official statistics/decisions, issuer/exchange claims, industry-association surveys and independent journalism are different evidence types. Shipping logistics coverage is not a tanker freight/fixture dataset. Finextra homepage index access is verified; its /news route failed in this environment. Baltic numeric-data access remains unverified until actually read. Broaden a relevant inaccessible source with an accessible original/counterparty source; retain the failed source's gap.

These sources feed the existing four broad families and expert/industry/social lanes. They do not create new lanes, recurring tasks or investment candidates by quota.

## 3. Consumer evidence

For Apple collect the entire requested 100-row JSON when available using `camillo_source_snapshots.py` or `radar_source_health.py`; preserve the full snapshot privately, then publish only material changes. A 10/100 excerpt is PARTIAL even if the top ten appear unchanged. Follow existing free/paid US/CA/GB cadence and preserve provider/device/category distinctions. Capture Android full accessible scope and provider version; never splice AppBrain into Apple/direct-Play history.

Use numeric anomalies to select a bounded, dated original-review/release sample, including disconfirming accounts. Track repeat use, payment, switching, abandonment and product reliability separately from attention. Preserve review sample count/selection/version/geography and promotions. Prefer actual disclosed active users, retention, purchases or transactions when available. Where unavailable, state the missing denominator and next check; do not invent population estimates. EARLY Camillo leads remain eligible before mature confirmation.

Keep Google RSS, Explore/custom-term series and ordinary search distinct. Follow `google-trends-connection.md`, at most one due Google invocation per slot. The public registered-feed worker does not collect custom Trends histories or repair restricted social/API access. Quantitative Pinterest, retail rankings and authenticated/restricted social feeds remain gaps until actual receipts show usable content. No paid service is enabled.

## 4. After-hours intake

Run bounded material-holding/catalyst primary-source intake inside the existing **Portfolio Checks task at 16:15 and 19:15 America/Toronto on weekdays**. Keep its identity and urgent-only notification role. Preserve the earlier risk check; the second check recovers late earnings/filings and relevant official decisions. No fourth routine Radar report or new task.

Use the last verified after-hours family/source cutoff with overlap. Inspect current issuer IR/filings, exact due earnings/catalysts, relevant regulator releases and counterparties. Label unfamiliar-company leads when encountered but do not claim this targeted intake completes Core's open-universe pass. Keep 16:15 and 19:15 occurrence IDs distinct and reuse common origins. Notifications remain immediate only when delay until 08:00 materially matters under existing risk rules; otherwise append research-only findings for the next Radar.

At 08:00 read both verified after-hours receipts and reconcile new origins before discovery. Recover missing windows; a successful internal check cannot advance unsearched broad-family cutoffs. Events after 19:15 are captured by the next morning/other established urgent channel; this is scheduled, not continuous coverage.

## 5. Weekly missed-event audit

At Friday 15:00 reuse the existing calibration block. Freeze selection rules before the measurement window. First live window: **October 5 15:00 through October 9 14:00 Toronto**, with evaluation at October 9 15:00. This starts after the implementation opportunity; earlier retrospective examples are labelled diagnostic only.

Build a 20-event target sample from the independent benchmark indexes in the register, using the first four unique qualifying origins per stratum chronologically: issuer filings/operating-financing; official clinical/regulatory; non-AI industry/customer changes; product/consumer behaviour; macro/policy. Use at least U.S./Canada source opportunities and retain international material where the fixed indexes expose it. Material means a concrete operating, financing, approval, safety, policy, supply/demand or product/use change, not stock-price commentary alone. Include good, adverse and ultimately immaterial hypotheses; do not select on whether Radar found them, price outcome or known winners. Less than 20 eligible events is a smaller disclosed sample, not a quota to fill.

During scheduled slots, preserve incremental benchmark-index candidate receipts and exclusions independently of Radar seen-history. Reuse public-index reads already obtained in discovery; perform at most one bounded due missing-index check and label unsearched intervals. Do not filter candidates because Radar already found them or because their hypothesis later failed. Friday assembles the frozen chronological sample from this candidate history and faithful index backfill; absent history or an inaccessible window remains a sampling/coverage limitation, not a retroactively complete benchmark.

Save selection rule/version, frozen_at, source/index strata and actual interval before collecting outcomes. Assemble events from the fixed indexes independently of Radar seen-history; retain exclusion reasons and deduplicate shared origins. For each event record first public availability, family/market, original URL/ID, an ex-ante detection deadline, first Radar/verified-fallback detection, first report surfacing and actual delivery if available.

Deadline is the next scheduled 08:00/11:00/15:00 Radar opportunity after public availability. For a material held/due catalyst between 15:00 and 19:15 weekdays, use the next 16:15/19:15 internal opportunity. Preserve scheduled deadline and actual cutoff separately; do not move deadlines to make late runs pass. Urgent risks also report raw latency and whether established urgency rules were satisfied.

Classify ON_TIME, LATE, MISSED or UNSCORABLE_COVERAGE_GAP. Missing detection plus unavailable history/incomplete source windows is unscorable, not a proven miss or zero. Compute on-time sample capture using scorable events; show sample size, unscorable count and limitations alongside it. Separate detection, surfacing and delivery delay, duplicate origins and the cause of each missed/late item. No global capture-rate or return claim from this sample. One small audit does not justify a higher comprehensiveness score.

Use `scripts/radar_source_health.py audit` when execution is available; it checks identity/time/coverage arithmetic, not the truth of supplied receipts. Otherwise apply the same rules manually and label helper execution NOT_RUN. Append results to the existing Journal and summarize only material fixes in Friday Radar. No separate audit report/task or parallel database.

## 6. Public worker and persistence

`scripts/radar_source_health.py collect` captures a fixed allowlist of Apple JSON, Federal Reserve RSS and SEC current Atom (SEC contact must be provided securely at runtime). It makes at most eight distinct bounded source requests, does not follow redirects, rejects HTML/empty malformed feeds, and stops further same-host requests after 401/403/429. No private portfolio input, credentials lookup, account access, broker action or remote investment write.

When local networking is unavailable, the existing `.github/workflows/camillo-trends-probe.yml` may run its **Public registered-feed probe**. It has no cron and no new automation. Verify exact code/input/live-step scope before a supported rerun; frozen reruns do not update code/terms. Defaults capture Apple US/CA/GB free and paid plus Fed RSS. This expansion is authorized by the October 5 source-reliability work; the existing Trends step and single-Google-invocation limits are preserved separately. A green test is not successful source retrieval.

Read actual receipts and full artifact snapshots. Artifacts expire after seven days: copy relevant full rows and receipts to the existing private Journal/supported source store before expiry. Public workflow evidence may contain only fixed public-source observations, never private mappings, holding/case records, journals or contacts. Report configured, tested, scheduled-executed, persisted and delivered separately. If no supported execution path exists, retain UNAVAILABLE and continue accessible discovery.

Record SOURCE_HEALTH_V1, SOURCE_CAPTURE_AUDIT_V1 and AFTER_HOURS_SOURCE_RECEIPT_V1 in the existing authorized Journal when native schemas lack these fields. Preserve stable occurrence/source/origin IDs and append-only history, use revision protection/read-back, and never invent strict API fields or tickers. These records are research-only and cannot activate a monitor, approve a proposal, change holdings or place a trade.
