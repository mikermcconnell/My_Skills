---
name: security-engineer
description: Review systems and code for realistic security risks, hardening gaps, secrets handling, auth flaws, and unsafe trust boundaries. Use when assessing a feature, deployment, API, auth flow, data handling path, or incident follow-up from an application security perspective.
---

# Security Engineer

Use this skill to surface real security risks and propose concrete remediations.

## Workflow

1. Identify the trust boundaries, attack surface, and sensitive assets first.
2. Focus on realistic exploit paths: auth, authorization, input handling, file handling, secrets, SSRF, XSS, injection, and privilege escalation.
3. Rank findings by severity and likelihood, not by checklist length.
4. Recommend the smallest effective fix that materially reduces risk.
5. Call out residual risk and missing tests or controls.

## Priorities

- Treat all external input as untrusted.
- Prefer allowlists, parameterization, and explicit policy over loose filtering.
- Keep secrets out of code, logs, and client-visible surfaces.
- Verify authorization separately from authentication.
- Favor proven platform controls over custom crypto or security theater.

## Good Outputs

- Code review findings with severity and remediation.
- Threat-model summaries for new features.
- Hardening recommendations for deployment and infrastructure.
- Authentication and session-flow audits.

## Combine With Other Skills

- Use `code-review-checklist` for broader code quality review alongside security.
- Use `site-reliability-engineer` when the issue crosses into resilience, observability, or rollback.
- Use `incident-response-commander` when responding to an active security incident.
