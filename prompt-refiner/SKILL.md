---
name: prompt-refiner
description: Improves rough prompts by asking clarifying questions and enhancing clarity. Use when the user provides a vague, incomplete, or ambiguous request that needs refinement before execution.
---

# Prompt Refiner Skill

When you receive a rough, vague, or incomplete prompt, follow this workflow before executing:

## Step 1: Analyze the Prompt

Before doing anything, evaluate the user's request:
- Is the core request clear and specific?
- What information is missing or assumed?
- Are there multiple ways to interpret this?
- What could go wrong if you assume incorrectly?

Output a brief analysis:
```
### What I understand:
- Main objective: [identify the core goal]
- Scope: [small fix / feature / refactor / exploration]
- Target: [files, components, or areas involved]

### What's unclear or missing:
- [List any ambiguities]
- [List missing context]
- [List assumptions I'd have to make]
```

## Step 2: Ask Clarifying Questions via Form

**IMPORTANT:** Use the `AskUserQuestion` tool to ask clarifying questions as interactive forms. This provides a better UX than text-based questions.

Structure your questions around these categories:

1. **Goal/Objective**: What's the primary objective? What does success look like?
2. **Scope**: Is this a quick fix or a comprehensive solution?
3. **Approach**: Which implementation approach to take?
4. **Constraints**: Any limitations, preferences, or existing patterns to follow?

### Example AskUserQuestion Usage:

For a vague prompt like "fix the form", use:

```
AskUserQuestion with questions:
[
  {
    "question": "Which form needs to be fixed?",
    "header": "Target",
    "options": [
      { "label": "Login form", "description": "User authentication form" },
      { "label": "Signup form", "description": "New user registration" },
      { "label": "Settings form", "description": "User preferences" },
      { "label": "Contact form", "description": "Contact/feedback form" }
    ],
    "multiSelect": false
  },
  {
    "question": "What type of issue are you experiencing?",
    "header": "Issue Type",
    "options": [
      { "label": "Validation", "description": "Input validation not working correctly" },
      { "label": "Submission", "description": "Form doesn't submit or errors on submit" },
      { "label": "Display/Layout", "description": "Visual or styling issues" },
      { "label": "Performance", "description": "Form is slow or unresponsive" }
    ],
    "multiSelect": true
  }
]
```

### Guidelines for Form Questions:

- Ask 1-4 questions maximum (tool limit is 4)
- Each question should have 2-4 options
- Use clear, concise labels (1-5 words)
- Add descriptions to explain each option
- Use `multiSelect: true` when multiple answers could apply
- Put recommended option first with "(Recommended)" suffix
- Users can always select "Other" for custom input

## Step 3: Summarize Understanding

After receiving answers, briefly restate:
- What you understand the task to be
- How you plan to approach it
- Any assumptions you're making

Ask for final confirmation: "Does this match what you had in mind? Should I proceed?"

## Step 4: Execute with Improved Clarity

Once confirmed, proceed with the refined understanding.

## When to Apply This Skill

Apply this workflow when prompts contain:
- Vague terms like "fix this", "make it better", "clean up"
- Missing context about which files/features
- Ambiguous scope ("update the UI", "improve performance")
- Multiple possible interpretations
- Technical decisions that need user input

## When NOT to Apply

Skip refinement for:
- Specific, clear requests ("Add a loading spinner to the Login button")
- Simple questions ("What does this function do?")
- Explicit file/line references
- Follow-up tasks where context is already established
- Requests where you can make reasonable defaults

## Full Example

**Vague prompt**: "Add production website stuff"

**Step 1 - Analysis**:
```
### What I understand:
- Main objective: Add production-ready web assets
- Scope: Configuration and metadata setup
- Target: index.html, manifest, favicons

### What's unclear:
- Branding assets available?
- PWA requirements?
- Production URL?
```

**Step 2 - Form Questions** (use AskUserQuestion tool):
```json
{
  "questions": [
    {
      "question": "What branding assets should I use for favicons?",
      "header": "Branding",
      "options": [
        { "label": "Use existing logo", "description": "I have logo files to provide" },
        { "label": "Generate from colors", "description": "Create simple icon using brand colors" },
        { "label": "Placeholder for now", "description": "Use generic placeholder icons" }
      ],
      "multiSelect": false
    },
    {
      "question": "Should this be a Progressive Web App (PWA)?",
      "header": "PWA",
      "options": [
        { "label": "Yes, full PWA", "description": "Installable with offline support" },
        { "label": "Basic manifest only", "description": "Add to homescreen but no offline" },
        { "label": "No PWA features", "description": "Standard web app only" }
      ],
      "multiSelect": false
    }
  ]
}
```

**Step 3 - Confirmation**: "Based on your answers, I'll add favicons using brand colors and set up a basic manifest without offline support. Proceed?"

**Step 4 - Execute**: Implement with clear understanding.

---

Remember: A few seconds of clarification saves minutes of rework. Use forms for a better user experience.
