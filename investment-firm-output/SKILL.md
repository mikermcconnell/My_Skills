---
name: investment-firm-output
version: 11
revision: 2026-09-24-two-strategy-lanes
description: Publish the existing Investment Firm reports with visible Core long-term portfolio and Camillo speculative information-edge cases, separate strategy-specific monitoring and unchanged Event Reaction mechanics. Preserve source coverage, delivery coordination and execution boundaries.
---

# Investment Firm output contract — version 11

Read ../investment-strategy-lanes/SKILL.md, then BASELINE_WORKFLOW.md. The baseline preserves the complete version-10 output, source and delivery rules. Apply the following scoped changes; all unrelated rules remain. Actual existing automation schedules take precedence over historical prose about a brief's nominal time. Do not change cadence or task identity.

## Every Radar report

Retain exactly the three main sections:
1. New news and opportunities.
2. Changes to existing investment cases.
3. Stock monitor — Buy / Hold / Wait / Sell.

Within each, explicitly distinguish **CORE — Long-term portfolio** and **CAMILLO — Speculative information edge**. Both labels remain visible on quiet runs with truthful no-change, no-mapped-case or incomplete-coverage notes. Do not print a second full copy of shared news; cross-reference one origin and state each strategy implication.

Under Stock monitor retain **Event Reaction — strategy mechanics** first when applicable. Then show:

### CORE — Long-term portfolio

Keep the baseline action queue and all valid canonical/legacy/defense safeguards. Add Strategy case / exact instrument where required to disambiguate. Unclassified existing cases retain their accepted rules in a clearly labelled unresolved-mapping subsection, not an invented Core assignment.

### CAMILLO — Speculative information edge

| Edge state | Stock / case / instrument | Price / as-of | Recognition / falsifier / next review | Stage / next action | Source / record status |
|---|---|---|---|---|---|

Include readable dated Camillo research cases even without price triggers; explicitly label RESEARCH CASE — NOT AN ACTIVE TRADE MONITOR when that is all the record supports. Show active risk/price monitors with their actual provenance and accepted conditions. No invented price level or CANONICAL source label. State research-case coverage separately from active-monitor coverage.

A Camillo edge state is not BUY/SELL approval. Preserve supported review versus completed-decision distinctions. No forcing a promising Camillo case to WAIT solely because it is above a Core buy target. Missing quotes block price-dependent decisions, not factual evidence updates.

Action deduplication is by strategy case + exact security/instrument/lot, not ticker alone. Preserve source precedence inside that scope; aggregate actual exposure without counting a shared lot twice. Opposing instructions for the same real lot require allocation reconciliation.

## Research, underwriting and synthesis

Investment RWC and Underwriting begin with Strategy / Case / Stage / Horizon. When both are assessed, show a two-row conclusion summary with separate reasoning and next steps; otherwise identify the other lane as not assessed. Full requested research remains available without duplicating analysis for display.

Daily Brief retains Your decisions / What changed / Research progress / What comes next, with strategy-labelled items. Portfolio Defense distinguishes Core thesis/value reviews from Camillo evidence/recognition/timing reviews while preserving Event Reaction. Standing Decision List refreshes preserve strategy-case identity and original cutoffs; never overwrite historical research or holdings to fit the layout.

Report annotations and new edge states are not declarations of backend schema support. Persist only accepted fields or authorized fallback. Preserve private reporting bindings outside public GitHub, source honesty, case history, consumed/re-arm state, fresh revisions, no automatic execution and the difference between saved configuration, completed run and actual delivery.
