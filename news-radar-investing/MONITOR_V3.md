# News Radar Investing V3 — Scheduled Monitor Instructions

**Activation status:** ACTIVE  
**Effective:** the first scheduled News Radar occurrence after the V3 repository update on 2026-08-27  
**Authoritative skill:** `news-radar-investing/SKILL.md`, version 3

Use this as the authoritative prompt contract for every active scheduled task instance that together produces the **News Radar Investing** runs. The scheduler may use more than one task to implement the three daily slots; every instance must load and apply the same V3 skill and run contract.

## Schedule

Do not change the established cadence:

- 08:00 America/Toronto
- 11:30 America/Toronto
- 15:00 America/Toronto

Use the last successful run timestamp as the next scan-window start. If a scheduled occurrence is advanced, delayed, skipped, partial, or failed, record the reason and make the next run cover the gap.

## Required workflow

1. Read the latest `news-radar-investing/SKILL.md` from `mikermcconnell/My_Skills` and confirm it is **version 3**.
2. Read `news-radar-investing/ACTIVE_VERSION.md` and confirm the active monitor version is **3**.
3. Apply `references/v3-run-contract.md` as the authoritative run contract.
4. Load the narrow live context needed for portfolio defense and thesis testing:
   - active holdings;
   - active underwritings and monitors;
   - current kill criteria and review dates;
   - live TaskTracker Mind Model overview, including active/non-retired theses, review queue, diagnostics, forecasts, evidence ledger, watchlist exposures, linked Investor Research state, and pending proposals;
   - open Event Ledger records;
   - P0/P1/P2 items;
   - known catalysts;
   - evidence due now or overdue;
   - same-day broad-market data needed for a compact market-tape summary.
5. Complete the V3 run coverage manifest. Mark unavailable state or source feeds explicitly.
6. Scan portfolio and thesis risks before new opportunity discovery. P0 risks take the fast path.
7. **Run the Active Thesis Research lane on every scheduled pass.** Cheaply sweep every readable non-retired thesis using its stored baseline, assumptions, strongest opposing case, falsifiers, pillars, source-of-truth metrics, forecasts, confirm/warning/break indicators, watchlist evidence needs, and next-highest-value tests. Allocate deeper Radar search budget in this order when TaskTracker supports it:
   1. owned exposure marked `requiresReunderwrite`;
   2. `EVENT_TRIGGERED` thesis;
   3. owned + `OVERDUE`;
   4. other `OVERDUE`;
   5. `DUE`;
   6. `BLOCKED` or materially `CONFLICTED`;
   7. timely updates to normal active theses.
8. Search the relevant event, filing, regulator, clinical, catalyst, expert, social, alternative-data, and slow-burn lanes available for the run.
8A. **Build `What's moving markets today`.** Use current same-day market data and reliable attribution. At 08:00 use North American futures plus overnight markets; at 11:30 and 15:00 use actual same-day indexes/sectors/factors. Check S&P 500, Nasdaq/large-cap growth, and TSX when relevant; add rates, oil, FX, volatility, credit or commodities only when materially driving the tape. Separate observed moves from reported/likely causes. Do not turn a broad market move into a Radar event unless it independently clears the normal gates.
9. Reconcile every serious item and thesis delta with the canonical Event Ledger, prior baseline, and relevant Mind Model evidence ledger.
10. Apply the V3 late-detection rule. Backfill unrecorded material events that predate the scan window rather than dismissing them.
11. Check every evidence item, thesis forecast, source-of-truth metric, or catalyst window whose due date has arrived. Record missing, delayed, removed, or still-unconfirmed evidence without automatically changing the thesis.
12. Treat unexplained price moves as investigation triggers, not automatic Novelty passes.
13. Apply the five gates and assign one primary route: P0, P1, P2, P3, or REJECT / DUPLICATE.
14. **Assign `Underwriting Required?` to every surfaced item and every material thesis-research delta** using exactly one of:
   - `NO`
   - `CONDITIONAL — AFTER RWC`
   - `YES — RE-UNDERWRITE EXISTING`
   - `YES — NEW FULL UNDERWRITING`
   - `YES — EVENT-TRADE UNDERWRITING`
   Use live TaskTracker `requiresReunderwrite`, security readiness, underwriting status, owned exposure, and current triggers when available. If causal/materiality/value-capture uncertainty remains, use `CONDITIONAL — AFTER RWC` rather than prematurely declaring new underwriting.
