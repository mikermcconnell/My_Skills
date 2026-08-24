---
name: skill-creator
description: Create new skills, improve existing skills, and evaluate how well a skill works. Use when the user wants to turn a workflow into a skill, edit or optimize a SKILL.md, define trigger wording, design test prompts, compare iterations, or package a reusable skill for future use.
---

# Skill Creator

Help the user create or improve a skill in a practical loop:
1. understand the intended behavior
2. write or revise the skill
3. test it on realistic prompts
4. review results with the user
5. improve it and repeat

Be flexible. Some users want a rigorous evaluation loop. Others just want help drafting a good skill quickly.

## Communicate clearly

Match the user's level of technical comfort.
- "evaluation" and "benchmark" are usually fine.
- Explain terms like JSON or assertions if the user may not know them.
- Prefer plain language over jargon unless the user clearly wants technical detail.

## Core job

Figure out where the user is in the skill-building process and help them move forward.

Common starting points:
- "I want to make a skill for X"
- "Turn this workflow into a skill"
- "Improve this existing SKILL.md"
- "Can you test whether this skill is actually better?"
- "Can you make this trigger more reliably?"

## Step 1: Capture intent

Start by pinning down the essentials.
1. What should the skill enable the model to do?
2. When should it trigger?
3. What should the output look like?
4. Should it include formal testing, or is a lighter drafting pass enough?

If the conversation already contains examples, extract them before asking new questions.
Do not ask a huge batch of questions at once. Ask only what is needed next.

## Step 2: Plan the skill contents

Translate the use cases into the skill structure.

Possible contents:
- `SKILL.md` for the core instructions
- `scripts/` for repeatable deterministic work
- `references/` for detailed docs or schemas the model should read only when needed
- `assets/` for templates or files used in outputs

Only add resources that clearly help future runs. Do not add filler files.

## Step 3: Write or revise the skill

When drafting the skill:
- keep the frontmatter strong; the description is the main trigger mechanism
- include both what the skill does and when it should be used
- make the trigger wording a little "pushy" so the skill does not under-trigger
- keep the body focused on workflow, decision rules, and useful examples
- explain why instructions matter instead of relying on rigid commands where possible
- keep the file lean; move heavy detail into references only when needed

### Skill structure

Each skill should normally include:
- `name`
- `description`
- a concise body with clear instructions

Use imperative wording.
Prefer realistic examples over abstract theory.

## Step 4: Create test prompts

After drafting the skill, create 2-3 realistic prompts that a real user would actually say.
Show them to the user for approval when practical.

Use prompts that are concrete and a little messy, not sterile toy examples.
Good prompts help reveal whether the skill actually generalizes.

If you are storing eval prompts, use an `evals/evals.json` file like this:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User task prompt",
      "expected_output": "What success looks like",
      "files": []
    }
  ]
}
```

## Step 5: Run the evaluation loop

If the environment supports subagents, prefer this loop:
1. run each prompt with the skill
2. run the same prompt without the skill, or against the old version when improving an existing skill
3. save outputs in a workspace next to the skill folder
4. draft assertions while runs are in progress
5. grade results
6. review outputs and metrics with the user
7. improve the skill and rerun

Use a sibling workspace named like `<skill-name>-workspace/`.
Within it, organize by iteration and by eval.

### Evaluation rules

- Launch with-skill and baseline runs together when possible.
- Give each eval a descriptive name, not just a number.
- Capture timing and token data when the environment exposes it.
- Prefer programmatic checks for objective assertions.
- For subjective skills, rely more on human review than forced metrics.

If the environment includes viewer or benchmark tooling, use it instead of inventing a custom review format.
If it does not, present outputs directly in the conversation and ask for feedback inline.

## Step 6: Improve intelligently

When revising a skill, do not overfit to one example.
Generalize from feedback.

Look for these signals:
- repeated failure patterns across prompts
- instructions that are too vague
- instructions that are too rigid or bloated
- repeated helper code that should become a bundled script
- non-discriminating assertions that always pass
- high-variance results that suggest a flaky eval

Explain the why behind changes. Remove instructions that are not pulling their weight.

## Description optimization

After the skill works reasonably well, offer to improve the description so it triggers more reliably.

Create a realistic mix of should-trigger and should-not-trigger prompts.
Focus especially on near-misses, not obviously unrelated negatives.
The goal is to improve trigger accuracy without making the skill fire on everything.

When optimizing descriptions:
- use realistic user phrasing
- include some ambiguity and messy wording
- test adjacent cases where another skill might win
- choose the best description based on held-out performance, not just the training set

## Environment guidance

### If subagents are available

Use them for independent forward-testing.
Do not leak the answer, intended fix, or your private diagnosis into the test prompt.
Pass the skill and the user-like task only.

### If subagents are not available

Run the test prompts yourself, one at a time.
Skip baseline comparisons if they are not practical.
Show the user outputs directly and ask what to improve.

### If browser review tools are unavailable

Use a static review file if available.
Otherwise keep the review loop in chat and save outputs to disk when the user needs to inspect files.

## Packaging

If packaging support exists, package the finished skill and give the user the final file path.
If not, leave the skill as a normal folder with a valid `SKILL.md`.

## Quality bar

A good finished skill:
- has clear trigger wording
- is concise enough to be practical
- includes only genuinely useful resources
- has been tried on realistic prompts
- has been revised based on actual results, not guesswork

## Default behavior

If the user is vague, guide them through: intent -> draft -> test prompts -> review -> improve.
If the user already has a draft, skip straight to evaluation and revision.
If the user says they just want to vibe, keep the loop light and collaborative.
