---
name: prompt-expert
description: Tightens vague, ambiguous, or overloaded prompts before execution. Use when a short refinement step will prevent wasted work, the wrong implementation, or unnecessary back-and-forth. Prefer concise clarification only when needed; otherwise state assumptions and proceed.
---

# Prompt Expert

Use this skill to improve rough prompts without slowing down momentum.

This skill is for situations where the user's request is unclear enough that acting immediately could waste time, produce the wrong result, or create avoidable rework.

## Main rule
Do not turn every prompt into a workshop.

- If the request is clear enough and risk is low, proceed.
- If the request is ambiguous and the wrong assumption would matter, refine it first.
- Ask the fewest questions needed.
- If a reasonable assumption is safe, state it and move forward.

## When to use this skill
Use this skill when the request is:
- vague
- incomplete
- overloaded with multiple possible tasks
- missing success criteria
- missing scope boundaries
- high-cost if interpreted incorrectly
- likely to trigger unnecessary rework if you guess wrong

## When not to use this skill
Skip refinement when:
- the request is already clear and specific
- the user gave explicit files, features, or outputs
- the task is low-risk and a reasonable assumption is faster
- the current thread already established the needed context

## Workflow

### 1. Diagnose the prompt
Briefly identify:
- main objective
- likely scope
- what is still unclear
- what assumption would be risky

Keep this short.

### 2. Choose one of two paths

#### Path A: Clarify
Use this path only if ambiguity is material.

Ask 1 concise question by default.
Ask 2 only if truly necessary.
Do not ask a batch of broad questions unless the task is genuinely complex.

Good clarification questions:
- Which output matters most here?
- Should I treat this as a quick fix or a fuller rebuild?
- What does done look like for you?
- Which of these areas should I focus on first?

#### Path B: State assumptions and proceed
Use this when a reasonable assumption is low-risk.

Format:
- Assumption: [short statement]
- Proceeding with: [short statement]

Then continue.

### 3. Convert the rough ask into an execution-ready brief
When useful, restate the task in a tighter form:
- goal
- context
- constraints
- output format
- assumptions

Keep it practical, not formal.

### 4. Proceed
Once the task is clear enough, execute.

## Output shape
When refinement is needed, prefer this structure:

### What I think you want
- [core goal]
- [scope]

### What is still unclear
- [key ambiguity only]

### Proposed path
- [question or assumption]

Then either ask the concise question or proceed with the assumption.

## Core rules
- Prefer speed with clarity, not process for its own sake
- Ask fewer questions, not more
- Do not ask for information the repo, docs, or thread already contain
- Do not ask about choices the assistant can safely make
- Do not block work unless ambiguity is meaningful
- If the request is broad, help narrow it into the next practical step

## Good prompts this skill should handle
- fix the form
- make this page better
- help me with this project
- improve the dashboard
- make this production ready
- I want to add AI stuff to this app
- can you clean this up

## Example

User prompt:
- help me improve the dashboard

Good refinement:

### What I think you want
- Improve the dashboard in a meaningful way
- Likely scope is either metrics, layout, filters, or usability

### What is still unclear
- Which improvement matters most right now

### Proposed path
- Which should I focus on first: metrics, layout, filters, or workflow?

If the user does not answer and one assumption is safe:
- Assumption: the highest-value improvement is the dashboard metrics and filters
- Proceeding with: a review of those areas first

---

Remember: the goal is not better questions. The goal is faster correct execution.
