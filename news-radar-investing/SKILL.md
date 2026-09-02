---
name: news-radar-investing
version: 3
description: Operate the high-recall, portfolio-aware front end of the public-equity research process. Detect and persist genuinely new events, actively test live Mind Model theses against their causal pillars, forecasts, falsifiers, and evidence gaps, surface slow-burn fundamental deltas, overdue evidence, known catalysts, clinical developments, filing changes, expert observations, and possible price-attribution errors; distinguish them from recycled coverage; prioritize risks to existing holdings and active underwritings; identify whether security underwriting is required; add a compact same-day market-tape summary; and route precise questions to Research With Confidence. Use for scheduled News Radar V3 runs, holdings-risk scans, active-thesis research, medical or cancer-trial radar, catalyst preparation, filing-delta review, expert or social-signal monitoring, and first-pass alert triage. Do not use for full causal research, complete value-capture analysis, valuation, final buy or sell decisions, event-trade approval, or account-specific position sizing.
---

# News Radar Investing V3

Operate the high-recall detection, memory, prioritization, thesis-testing, market-context, and routing layer of the investment process:

`News Radar V3 -> Research With Confidence -> Full Underwriting or Event-Trade Underwriting -> independent challenge when applicable -> Portfolio Capital Allocation -> Mind Model / monitoring`

Radar catches, normalizes, persists, actively tests approved theses, summarizes the same-day market tape, and routes. It does not prove the thesis, approve a thesis change, perform valuation, or declare a security investable.

## Stage boundary

Keep the stages distinct:

- **News Radar V3** owns detection, novelty control, canonical event memory, portfolio-defense priority, active-thesis testing, compact market-tape context, preliminary exposure mapping, underwriting-requirement classification, and the exact next question.
- **Research With Confidence** owns independent verification, causality, counterfactuals, confounders, economic materiality, value capture, and whether a plausible expectations gap survives.
- **Full Underwriting** owns current price, capital structure and dilution, reverse valuation, scenarios, expected return, downside, opportunity cost, time-to-resolution, kill criteria, and the final security posture.
- **Event-Trade Underwriting** owns discrete short-duration payoff states, break-even event probabilities, execution, liquidity, halt, gap, borrow, options, and slippage risk.
- **Portfolio Capital Allocation** owns loss budgets, weights, funding sources, cluster limits, and staged implementation.
- **Mind Model** owns the approved thesis record, causal pillars, forecasts, falsifiers, evidence ledger, watchlist transmission map, proposals, and decision history.

Do not let an interesting Radar item, thesis, or market narrative consume the time needed to complete the broader high-recall scan.

## References

Read only what the run needs:

- `references/v3-run-contract.md` is authoritative for the V3 schedule, run manifest, active-thesis research, market-tape summary, late-event recovery, overdue-evidence checks, underwriting-requirement classification, persistence, depth boundary, and compact output.
- `references/event-ledger-schema.md` for the canonical event record, novelty classes, thesis effects, observation types, and deduplication.
- `references/source-and-routing-rules.md` for source provenance, the five gates, priority routing, and scheduled-run behavior.
- `references/primary-source-feed-map.md` when defining source coverage, declaring scan limitations, or auditing missed feeds.
- `references/slow-burn-and-catalyst-lanes.md` for cumulative fundamental changes and pre-event expectations packets.
- `references/integration-and-persistence.md` when TaskTracker, Mind Model, Investing portfolios, Library fallback, or persistence are relevant.
- `references/social-arbitrage-lane.md` for behavioural or alternative-data observations.
- `references/clinical-radar-overlay.md` for medical research, clinical trials, regulator actions, and oncology alerts.
- `EXPERT_SOURCES.md` when monitoring named experts such as SemiAnalysis or Dylan Patel.

## Operating principles

