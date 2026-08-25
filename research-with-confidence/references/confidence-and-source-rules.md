# Confidence and Source Rules

## Confidence is claim-specific

Use the narrowest useful scale:

- **Very High:** direct primary or independently replicated evidence; material alternative explanations are unlikely.
- **High:** multiple strong sources or one decisive primary source with limited unresolved conflict.
- **Medium:** credible support exists, but an important denominator, causal link, timing issue, or conflict remains.
- **Low:** the claim depends on a single weak source, speculative inference, contradictory evidence, or an unobserved assumption.
- **Unresolved:** evidence is insufficient to choose among material alternatives.

Do not average confidence across unrelated claims. A report can have High confidence in the technology trend and Low confidence in one company's commercial success.

## Source origin and claim status

Record separately:

### Origin

- regulator/court/government;
- filing/exchange notice;
- company or sponsor;
- official registry/dataset/standards body;
- independent structured data;
- high-quality journalism;
- named expert/practitioner;
- anonymous source;
- social/forum observation.

### Claim status

- reported fact;
- official finding;
- company claim;
- independent confirmation;
- channel check or observation;
- derived calculation;
- researcher inference;
- unsupported assertion.

Primary does not mean unbiased. Secondary does not mean useless. Judge proximity, incentives, methods, and reproducibility.

## Independence groups

Count evidence by origin, not article count. Common shared-origin patterns include:

- many outlets citing one press release;
- syndication of one newswire article;
- commentary repeating one analyst note;
- several social posts quoting the same screenshot;
- a sponsor release repeating a registry update.

Independent evidence comes from a materially separate observation, counterparty, dataset, regulator, customer, supplier, or method.

## Claim ledger

For each load-bearing claim record:

```text
claim
claim_type
supporting_evidence
challenging_evidence
independence_groups
derived_calculation
remaining_unknown
confidence
confidence_reason
next_decisive_evidence
```

## Common traps

- repeated citations mistaken for consensus;
- new publication mistaken for new information;
- company guidance mistaken for independent validation;
- a strong mechanism mistaken for proof of scale;
- a large numerator without the relevant denominator;
- market price movement used as proof of causality;
- a source limitation relabeled as opposing evidence;
- several weak observations outweighing one decisive primary fact;
- exact probabilities that cannot be supported;
- hindsight changing what was supposedly knowable at the original date.

## Confidence versus decision readiness

Keep separate:

- **evidence confidence** — how strongly the claim is supported;
- **decision readiness** — whether the material economics, risks, timing, and alternatives are sufficiently known to act;
- **mispricing confidence** — whether the security price likely embeds a different outcome.

High evidence confidence does not automatically make a security investable.
