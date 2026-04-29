# Security review workflow

Use this workflow when the goal is to pressure-test an app, feature, or deployment for practical security basics.

## Main question
Security review is mostly about four things:
- what is trusted
- what should not be trusted
- what access exists
- how bad failure would be

## Step 1: Define the surface
Start by stating:
- what feature, flow, or system is being reviewed
- who uses it
- what actions it allows
- what data it touches

Good examples:
- Firebase-authenticated dashboard route
- CSV import flow for brokerage data
- Firestore-backed admin page
- internal planning tool with file uploads

## Step 2: Identify trust boundaries
Ask:
- where does untrusted input enter?
- what parts are only client-side?
- what parts are enforced server-side or database-side?
- what assumptions is the app making about the user, request, or environment?

Typical untrusted inputs:
- form fields
- query parameters
- uploaded files
- API requests
- local storage values
- anything sent from the browser

## Step 3: Identify sensitive assets
Look for:
- user data
- internal operational data
- admin capabilities
- service accounts
- API keys
- access tokens
- private environment variables
- payment or notification credentials

## Step 4: Review authentication and authorization separately
Authentication asks:
- who is this?

Authorization asks:
- what are they allowed to do?

Common failure patterns:
- route checks login but not ownership
- frontend hides buttons but backend still allows the action
- Firestore rules are broader than intended
- service account has more access than the feature needs

## Step 5: Review input handling
Ask:
- what validation exists?
- what happens if input is blank, malformed, oversized, duplicated, or manipulated?
- could input trigger unexpected queries, writes, or output changes?
- could imports overwrite, leak, or misclassify data?

## Step 6: Review secrets handling
Check:
- are secrets in environment variables instead of source code?
- are service accounts or tokens exposed in repo, logs, screenshots, or prompts?
- are client-side values being mistaken for secrets?
- is secret rotation possible if needed?

## Step 7: Review blast radius
Ask:
- if this control fails, what is exposed?
- one page?
- one user?
- all users?
- all data?
- deploy credentials?

Prefer fixes that shrink blast radius fast.

## Risk priorities
### Highest-priority things to review first
- broken authorization
- exposed secrets
- overly broad Firestore or database rules
- admin or privileged routes
- file uploads and imports
- anything multi-user
- anything public-facing

### Medium-priority things
- internal dashboards
- non-sensitive forms
- operational tools with limited scope

### Lower-priority things
- static pages
- purely cosmetic UI changes

## Minimum output
For a useful security pass, always include:
- what was reviewed
- the main trust boundary
- the top 3 risks
- the smallest practical fixes
- what still needs deeper review

## Good review questions
- What is the real trust boundary here?
- What input is being trusted too much?
- Is this enforced by the backend or only by the UI?
- If this leaked or failed, how bad would it be?
- What is the smallest fix that would materially reduce risk?