- Optimize for **high recall with explicit uncertainty**, not a low-volume list containing only obvious winners.
- Treat every alert as a lead, not proof, a trade signal, an approved thesis update, or a valuation change.
- Protect existing capital first. Potential permanent-loss or thesis-breaking risk to a holding or active underwriting outranks new opportunity discovery.
- **Actively test approved theses.** Do not wait for generic news to happen to mention a thesis ticker. Search directly for the thesis's assumptions, causal pillars, forecasts, falsifiers, source-of-truth metrics, and next-highest-value tests.
- Add a **compact same-day market tape** to every scheduled visible run so the user can distinguish company-specific moves from broad rates, commodities, macro, geopolitical, sector, or factor pressure.
- Compare every claim with its prior baseline. A new article is not necessarily new information.
- Search for cumulative changes and missing expected evidence, not only dramatic headlines.
- For known catalysts and thesis forecasts, freeze expectations before the result whenever practical.
- Separate **source origin** from **claim status**. A company release is primary evidence of what management said, not independent proof that the economics are correct.
- Separate **observed market movement** from **causal attribution**. Do not present a market narrative as fact merely because prices moved together.
- Timestamp first publication, underlying event time, first Radar detection, market status, and any price or volume reaction.
- Never invent a reaction while the relevant market is closed or use a price move as proof that a new fundamental event exists.
- Do not manufacture an investment angle, fill an alert quota, or force symmetrical positive and negative stories.
- Keep world outcome, thesis evidence, company value capture, security valuation, event-trade suitability, and portfolio action separate.
- Automatically persist research-only Radar state when supported, but never automatically approve or change a thesis, fair value, security posture, monitor threshold, or holding.
- Every surfaced item must explicitly state whether underwriting is required, using the controlled classifications below.
- **Keep the visible chat concise but complete.** Target roughly 75% of the prior V3 visible length for an equivalent information set by removing repetition, not by reducing search coverage or required persisted state. The visible chat is the complete user-facing Radar response; no separate Markdown artifact is required.

## Authoritative schedule

Scheduled V3 runs use:

- **08:00 America/Toronto**
- **11:30 America/Toronto**
- **15:00 America/Toronto**

Use the scan window since the last successful run. If a run is advanced, delayed, skipped, partial, or failed, preserve the reason and ensure the next run covers the gap.

## Workflow

### 1. Preflight the current state

Before broad discovery, load or attempt to load:

- the last successful run and current scan window;
- open Event Ledger records and existing independence groups;
- open P0, P1, and P2 items;
- evidence due now or overdue;
- known catalyst dates and frozen packets;
- live holdings and active underwritings;
- current monitors, kill criteria, and review dates;
- the live TaskTracker Mind Model overview, including active theses, review queue, diagnostics, forecasts, evidence, watchlist exposures, linked Investor Research state, and pending proposals;
- same-day broad-market context available for the market tape;
- available feeds, outages, and likely blind spots.

Start the V3 run coverage manifest. If a required state source is unavailable, mark the gap and do not imply that the associated holdings, underwritings, theses, or market drivers were checked.

### 2. Run portfolio defense first

Search first for developments that could impair a holding or active underwriting, including:

- financing, liquidity, dilution, covenant, auditor, internal-control, fraud, safety, legal, regulatory, clinical, operational, customer-concentration, or governance risk;
- a breached or threatened kill criterion;
- a milestone, readout, financing, filing, permit, launch, or decision that was due but did not arrive;
- a material multi-holding or common-factor exposure.

P0 items take the fast path. Do not delay an urgent risk alert to complete thesis research, second-order beneficiary work, broad thematic mapping, or the market-tape summary.

### 2A. Run the Active Thesis Research lane

After urgent portfolio-defense work and before open-universe discovery, actively research the current non-retired Mind Model theses.

Use the live TaskTracker Mind Model overview when available. GitHub source, local seeds, migrations, or remembered thesis prose explain schema but are not confirmed production state.

For each active thesis, construct a compact **thesis search manifest** from the stored thesis rather than inventing generic search terms. Research the smallest set of current sources needed to test:

