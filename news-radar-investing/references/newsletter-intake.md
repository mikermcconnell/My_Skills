# Registered Newsletter Intake — News Radar V3

Approved September 22, 2026. This contract turns high-signal specialist newsletters into deterministic Investment Firm inputs without creating a new Radar lane, scheduled task, or automatic investment recommendation.

## Purpose

Registered newsletters are **expert-source discovery feeds**. Each new issue is treated as one source origin that may contain multiple atomic claims, observations, models, forecasts, or investment hypotheses.

Flow:

`registered issue -> detect/deduplicate -> extract incremental claims -> classify source/claim type -> map exposures & Emerging Signals -> Radar route -> RWC verification when warranted -> underwriting only after RWC -> monitoring handoff for unresolved evidence`

Do not summarize every issue for its own sake. Extract only the parts that can change a thesis, open a research question, identify an Emerging Signal, alter a bottleneck/value-capture map, or reveal a new public-market opportunity/risk.

## Registered-source record

Maintain each source with:

```text
source_id
publisher
tier: A | B | C
source_type
homepage_or_issue_index
optional_sitemap_or_feed
topic_strengths
typical_edge
known_biases_or_methodological_limits
primary_verification_sources
last_checked_at
last_unique_issue_url
last_unique_issue_published_at
historical_rwc_survival_when_available
notes
```

Tier meanings:

- **A — routine issue intake:** high expected decision value; check issue index during every scheduled Expert / Industry Sources pass.
- **B — targeted intake:** check when relevant to active theses/sectors or when surfaced by broad discovery.
- **C — opportunistic:** use as discovery/context when encountered.

Tier is about expected research value and latency, not truthfulness. Even Tier-A claims require normal provenance and independent verification.

## Issue detection and deduplication

For Tier-A sources, each 08:00, 11:00 and 15:00 Toronto Radar pass should check the publisher's current issue index, homepage, sitemap/feed, or another supported canonical listing.

Prefer the **canonical issue URL + publication timestamp + title** as the issue identity. Email, homepage card, social promotion, syndicated excerpt, and canonical URL for the same issue are one origin.

Record:

```text
newsletter_issue_id
source_id
canonical_url
title
authors
published_at
first_detected_at
access_state: FULL | PARTIAL | PAYWALLED | UNAVAILABLE
issue_independence_group
```

A new issue is not automatically material. If already seen in canonical/fallback history, do not create another Radar discovery merely because a social/email wrapper appeared later.

## Intake when web access is partial or paywalled

If the canonical web issue is partial/paywalled:

1. preserve the accessible title, author, date and claims actually visible;
2. when an authorized Gmail source is available and the user receives the newsletter, search the matching sender/title/date as a **content-access fallback**;
3. treat the email and web page as the same issue origin;
4. never claim full-issue coverage unless the full issue was actually readable;
5. do not bypass publisher access controls or invent unseen claims.

## Atomic claim extraction

For each potentially material issue, extract only incremental, decision-relevant items. Each atomic item should preserve:

```text
claim_id
newsletter_issue_id
claim_text_or_precise_paraphrase
claim_type: REPORTED_FACT | DATA_OBSERVATION | CHANNEL_CHECK | TECHNICAL_MODEL | DERIVED_CALCULATION | FORECAST | EXPERT_INTERPRETATION | INVESTMENT_HYPOTHESIS
prior_baseline
what_is_incremental
independence_group
affected_sector_or_security
preliminary_mechanism
main_capture_uncertainty
emerging_signal_archetype_when_relevant
next_verification
route
```

One newsletter may contain many claims, but **the issue itself remains one source origin**. Internal models/figures derived from one proprietary dataset are not independent confirmations of one another.

## Three-layer separation

Always separate:

