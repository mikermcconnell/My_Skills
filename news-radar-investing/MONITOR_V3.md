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
   - evidence due now or overdue.
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
17. Keep Radar analytically thin. Stop after the exact delta, baseline, source status, plausible materiality, preliminary mechanism, direct exposure, affected thesis/pillar/forecast when relevant, capture uncertainty, strongest failure reason, underwriting requirement, and no more than three decisive Research With Confidence questions.
18. Route causality, counterfactuals, detailed materiality, full value capture, and expectations analysis to Research With Confidence. Route valuation, dilution, scenarios, returns, timing, kill criteria, and security posture to Full Underwriting. Route event payoff/execution questions to Event-Trade Underwriting.
19. Do not automatically change a Mind Model thesis, probability, forecast, underwriting posture, fair value, entry range, kill criterion, review date, holding, or portfolio sizing.

## Scheduled output

Title each run:

`News Radar Investing V3 — [08:00 Morning | 11:30 Midday | 15:00 Pre-Close] — YYYY-MM-DD`

Lead with:

| Priority | Event ID | What changed | Affected holding / thesis | Gate issue | Route | Underwriting Required? | Exact next question | Evidence / date |
|---|---|---|---|---|---|---|---|---|

Provide concise detail only for P0 and P1 items. For P2 and P3, state the missing evidence/date and underwriting requirement without a mini deep dive.

When the Active Thesis Research lane finds a material delta, add:

| Thesis | What Radar tested | New evidence | Pillar / forecast affected | Direction | Route | Underwriting Required? | Next test / date |
|---|---|---|---|---|---|---|---|

Do not list unchanged theses row-by-row. Record which theses were swept in the coverage manifest.

End with:

- holdings and active underwritings checked;
- active theses, review-queue items, catalysts, and evidence-due items checked;
- thesis-research coverage and any unavailable Mind Model state;
- source lanes searched;
- unavailable state, feed outages, and blind spots;
- late detections and scan-gap recovery;
- persistence status;
- active Radar version and monitor contract used;
- next scheduled slot.

A no-lead run is valid. Say that no qualifying event or material thesis delta was found in the searched universe rather than claiming that nothing material occurred anywhere.