- thesis `baseline`, `summary`, `assumptions`, `investmentHypothesis`, and `strongestOpposingCase`;
- thesis-level `falsifiers` and `nextHighestValueTest`;
- every material causal pillar's `claim`, `mechanism`, `metric`, `baseline`, `target`, `targetDate`, `sourceOfTruth`, `falsifier`, and `nextHighestValueTest`;
- every open forecast's `statement`, `resolutionDate`, `metric`, `baseline`, `target`, `sourceOfTruth`, `confirmIndicators`, `warningIndicators`, and `breakIndicators`;
- watchlist exposure `mechanism`, `evidenceNeeded`, `falsifier`, `positionStatus`, linked `securityReadiness`, and linked underwriting status when available;
- thesis diagnostics such as `STALE`, `CONCENTRATED`, `CONFLICTED`, `MISSING_CHALLENGE`, `MISSING_FORECAST`, and `MISSING_PILLARS` when they change what evidence is most valuable to seek.

Do not give every thesis a full deep search three times per day. Run a cheap, explicit sweep across all active theses, then allocate deeper Radar search budget in this order when TaskTracker state supports it:

1. owned exposure whose review queue says `requiresReunderwrite`;
2. `EVENT_TRIGGERED` thesis;
3. owned exposure with `OVERDUE` review;
4. other `OVERDUE` thesis;
5. `DUE` thesis;
6. `BLOCKED` or materially `CONFLICTED` thesis;
7. normal active thesis whose forecast, falsifier, source-of-truth metric, or next-highest-value test has a timely observable update.

For each material thesis delta:

1. identify the exact thesis, pillar, forecast, falsifier, or watchlist exposure affected;
2. compare the new evidence with the stored baseline and existing evidence ledger;
3. preserve whether the evidence is `SUPPORT`, `CHALLENGE`, or `CONTEXT` and what it proves versus does not prove when the write path supports those fields;
4. apply the normal five gates and one primary Radar route;
5. classify the underwriting requirement;
6. route unresolved causal/economic questions to RWC;
7. persist research-only evidence, a linked research question, or a pending thesis proposal when supported and justified.

Radar may create evidence or a reviewable proposal, but it must never approve a proposal or directly change an approved thesis. A proposal is a record that evidence may justify a change, not the change itself.

A thesis with no material delta does not need a mini-report. Record it as checked in the run manifest.

### 2B. Build the compact market tape

Every scheduled visible run should include a short `What's moving markets today` section. This is **context**, not a substitute for event routing or thesis research.

Use the freshest same-day evidence available at the run cutoff:

- at **08:00**, use U.S./Canadian futures plus overnight global markets because regular North American trading is not open;
- at **11:30** and **15:00**, use actual same-day index/sector/factor movement rather than stale futures;
- check the S&P 500, Nasdaq/large-cap growth, and TSX when relevant; rates/yields, oil, FX, volatility, credit, or commodities only when they are materially influencing the tape;
- identify sector or factor leadership/weakness when it helps explain the user's portfolio moves.

Visible market-tape rules:

- **maximum 3 bullets and roughly 80–100 words total**;
- each bullet should combine the observed move with the best-supported driver, e.g. `Rates`, `Oil/geopolitics`, `AI/semis`, `Risk appetite`;
- distinguish `observed` from `reported/likely driver`; if attribution is unclear, say so;
- include an as-of time when using live prices;
- do not repeat a company-specific event already clear in the lead Radar table unless it is genuinely driving the broader market;
- do not promote a broad market move into P0/P1/P2 merely to populate the tape. It must independently pass the normal gates and portfolio/thesis relevance rules to become a Radar event;
- if market data or reliable attribution is unavailable, say `Market tape unavailable or attribution uncertain` rather than inventing a narrative.

The market tape should help answer: **Is today's portfolio move mostly market/factor-driven, or is there a company/thesis-specific delta?**

### 3. Scan the relevant lanes

Classify the run as one or more of:

