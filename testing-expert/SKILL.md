---
name: testing-expert
description: Practical feature-by-feature testing workflow for software repositories. Use when implementing meaningful features, fixes, refactors, data logic, imports, dashboards, schedules, or whenever tests, edge cases, regression risks, or manual verification should be planned and generated consistently.
---

# Testing Expert

Use this skill to make testing a standard part of delivery.

This skill is for practical software work, especially when AI is writing or changing code and the user wants confidence that the result works.

## Read only what you need
- `references/feature-testing-workflow.md` for the standard workflow, output format, and risk-based priorities
- Use repo docs such as `AGENTS.md`, `AGENTS.md`, `ORCHESTRATOR.md`, or `TESTING.md` when they exist

## When to use this skill
Use this skill when:
- building a meaningful feature
- fixing a bug with regression risk
- changing calculations, business rules, or data transformations
- working on imports, exports, dashboards, schedules, maps, or planning outputs
- adding tests to an existing repo
- deciding what should be tested automatically vs manually
- preparing release verification for a risky change

## Workflow

1. Define the change
- What is the feature or fix supposed to do?
- What inputs, outputs, and business rules matter?

2. Identify risk
- List failure modes
- List edge cases
- List regression risks
- Focus on what would be expensive or embarrassing to get wrong

3. Split the testing work
- Automated logic tests
- Manual workflow checks
- Regression checks
- Sanity checks for real-world plausibility

4. Generate the highest-value tests first
- Start with calculations, business logic, filters, transforms, validation, and scheduling logic
- Prefer focused tests over broad shallow coverage
- Keep tests readable

5. Create a manual verification checklist
- Main user flow
- One realistic case
- One edge case
- One regression check
- Output plausibility check

6. Close with a verification summary
Always state:
- what was tested automatically
- what was tested manually
- what edge cases were considered
- what remains untested
- whether the feature is tested enough for its risk level

## Core rules
- Test behavior, not implementation trivia
- Prioritize high-risk logic before low-risk UI polish
- Treat AI-generated code as unproven until tested
- Prefer a small number of valuable tests over coverage theatre
- Do not claim work is done until testing and verification are addressed
- If tests are missing because the repo is not set up yet, say so and still provide the test plan and manual checklist

## Output format
When useful, structure your testing output like this:
- Feature summary
- Failure modes
- Edge cases
- Automated tests to add
- Manual verification checklist
- Regression risks
- Verification summary

## Good prompts this skill should handle
- Add this feature and make sure testing is handled properly
- What tests do we need for this dashboard change?
- Write the tests for the risky logic first
- Give me a manual verification checklist for this import flow
- Review this feature and tell me what is still untested