1. **Factual / observable evidence** — data, architecture, company behavior, deployments, supply, pricing, benchmarks, filings or other observations.
2. **Author analysis** — interpretation, causal model, bottleneck thesis, forecasts, architecture/economic judgments.
3. **Investment mapping** — which public securities may capture/lose value and whether expectations may lag.

Radar can preserve all three, but RWC must independently verify material load-bearing claims and value-capture mapping before Full Underwriting.

## Routing

Apply normal five gates and Emerging Signal logic:

- **P0:** credible urgent permanent-loss/thesis risk.
- **P1 RWC NOW:** material expert thesis or data sequence with plausible economic transmission and a real expectations/value-capture question.
- **P2 TARGETED EVIDENCE:** useful thesis with one or more decisive missing facts, denominator, customer/supplier verification, or economic mapping.
- **P3 MONITOR:** interesting but early/weakly material or too uncertain.
- **REJECT / DUPLICATE:** recycled, unsupported, immaterial, or no credible public-market capture.

Do not route directly from newsletter to BUY/SELL, accepted thesis, fair-value change, or live monitor threshold.

## RWC handoff requirements

A P1/P2 newsletter handoff should include:

- canonical issue identity and publication time;
- exact incremental claims, separated by type;
- what comes from publisher proprietary modeling versus externally verifiable evidence;
- strongest methodological assumption or source incentive;
- affected existing theses/holdings/candidates **only when live context is readable**;
- plausible second-order beneficiaries, losers, and non-beneficiaries;
- Emerging Signal / Signal Sequence mapping where applicable;
- the two or three decisive independent checks;
- what would falsify the newsletter's interpretation;
- route and next evidence/date.

RWC should not re-summarize the whole newsletter. It should test the **load-bearing claims and value-capture chain**.

## Source calibration

Over time retain:

`issue -> material atomic claims -> RWC survival/revision/rejection -> underwriting advancement -> monitoring/decision relevance`.

Use this to calibrate source priority and topic-specific trust. Do not create a simplistic accuracy score. A source may be excellent at technical architecture and weak at public-equity value capture, or vice versa.

Demote a source only after confirming another feed captures its valuable unique events with acceptable latency.

## Initial registered source

### SEMIANALYSIS

```text
source_id: SEMIANALYSIS
publisher: SemiAnalysis
tier: A
source_type: TECHNICAL | CHANNEL | DATA | EXPERT_RESEARCH
homepage_or_issue_index: https://newsletter.semianalysis.com/
optional_sitemap_or_feed: https://newsletter.semianalysis.com/sitemap
topic_strengths: semiconductors; AI accelerators; inference/training systems; networking; optics; memory/storage; packaging/foundry; datacenter power/cooling; hyperscaler/lab infrastructure; bottlenecks; vendor share and roadmaps
typical_edge: product-first technical modeling, supply-chain/channel work, system architecture, proprietary datasets/models, cross-stack economic mapping
known_biases_or_methodological_limits: forward-looking architecture assumptions can be model-sensitive; proprietary datasets/models may not be independently reproducible; technical importance does not automatically equal listed-equity capture; author/vendor views must be separated from externally verified facts
primary_verification_sources: vendor technical documentation; hyperscaler/lab disclosures; customer/supplier filings; conference materials; benchmark artifacts; regulator/export-control records; capex/procurement evidence; independent industry/customer data
```

SemiAnalysis / Dylan Patel and relevant contributors remain priority discovery sources under `EXPERT_SOURCES.md`. This registry makes **new issue intake deterministic** rather than relying on ad hoc discovery.

## Initial live issue

First issue registered under this contract:

- Title: `Computation and Data Movement for Inference`
- Author: Tanj Bennett
- Publication date: September 21, 2026
- Canonical URL: `https://newsletter.semianalysis.com/p/computation-and-data-movement-for`

Treat this as the first live regression case for issue identity, claim extraction, RWC routing, and fallback-aware deduplication. Do not hard-code its claims as permanent architecture truth; later evidence may support, refine, or reject them.