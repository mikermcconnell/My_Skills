# News Radar Investing V3 — Scheduled Monitor Instructions

Use this as the authoritative prompt for the existing scheduled monitor named **News Radar Investing**.

## Schedule

Run at:

- 08:00 America/Toronto
- 11:30 America/Toronto
- 15:00 America/Toronto

Use the last successful run timestamp as the next scan-window start. If a scheduled occurrence is advanced, delayed, skipped, partial, or failed, record the reason and make the next run cover the gap.

## Required workflow

1. Read the latest `news-radar-investing/SKILL.md` from `mikermcconnell/My_Skills` and confirm it is **version 3**.
2. Apply `references/v3-run-contract.md` as the authoritative run contract.
3. Load the narrow live context needed for portfolio defense:
   - active holdings;
   - active underwritings and monitors;
   - current kill criteria and review dates;
   - active Mind Model theses and watchlist;
   - open Event Ledger records;
   - P0/P1/P2 items;
   - known catalysts;
   - evidence due now or overdue.
4. Complete the V3 run coverage manifest. Mark unavailable state or source feeds explicitly.
5. Scan portfolio and thesis risks before new opportunity discovery.
6. Search the relevant event, filing, regulator, clinical, catalyst, expert, social, and slow-burn lanes available for the run.
7. Reconcile every serious item with the canonical Event Ledger and prior baseline.
8. Apply the V3 late-detection rule. Backfill unrecorded material events that predate the scan window rather than dismissing them.
9. Check every evidence item whose due date or catalyst window has arrived. Record missing, delayed, removed, or still-unconfirmed evidence without automatically changing the thesis.
10. Treat unexplained price moves as investigation triggers, not automatic Novelty passes.
11. Persist research-only state automatically using the supported canonical store, TaskTracker research record, or dated Library fallback. Declare `PERSISTENCE_FAILED` if no write succeeds.
12. Apply the five gates and assign one primary route: P0, P1, P2, P3, or REJECT / DUPLICATE.
13. Keep the Radar analytically thin. Stop after the exact delta, baseline, source status, plausible materiality, preliminary mechanism, direct exposure, capture uncertainty, strongest failure reason, and no more than three decisive Research With Confidence questions.
14. Route causality, counterfactuals, detailed materiality, full value capture, and expectations analysis to Research With Confidence. Route valuation, dilution, scenarios, returns, timing, and security posture to Full Underwriting.
15. Do not automatically change a Mind Model thesis, probability, underwriting posture, fair value, entry range, kill criterion, review date, or holding.

## Scheduled output

Title each run:

`News Radar Investing V3 — [08:00 Morning | 11:30 Midday | 15:00 Pre-Close] — YYYY-MM-DD`

Lead with:

| Priority | Event ID | What changed | Affected holding / thesis | Gate issue | Route | Exact next question | Evidence / date |
|---|---|---|---|---|---|---|---|

Provide concise detail only for P0 and P1 items. For P2 and P3, state the missing evidence and date without a mini deep dive.

End with:

- holdings, active underwritings, theses, catalysts, and evidence-due items checked;
- source lanes searched;
- unavailable state, feed outages, and blind spots;
- late detections and scan-gap recovery;
- persistence status;
- next scheduled slot.

A no-lead run is valid. Say that no qualifying event was found in the searched universe rather than claiming that nothing material occurred anywhere.
