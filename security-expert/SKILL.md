---
name: security-expert
description: Practical security review workflow for software repositories, internal tools, Firebase apps, dashboards, imports, auth flows, and operational systems. Use when the user wants to walk through trust boundaries, secrets, permissions, input handling, data exposure, or blast radius in a practical, repeatable way.
---

# Security Expert

Use this skill to walk through security in a practical way.

This skill is for real app and tool work where the goal is not abstract security theory, but deciding what is trusted, what is exposed, and what needs to be protected before a feature or system is relied on.

## Read only what you need
- `references/security-review-workflow.md` for the standard workflow, review questions, and priority areas
- Use repo docs such as `AGENTS.md`, `AGENTS.md`, `ORCHESTRATOR.md`, deployment notes, auth docs, or environment docs when they exist

## When to use this skill
Use this skill when:
- reviewing an app, feature, route, API, auth flow, import flow, or deployment for security basics
- checking how authentication and authorization are enforced
- reviewing Firebase, Firestore, tokens, service accounts, or other secrets handling
- deciding what input is trusted and where the real trust boundary is
- checking whether an internal tool is still exposing more access than it should
- reviewing blast radius before release or before sharing a tool more broadly

## Workflow

1. Define the surface
- What system, feature, or flow are we reviewing?
- What data, actions, or users matter here?
- Is this public-facing, internal-only, admin-only, or multi-user?

2. Identify trust boundaries and sensitive assets
- What is trusted?
- What is untrusted?
- What secrets, sensitive data, privileged actions, or critical systems are involved?

3. Review access control
- How is authentication handled?
- How is authorization handled?
- Can users or clients access more than they should?
- Is the backend or database enforcing the rule, or only the frontend?

4. Review input and data handling
- What external input enters this flow?
- What validation, filtering, or allowlisting exists?
- Could malformed, missing, or manipulated input change behavior or expose data?

5. Review secrets and exposure paths
- Where are keys, tokens, service accounts, and config values stored?
- Are secrets kept out of code, logs, client-visible surfaces, and screenshots?
- What would happen if one leaked?

6. Review blast radius and practical fixes
- If something fails here, how bad is it?
- What is the smallest effective fix that reduces the risk materially?
- What still remains risky after the fix?

## Core rules
- Do not trust client behavior by default
- Treat authentication and authorization as separate checks
- Treat all external input as untrusted
- Keep secrets out of repos, logs, prompts, and client-visible surfaces
- Prefer backend and database enforcement over UI-only restrictions
- Focus on realistic risk and blast radius, not security theatre
- If a flow matters operationally, clearly say what still needs review before trust

## Output format
When useful, structure your security output like this:
- Surface being reviewed
- Sensitive assets and trust boundaries
- Main security risks
- Most likely failure or abuse paths
- Smallest practical fixes
- Residual risk
- Recommended next review step

## Good prompts this skill should handle
- Walk me through the security risks in this Firebase app
- Review this feature for auth, secrets, and trust-boundary problems
- What could go wrong if this internal tool is shared more broadly?
- Help me think through security before I release this import flow
- Is this route protected by real authorization or just UI hiding?
