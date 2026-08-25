---
name: mind-model
description: Maintain and evaluate TaskTracker Mind Model theses using atomic evidence, event novelty, thesis-effect classification, source independence, calibrated probability changes, and explicit competing outcomes. Always use when researching, discussing, scoring, forecasting, changing probabilities, extracting source evidence, classifying SUPPORT, CHALLENGE, or CONTEXT, or developing an investment implication for a strategic or investing thesis.
---

# Mind Model

Turn sources and resolved events into calibrated, falsifiable thesis evidence without artificial balance or duplicate counting.

## Non-negotiable rules

There is no target mix of supporting, challenging, or contextual evidence.

- A source may be entirely supporting, entirely challenging, or contextual only.
- Never invent, stretch, or relabel a claim to balance counts.
- Repeated coverage sharing one origin is one evidentiary observation.
- A new article is not automatically new evidence.
- Event novelty, thesis effect, evidence stance, and investment action are separate classifications.
- No Radar, RWC, monitor, or model result automatically changes thesis wording, probability, status, valuation, or holdings.

## Reference

Read `references/evidence-classification.md` when a stance is unclear, the thesis is hybrid/coexistence, or the event may be repeated guidance or confidence-only evidence.

## Workflow

### 1. Read the current thesis and revision

Before evaluating evidence, read:

- exact thesis wording and scope;
- baseline and current probability range;
- named competing outcomes;
- assumptions and mechanism;
- measurable forecasts and resolution dates;
- strongest opposing case and falsifiers;
- investment hypothesis and current revision.

Restate the thesis as a falsifiable claim. Define scenario boundaries before classifying evidence for a hybrid or coexistence thesis.

### 2. Reconcile the Event Ledger record when one exists

Record separately:

- `event_id` and original source;
- prior baseline;
- `delta_class`: GENUINELY_NEW, REPEATED_GUIDANCE, INDEPENDENT_CONFIRMATION, ACCELERATION, DECELERATION, CONTRADICTION, RISK_DISCLOSURE, or UNKNOWN;
- `thesis_effect`: INTRINSIC_VALUE_CHANGE, PROBABILITY_CHANGE, TIMING_CHANGE, CONFIDENCE_ONLY, MONITOR_ONLY, or NO_CHANGE;
- information cutoff and first-seen time.

A genuinely new event may still be `MONITOR_ONLY`. Repeated guidance may be `NO_CHANGE`. Independent confirmation may change confidence without changing the central forecast.

Do not create a new evidence record merely because another article repeats the same event. Link it to the existing event and independence group.

### 3. Assess source quality separately from direction

Record:

- proximity to the underlying fact;
- source origin and claim status;
- reliability, methods, and limitations;
- author or sponsor incentives;
- independence group;
- publication date, information cutoff, and original URL.

Reliability affects strength, not stance. A promotional company source can support a thesis; label it SUPPORT with appropriate limitations rather than disguising it as context.

### 4. Split into atomic decision-relevant claims

Create one evidence record per claim that can change the thesis, forecast, or interpretation. Do not summarize every paragraph.

For each claim ask:

> If this claim is true, does it make this exact thesis or measurable forecast more likely, less likely, or neither?

Classify:

- `SUPPORT` — raises probability of the thesis or forecast.
- `CHALLENGE` — lowers probability or raises a named competing outcome.
- `CONTEXT` — changes mechanism, scope, timing, uncertainty, or interpretation without materially moving probability.

When ambiguous, explain why and use CONTEXT; do not force a challenge.

### 5. Check for thesis leakage and duplicate evidence

Watch for:

- evidence for one side of a hybrid thesis automatically treated as proof of coexistence;
- a source limitation mislabeled as a challenge;
- a manufactured strongest opposing case;
- many articles sharing one original source counted separately;
- a repeated target treated as a fresh probability update;
- several weak records outweighing one decisive primary fact;
- intrinsic-value changes mixed with world-outcome probability changes.

Rejected or missed Radar events belong in the calibration record. They become Mind Model evidence only when they contain a claim that actually bears on the thesis.

### 6. Update probability by impact, not votes

Assess the change using:

- independence;
- proximity and reliability;
- magnitude and relevance;
- strength of the causal connection;
- novelty relative to baseline;
- whether the evidence discriminates among competing outcomes;
- whether the effect changes probability, timing, confidence, or intrinsic value.

State `raise`, `lower`, or `no change`. Use ranges only when justified. Leave probability unchanged for repeated guidance, weakly linked context, or non-independent confirmation that does not change the model.

### 7. Keep the investment conclusion separate

Evaluate independently:

1. probability of the world outcome;
2. which company or security captures value;
3. whether the financial effect is material;
4. whether intrinsic value or only confidence/timing changed;
5. whether the current security price is attractive;
6. whether the idea clears the portfolio hurdle and opportunity cost.

A high-probability thesis can remain `NO_TRADE`, `LOW_CONVICTION`, or `WATCH`.

### 8. Write safely to TaskTracker

When a write is explicitly requested:

1. read or back up the latest overview immediately before writing;
2. capture the original source and Event Ledger link before evidence;
3. add only justified atomic evidence records;
4. preserve independence groups and do not duplicate one origin;
5. submit wording, probability, status, forecast, or investment changes as a proposal against the latest revision;
6. never approve or claim approval as an API-key agent;
7. reread and verify source IDs, evidence IDs, proposal status, revision, and persistence.

## Output standard

Report:

- prior thesis and competing outcomes;
- event delta class and thesis effect when applicable;
- source origin, claim status, and independence group;
- natural SUPPORT / CHALLENGE / CONTEXT records;
- probability effect and reason, including no change;
- timing and intrinsic-value effects separately;
- investment implication, including no trade;
- unresolved questions and next evidence/date;
- proposal status when persistence was requested.

Never praise a result for being balanced. Praise it for being accurate, independent, novel, and discriminating.
