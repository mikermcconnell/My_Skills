---
name: system-design-expert
description: Practical system design workflow for software features and apps. Use when a non-trivial feature changes structure, module boundaries, data flow, frontend-vs-backend responsibility, shared business logic, or where code should live. Best used after prompt clarification and before implementation. Skip it for tiny low-risk tweaks.
---

# System Design Expert

Use this skill to put the right logic in the right place before implementation starts.

This skill is for practical feature and app design, not abstract architecture theatre. Use it to keep apps understandable as they grow, especially in AI-assisted codebases where unclear structure quickly turns into tangled structure.

## Read only what you need
- `references/system-design-workflow.md` for the standard workflow, boundary checks, and decision rules
- Use repo docs such as `AGENTS.md`, `AGENTS.md`, `ORCHESTRATOR.md`, architecture notes, or feature docs when they exist

## When to use this skill
Use this skill when:
- a new feature touches multiple files or layers
- the feature changes structure, not just behavior
- it is unclear whether logic belongs in the frontend, route, backend, service, or data layer
- shared business logic may be introduced or duplicated
- a route or component is starting to do too much
- a new import, export, dashboard, workflow, or operational tool is being added
- auth, validation, persistence, and business rules need clearer boundaries

Usually use this skill after `prompt-expert` and before implementation.
Skip it for tiny UI tweaks, simple copy changes, or obvious single-file fixes.

## Workflow

1. Define the feature clearly
- What problem is this feature solving?
- What inputs, outputs, users, and business rules matter?
- What parts of the app are affected?

2. Map responsibilities
- What belongs in the UI?
- What belongs in request or route handling?
- What belongs in business logic?
- What belongs in data access or persistence?
- What belongs in auth, config, or infrastructure?

3. Decide boundaries
- Where should the main logic live?
- What should be the single source of truth?
- What should not be duplicated across layers?
- What changes together and should stay together?

4. Check data flow and coupling
- Where does data enter?
- Where is it validated?
- Where is it transformed?
- Where is truth stored?
- What will become harder to change if this is placed here?

5. Recommend the simplest shape that fits
- Prefer clear module boundaries over clever abstractions
- Prefer modular monolith patterns over premature service splits
- Offer options only when there is a real decision to make
- Choose the structure the current team can actually operate and maintain

6. Turn the design into implementation guidance
Always state:
- what files or modules should own the logic
- what should stay out of the frontend
- what should not be mixed together
- what future duplication or coupling risk to watch for

## Core rules
- Put business rules in a clear, reusable place
- Keep routes focused on orchestration, not heavy domain logic
- Keep frontend focused on display and interaction, not source-of-truth rules
- Prefer small clear abstractions only after repeated need appears
- Ask what changes together before splitting modules
- Design for clarity, testability, and future edits, not theoretical scale alone
- If the structure is still emerging, keep it simpler and more reversible

## Output format
When useful, structure your output like this:
- Feature summary
- Responsibilities map
- Boundary decisions
- Data flow notes
- Main coupling or duplication risks
- Recommended structure
- Implementation guidance

## Good prompts this skill should handle
- Where should this new feature live in the app?
- Help me decide what should be frontend vs backend for this workflow
- Review this plan for boundary problems before we build it
- This route is getting messy — how should we restructure it?
- What is the simplest clean shape for this new module?
