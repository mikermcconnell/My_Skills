---
name: incident-response-commander
description: Structure active incidents and post-incident follow-up with severity assessment, role assignment, timeline building, stakeholder updates, and blameless post-mortems. Use when the user is dealing with a production issue, outage, degraded service, SEV assessment, incident comms, runbook gaps, on-call process design, or needs a clean incident report.
---

# Incident Response Commander

Use this skill when the system is already failing or when incident readiness needs to be improved.

## Active Incident Workflow

1. Classify severity.
   Identify:
   - customer impact
   - scope
   - data risk
   - workaround availability
   - time sensitivity

2. Establish structure immediately.
   Assign or simulate:
   - incident commander
   - technical lead
   - communications owner
   - scribe

3. Build a live timeline.
   Record:
   - detection time
   - symptoms
   - actions taken
   - hypotheses
   - what changed
   - current status

4. Timebox investigations.
   Push toward explicit hypotheses and pivots instead of unstructured guessing.

5. Keep communication on a fixed cadence.
   Even "no change, still investigating" is better than silence during a real incident.

## Post-Incident Workflow

1. Write a factual timeline first.
2. Separate impact, trigger, contributing factors, and systemic causes.
3. Keep the language blameless.
4. Convert lessons into owned follow-up actions.
5. Flag which actions are prevention, detection, response, or recovery improvements.

## Rules

- Never skip severity framing.
- Never mix active diagnosis notes with post-mortem conclusions.
- Prefer system causes over person-blame language.
- Require owners and due dates for follow-up actions.
- Call out missing runbooks, dashboards, or ownership boundaries when they slowed response.

## Output Shapes

- Incident bridge structure:
  - severity
  - impact
  - current hypothesis
  - next 2-3 actions
  - comms cadence

- Status update:
  - what users are seeing
  - what is known
  - what is being done now
  - next update time

- Post-mortem:
  - summary
  - impact
  - timeline
  - root/contributing/systemic causes
  - action items

## Checklist

- Who is affected?
- What is the current severity and why?
- What changed most recently?
- What is the next decisive action?
- What missing guardrail would have shortened this incident?
