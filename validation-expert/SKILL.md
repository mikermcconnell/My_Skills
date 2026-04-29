---
name: validation-expert
description: Practical output-validation workflow for software tools, schedules, dashboards, metrics, maps, imports, planning outputs, and decision-support work. Use when the question is whether an output should be trusted in real use, what assumptions matter, what sanity checks are needed, or what confidence level is appropriate.
---

# Validation Expert

Use this skill to decide whether a result is trustworthy for the real-world use case.

This skill is for outputs that may influence planning, operations, interpretation, recommendations, or decisions.

## Read only what you need
- `references/output-validation-workflow.md` for the standard workflow, confidence levels, and common validation checks
- Use repo docs such as `AGENTS.md`, `AGENTS.md`, `ORCHESTRATOR.md`, or `TESTING.md` when they exist

## When to use this skill
Use this skill when:
- reviewing a metric, dashboard, schedule, map, import result, summary, or planning output
- checking whether an output is decision-ready
- pressure-testing assumptions behind a feature or calculation
- deciding whether a technically correct result is still misleading or incomplete
- preparing stakeholder-facing or operationally important outputs
- assessing confidence level and what review is still needed

## Workflow

1. Define the purpose
- What is this output for?
- Is it exploratory, internal, operational, public-facing, or decision-support?

2. Review source data
- What data is this based on?
- Is it complete enough, current enough, clean enough, and representative enough?

3. Surface assumptions
- What assumptions are built into the output?
- Which assumptions matter most?
- Are they reasonable in the real context?

4. Review logic and interpretation
- Is the formula, rule, or method the right one?
- Could the output be technically correct but still misleading?

5. Run sanity checks
- Does this align with what is already known?
- Does the result look plausible in real use?
- What would a domain expert question first?

6. Decide confidence and review needs
- Low, medium, or high confidence
- What remains uncertain?
- Is stakeholder or domain review needed before action?

## Core rules
- Do not confuse tested output with validated output
- Do not treat technically correct output as decision-ready by default
- Always surface assumptions for meaningful outputs
- Prefer practical sanity checks over abstract certainty claims
- Call out when incomplete data or weak assumptions reduce confidence
- If the output may influence action, state whether human domain review is still needed

## Output format
When useful, structure your validation output like this:
- Output purpose
- Source data concerns
- Key assumptions
- Interpretation risks
- Sanity checks
- Confidence level
- Recommended next review step

## Good prompts this skill should handle
- Validate this dashboard metric before we rely on it
- What assumptions are built into this Scheduler output?
- Review this planning summary for validation risk
- Is this output decision-ready or only exploratory?
- What would Jason or Robin likely challenge in this result?