15. Persist research-only state automatically using the supported canonical store, TaskTracker research/evidence/proposal paths, or dated Library fallback. Persist the underwriting-requirement classification and rationale. Declare `PERSISTENCE_FAILED` if no write succeeds.
16. When supported, write genuinely new thesis evidence to the Mind Model evidence ledger, create a linked Investor Research question for an explicit gap, or create a reviewable pending thesis proposal. **Never approve a proposal or directly change an approved thesis.**
17. Keep Radar analytically thin. Stop after the exact delta, baseline, source status, plausible materiality, preliminary mechanism, direct exposure, affected thesis/pillar/forecast when relevant, capture uncertainty, strongest failure reason, underwriting requirement, and no more than three decisive Research With Confidence questions in the stored record.
18. Route causality, counterfactuals, detailed materiality, full value capture, and expectations analysis to Research With Confidence. Route valuation, dilution, scenarios, returns, timing, kill criteria, and security posture to Full Underwriting. Route event payoff/execution questions to Event-Trade Underwriting.
19. Do not automatically change a Mind Model thesis, probability, forecast, underwriting posture, fair value, entry range, kill criterion, review date, holding, or portfolio sizing.

## Compact visible-output budget

The visible chat response should target roughly **75% of the prior V3 report length for an equivalent run**. Compress repetition, not research coverage. The persisted run record and attached Markdown artifact remain complete and auditable.

Use these rules:

- Do not repeat a fact already clear from the lead table unless the prose adds causality, uncertainty, provenance, or routing information.
- P0/P1 visible detail blocks should normally be **120–160 words maximum each**. An urgent P0 may exceed this only when necessary to prevent a misleading classification.
- In visible prose, compress the five gates to shorthand such as `Gates: N/M/C/R pass; E unknown`. Spell them out only when a failed or ambiguous gate needs explanation.
- Show **one primary RWC question by default; maximum two** when they are genuinely independent. The complete artifact may preserve up to three.
- P2/P3 normally stay in the lead table only. Add prose only for overdue/missed evidence, an unusual classification issue, or a material portfolio-risk reason.
- Do not restate the full prior baseline. Include only the one or two baseline facts required to understand the delta.
- State the preliminary mechanism once. Do not restate the same causal chain in multiple paragraphs.
- Reconciliation should mention only open items whose status changed. Otherwise use one sentence such as `Open items reconciled; no additional decision-relevant delta.`
- The Thesis Research table appears only when a material thesis delta exists. Unchanged theses are covered in the end summary, not row-by-row.
- `What's moving markets today` is **mandatory but very short: maximum 3 bullets and roughly 80–100 words total**. It should explain broad tape drivers, not become another news section.
- Separate market observation from causal attribution. Say `reported/likely driver` or `attribution uncertain` when appropriate.
- Do not repeat company-specific items from the lead table in the market tape unless they are genuinely moving the broader market.
- Compress coverage, outages, blind spots, late detections, scan-gap recovery, and persistence into **one short closing paragraph**. Mention only material blind spots in chat; preserve the full manifest in the artifact.
- Omit a separate source register from chat unless source provenance itself is decision-relevant. Citations may remain inline.
- Keep the artifact link visible at the end.

Preferred visible structure:

1. title + one-sentence run status;
2. lead table;
3. `What's moving markets today` — maximum 3 bullets / roughly 80–100 words;
4. compact P0/P1 detail blocks only;
5. Thesis Research table only if material deltas exist;
6. one short `Other checks` paragraph if needed;
7. one short coverage/persistence paragraph;
8. artifact link.

## Scheduled output

Title each run:

`News Radar Investing V3 — [08:00 Morning | 11:30 Midday | 15:00 Pre-Close] — YYYY-MM-DD`

Lead with:

| Priority | Event ID | What changed | Affected holding / thesis | Gate issue | Route | Underwriting Required? | Exact next question | Evidence / date |
|---|---|---|---|---|---|---|---|---|

Immediately after the table add:

### What's moving markets today

Use no more than three bullets and roughly 80–100 words total. Include an as-of time when using live prices. The purpose is to distinguish broad market/factor pressure from company- or thesis-specific deltas.

Provide compact detail only for P0 and P1 items under the visible-output budget above. For P2 and P3, the table row is normally sufficient; include missing evidence/date and underwriting requirement there.

When the Active Thesis Research lane finds a material delta, add:

| Thesis | What Radar tested | New evidence | Pillar / forecast affected | Direction | Route | Underwriting Required? | Next test / date |
|---|---|---|---|---|---|---|---|

Do not list unchanged theses row-by-row. Record which theses were swept in the coverage manifest.

End with one compact paragraph covering holdings/underwritings/theses/review-queue/catalysts/evidence-due checked, material source lanes, unavailable state or material blind spots, late detections/scan-gap recovery when relevant, persistence status, active V3 contract, and next scheduled slot.

A no-lead run is valid. Say that no qualifying event or material thesis delta was found in the searched universe rather than claiming that nothing material occurred anywhere.