- **Scheduled event scan** — the normal 08:00, 11:30, or 15:00 pass.
- **After-close capture** — record earnings, filings, trial results, and regulator actions for the next queue without automatically deep-researching everything.
- **User-supplied alert** — evaluate the exact item and its baseline.
- **Holdings-risk scan** — prioritize current capital at risk.
- **Active-thesis research** — test current Mind Model pillars, forecasts, falsifiers, and evidence gaps.
- **Slow-burn fundamental delta scan** — append and compare filings, calls, KPIs, estimates, trial records, capacity, financing, share count, risk factors, or monitor evidence.
- **Catalyst preparation** — create or refresh a frozen pre-event expectations packet.
- **Evidence-due scan** — check promised or scheduled evidence whose date or window has arrived.
- **Expert, social, or alternative-data scan** — identify original observations and preserve provenance.

Declare the actual source universe searched and unavailable feeds.

### 4. Reconcile every serious observation with the Event Ledger and thesis baseline

For every serious alert, thesis delta, cumulative pattern, or overdue-evidence item:

1. identify the original source and underlying event;
2. search for the most relevant prior guidance, filing, trial record, policy baseline, thesis pillar, forecast, monitor snapshot, or earlier reporting;
3. search the Event Ledger for the same underlying fact or independence group;
4. search the relevant Mind Model evidence ledger when a thesis is affected;
5. assign one `delta_class`, one `thesis_effect`, one `detection_status`, one primary route, and one underwriting-requirement classification;
6. group dependent coverage under one canonical `event_id`;
7. append atomic slow-burn observations rather than inventing a dramatic headline;
8. preserve a frozen catalyst or forecast packet and compare the result with it without rewriting the packet.

If the baseline is unknown, use `UNKNOWN`, state what must be checked, and do not call the event genuinely new.

#### Late-detection rule

If the underlying event predates the current scan window but no canonical record exists, classify it `LATE_DETECTION`, backfill it, measure latency, identify the likely missed-feed reason, and route it normally. Never reject a material unrecorded event merely because it should have been found earlier.

#### Missing-evidence rule

When expected evidence is absent or delayed, record the absence as an observation. Radar detects the change in the evidence state; RWC determines whether the absence is economically or probabilistically meaningful.

#### Price-dislocation rule

An unusual stock move can trigger a targeted source search, but price action alone does not pass Novelty. Use `PRICE_DISLOCATION_UNEXPLAINED` until an underlying event or defensible attribution is found.

### 5. Persist research-only state

For scheduled V3 runs, persist when supported:

- the run coverage manifest;
- canonical Event Ledger additions and updates;
- first-seen, detection, and event timestamps;
- duplicate and rejected items needed for calibration;
- atomic slow-burn observations;
- active-thesis research observations and checked-thesis coverage;
- thesis evidence records for genuinely new decision-relevant claims;
- linked Investor Research questions when the next missing fact is explicit;
- reviewable Mind Model proposals when evidence may justify a thesis change, without approval;
- underwriting-requirement classification and rationale;
- P2 evidence requests and due dates;
- catalyst packets;
- market-tape as-of time and high-level drivers when persistence supports it;
- feed outages, late detections, and persistence failures.

Use the supported canonical store. If unavailable, save a dated Library persistence record; its file format is not mandated. If no write path succeeds, report `PERSISTENCE_FAILED`.

Do not use Radar persistence to approve or change Mind Model probabilities, thesis wording, underwriting posture, fair value, entry ranges, kill criteria, review dates, or portfolio positions.

### 6. Apply the five hard gates

Assess each separately:

1. **Novelty** — is there a genuine information delta, independent confirmation, cumulative change, contradiction, new risk, or changed evidence state rather than repeated guidance, stale coverage, circular sourcing, or non-comparable data?
2. **Materiality** — could it materially change revenue, margins, cash flow, asset value, financing, probability, timing, thesis health, or permanent-loss risk?
3. **Capture** — is there a listed security or existing thesis with sufficiently direct economic exposure?
4. **Expectation** — is there a plausible reason the market may not fully understand the magnitude, duration, ownership, timing, second-order consequence, or attribution?
5. **Researchability** — can a named document, datapoint, counterparty, benchmark, thesis source of truth, or dated catalyst resolve the important uncertainty?

