---
name: devops-automator
description: Improve CI/CD, deployments, environment setup, infrastructure automation, and operational workflows. Use when the task involves pipelines, release safety, deployment scripts, runtime configuration, observability wiring, or reducing manual operational work.
---

# DevOps Automator

Use this skill to remove operational drag and make delivery safer.

## Workflow

1. Map the current delivery path: build, test, package, deploy, verify, rollback.
2. Find the manual steps, hidden dependencies, and failure-prone handoffs.
3. Automate the highest-value path first rather than redesigning everything.
4. Add checks that prevent bad releases: smoke tests, health checks, gated deploys, rollback hooks.
5. Keep environments reproducible and configuration explicit.

## Priorities

- Optimize for repeatability and safe recovery.
- Keep CI/CD simple enough that the team can debug it.
- Separate build-time and runtime configuration clearly.
- Prefer incremental rollout and rollback support over all-at-once deploys.
- Include monitoring or verification in the deployment loop.

## Good Outputs

- Cleaner pipeline structure.
- Automated setup for local, staging, or production environments.
- Deployment scripts with verification and rollback steps.
- Practical infra-as-code or environment-management improvements.

## Combine With Other Skills

- Use `site-reliability-engineer` when the main problem is reliability rather than automation.
- Use `security-engineer` when pipeline or infrastructure changes affect secrets, access, or exposure.
- Use `system-design-expert` when delivery problems trace back to system boundaries or service shape.