Failure of Novelty, Materiality, or Capture normally means `REJECT / DUPLICATE`. An unresolved Expectation or Researchability gate normally means `P2` or `P3`, not a forced rejection.

Radar establishes only a plausible expectations question. RWC determines whether a genuine expectations gap survives.

### 7. Map only enough exposure to route correctly

For every serious item record:

- direct holding or security;
- linked thesis, pillar, forecast, watchlist exposure, or underwriting;
- exposure type: `DIRECT`, `DERIVATIVE`, `READ_THROUGH`, or `NONE_IDENTIFIED`;
- preliminary mechanism;
- main capture uncertainty;
- portfolio cluster when relevant;
- linked security readiness and underwriting status when available.

Require a second-order beneficiary and a false friend or comparator only for P1 opportunity discovery, industry or class-level events, bottleneck shifts, policy changes, or cases where cross-company transmission is the point of the lead.

Do not complete detailed value-capture ranking inside Radar.

### 8. Route the event

Assign exactly one primary route:

- **P0 — HOLDINGS / THESIS RISK:** potential thesis break, financing/liquidity problem, fraud/safety/regulatory issue, clinical hold or rejection, breached kill criterion, break indicator, or another permanent-loss concern. Investigate first.
- **P1 — RESEARCH WITH CONFIDENCE NOW:** material, plausibly novel, economically traceable, and potentially misunderstood, misattributed, or incomplete.
- **P2 — TARGETED EVIDENCE:** one named fact, document, denominator, customer, comparator, causal link, thesis source of truth, or due item is missing. State exactly what and when.
- **P3 — MONITOR:** real development, but currently insufficient materiality, capture, expectation gap, or researchability.
- **REJECT / DUPLICATE:** false, stale, repeated without a new delta, immaterial, circularly sourced, inaccessible, non-comparable, or not meaningfully captured by a public security or active thesis.

Radar may flag a possible short-duration setup, but it must not convert recency into a trade. Route factual verification through RWC and event payoff or execution questions to Event-Trade Underwriting.

### 8A. Classify whether underwriting is required

Every surfaced P0, P1, P2, P3, and material thesis-research delta must include exactly one `Underwriting Required?` value:

- **`NO`** — evidence belongs in thesis/evidence monitoring; no security underwriting is currently needed.
- **`CONDITIONAL — AFTER RWC`** — the item could warrant underwriting, but causality, economic materiality, value capture, or expectations still need RWC. This is the normal classification for a new P1 candidate whose security work would be premature before RWC.
- **`YES — RE-UNDERWRITE EXISTING`** — an existing security underwriting may have materially changed and the remaining decision work is principally current price, scenarios, value, downside, timing, kill criteria, or posture. Use this when TaskTracker explicitly marks `requiresReunderwrite` or when verified evidence has crossed a current underwriting's material re-underwrite trigger.
- **`YES — NEW FULL UNDERWRITING`** — a new security has enough verified causal and capture evidence that valuation/security work is now the principal remaining step. Do not use this merely because an event is exciting; if RWC uncertainty remains material, use `CONDITIONAL — AFTER RWC`.
- **`YES — EVENT-TRADE UNDERWRITING`** — a discrete short-duration event has adequate factual support and the main remaining questions are payoff states, break-even probability, executable price, liquidity, options, halt/gap, borrow, or slippage.

This classification is routing metadata, not a valuation or investability conclusion. Radar must state the one-sentence reason for any `YES` or `CONDITIONAL` classification.

When live TaskTracker state is available, use it as an input rather than guessing:

- `reviewQueue.requiresReunderwrite` strongly supports `YES — RE-UNDERWRITE EXISTING`;
- linked watchlist `securityReadiness`, Investor Research `underwritingStatus`, owned position status, thesis review state, and current kill/review triggers should inform the classification;
- Mind Model transmission alone does not make a security decision-ready.

### 9. Enforce the hard depth boundary

A normal Radar item stops after establishing:

- what changed versus baseline;
- source origin, claim status, and independence;
- timestamps and market status;
- plausible materiality and preliminary mechanism;
- affected holding, thesis, pillar, forecast, or candidate set;
- five-gate results;
- strongest reason the lead may fail;
- primary route;
- `Underwriting Required?` and brief reason;
- three or fewer decisive RWC questions in the stored record;
- next evidence and date.

Stop and route when the remaining question is principally:

- causal attribution or counterfactual analysis;
- detailed economic materiality or value capture;
- complete expectations analysis;
- valuation, dilution, financing, scenario modeling, expected return, or timing;
- clinical-commercial underwriting;
- event payoff, options, liquidity, halt, borrow, or slippage;
- portfolio sizing, funding, cluster loss, or hedging.

Depth exceptions are limited to urgent P0 risk, comparison with an already frozen catalyst/forecast packet, retrieval of one time-sensitive classification document, or an explicitly requested combined workflow.

### 9A. Compress the visible response, not the research

The visible chat response should target roughly **75% of the prior V3 report length for an equivalent information set**. This presentation budget does not reduce source coverage, thesis sweeps, Event Ledger reconciliation, persistence, or required stored audit state. **The visible chat is the complete user-facing Radar response; no separate Markdown artifact or attachment is required.**

Apply these visible-output rules:

- Do not repeat a fact already clear from the lead table unless the prose adds causality, uncertainty, provenance, or routing information.
- P0/P1 visible detail blocks should normally be **120–160 words maximum each**. Exceed only for an urgent P0 when compression would make the classification misleading.
- Compress the five gates to shorthand such as `Gates: N/M/C/R pass; E unknown`. Spell out only a failed or ambiguous gate that changes routing.
- Show **one primary RWC question by default; maximum two** when genuinely independent. The stored record may preserve up to three.
- P2/P3 should normally stay in the lead table only. Add prose only for overdue/missing evidence, unusual classification, or material portfolio-risk context.
- Restate only the one or two baseline facts necessary to understand the delta.
- State the mechanism once; do not rephrase the same causal chain repeatedly.
- Mention only reconciliation items whose status changed. Otherwise use one sentence: `Open items reconciled; no additional decision-relevant delta.`
- Show the Thesis Research table only when a material thesis delta exists. Unchanged theses belong in the coverage summary.
- The `What's moving markets today` section is capped at **3 bullets / roughly 80–100 words total** and should not cause the response to exceed the compact-output budget materially.
- Compress the coverage manifest to one short closing paragraph in chat. Mention only material unavailable state, outages, blind spots, late detections, scan-gap recovery, and persistence status; persist the full manifest through the supported canonical store or dated Library fallback when available.
- Omit a separate visible source register unless provenance itself is decision-relevant. Use inline citations instead.
- Do not generate or link a separate Markdown file solely for Radar output.

### 10. Produce the queue, market tape, thesis-research result, and coverage result

Lead with:

| Priority | Event ID | What changed | Affected holding / thesis | Gate issue | Route | Underwriting Required? | Exact next question | Evidence / date |
|---|---|---|---|---|---|---|---|---|

Immediately after the lead table, add:

### What's moving markets today

Use up to three short bullets and roughly 80–100 words total. Cover only the broad drivers that are actually relevant to the day's tape. Separate observed price/index/factor movement from causal attribution and include an as-of time when using live market data.

For P0/P1, the visible detail block should normally contain only:

1. exact delta versus the one or two relevant baseline facts;
2. provenance only if it is not obvious from the table;
3. one-sentence mechanism/materiality;
4. gates shorthand;
5. strongest failure reason;
6. `Underwriting Required?` and brief reason;
7. one primary RWC question, maximum two;
8. next evidence/date only if not already clear from the table.

For P2 and P3, the table row is normally sufficient. Put missing evidence/date and underwriting requirement in the row rather than expanding into a mini-report.

When the Active Thesis Research lane finds a material delta, add a compact section:

| Thesis | What Radar tested | New evidence | Pillar / forecast affected | Direction | Route | Underwriting Required? | Next test / date |
|---|---|---|---|---|---|---|---|

Do not list unchanged theses row-by-row. Record checked theses in the persisted manifest and summarize them compactly at the end.

Preferred visible response order:

1. title + one-sentence run status;
2. lead table;
3. `What's moving markets today` — maximum 3 bullets / roughly 80–100 words;
4. compact P0/P1 detail only;
5. Thesis Research table only when needed;
6. one short `Other checks` paragraph only when needed;
7. one short coverage/persistence paragraph.

A valid no-lead run must be allowed. Say that no qualifying item was found in the searched universe, not that nothing material occurred anywhere.

## Handoff to Research With Confidence

A P0 or P1 handoff must preserve:

- `event_id`, lane, original source, and information cutoff;
- prior baseline, `delta_class`, `thesis_effect`, and `detection_status`;
- linked thesis, pillar, forecast, falsifier, or exposure when applicable;
- original Radar hypothesis;
- preliminary mechanism;
- direct exposure and main capture uncertainty;
- obvious confounders already visible without deep investigation;
- market-open/closed status and available price context;
- any frozen catalyst or forecast packet;
- strongest reason the lead may fail;
- `Underwriting Required?` classification and reason;
- three or fewer decisive questions in the stored handoff;
- next evidence and date.

Do not ask RWC to prove the Radar thesis. Ask it to determine whether the claim, causality, materiality, value capture, and expectations gap survive independent verification and whether the lead deserves Full Underwriting, Event-Trade Underwriting, targeted research, waiting, monitoring, or rejection.

## Slow-burn and thesis cadence

- Intraday runs append genuinely new atomic observations and sweep current thesis falsifiers/forecast indicators.
- A structured weekly review compares cumulative evidence with dated comparable baselines and reviews thesis diagnostics such as stale, concentrated, conflicted, missing challenge, or missing forecast.
- Earnings, material filings, trial updates, major operating disclosures, or thesis forecast resolution dates trigger a comparable-period delta check.
- Preserve history. Do not rewrite earlier observations, forecasts, or catalyst packets once the trend becomes obvious.

## Quality check

Before finishing, confirm that:

- the V3 coverage manifest was completed or its failure was declared;
- live holdings, active underwritings, monitors, theses, Mind Model review queue, catalysts, and evidence-due items were checked or explicitly marked unavailable;
- the Active Thesis Research lane swept every readable non-retired thesis at least cheaply and deeper work followed the priority order;
- the market tape was produced from same-day data or explicitly marked unavailable/uncertain, with observed moves separated from attribution;
- the original event and prior baseline were checked;
- affected thesis pillars, forecasts, falsifiers, and watchlist evidence gaps were checked when relevant;
- late detections were backfilled rather than discarded;
- overdue or missing expected evidence was checked;
- every event has one delta class, one thesis effect, one detection status, one primary route, and one underwriting-requirement classification;
- repeated coverage sharing one origin was deduplicated;
- source origin and claim status were not conflated;
- P0 risks were not delayed for thesis, thematic, or market-tape work;
- slow-burn evidence used comparable periods and preserved atomic observations;
- catalyst and forecast expectations were frozen before the outcome whenever practical;
- price action was not treated as proof of novelty;
- no RWC, underwriting, event-trade, thesis-approval, or portfolio conclusion was smuggled into Radar;
- every P0/P1 stored handoff has three or fewer decisive RWC questions, while visible output normally shows one and at most two;
- every P2/P3 item has named next evidence or a reason no further work is warranted;
- every material thesis delta states what it proves and does not prove when the persistence path supports those fields;
- the visible response obeyed the compact-output budget, including the 3-bullet market-tape cap, without reducing required persisted audit state;
- research-only state was persisted or `PERSISTENCE_FAILED` was declared;
- a valid no-lead run was allowed rather than lowering the gates.
