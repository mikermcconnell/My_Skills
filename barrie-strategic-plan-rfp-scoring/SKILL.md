---
name: barrie-strategic-plan-rfp-scoring
description: Score FIN2026-064P Barrie Transit Strategic Plan RFP submissions. Use when reviewing Barrie Transit Strategic Plan proponent folders, running the full-vendor scoring loop, inventorying section PDFs, drafting Section F evaluator worksheet comments, assigning suggested 1-10 scores, or checking obvious issues before scoring.
---

# Barrie Strategic Plan RFP Scoring

Score FIN2026-064P Barrie Transit Strategic Plan submissions against Section F only.

This is a project-specific skill. Use it instead of the generic `rfp-scoring` skill for this RFP.

## Use these references

Read only what is needed, but always read the relevant reference before scoring:
- `references/submission-file-process.md` for folder setup and file inventory steps
- `references/workbook-row-map.md` for exact worksheet rows and output cells
- `references/section-f-scoring-guide.md` for each rated criterion
- `references/appendix-d-scope-summary.md` for the scope of work
- `references/addenda-summary.md` for changes that affect scoring

When writing for Mike, read the `personal_context` MCP resources if available:
- `portfolio://communication-style`
- `portfolio://preferences-and-constraints`

## Default scope

Unless Mike asks otherwise:
- Score Section F technical criteria only.
- Use Appendix D / Section A as the scope reference.
- Score one proponent at a time.
- Score each proponent independently.
- Do not compare proponents.
- Do not review pricing.
- Do not calculate weighted points, section totals, technical totals, or award rankings.
- Do not edit the Excel workbook.
- Provide suggested scores only. Mike makes the final evaluator decision.
- Ask before saving scoring notes to Markdown.

## Standard workflow

For each proponent:
1. Run the file inventory first.
2. Match available PDFs to F.1 to F.5.
3. Flag missing or unclear files before scoring.
4. Open/review the Excel evaluation worksheet criteria for the exact row being scored.
5. Use the Excel row criteria as the basis for the response and suggested score.
6. Review the matching reference guide only as support; do not let the reference guide replace the workbook wording.
7. Review the relevant submission evidence against the Excel criteria.
8. Score the exact worksheet rows.
9. Draft paste-ready comments and suggested 1-10 scores.
10. Add an `Obvious flags` section only if something material is noticed.

## Full-vendor scoring loop

Use this faster loop for the remaining vendors unless Mike asks for one row at a time:

1. Inventory the proponent folder.
2. Confirm the PDFs map to F.1 through F.5.
3. Review the Excel criteria before scoring each worksheet row.
4. Score all 9 worksheet rows.
5. Provide output in this order:
   - Score table
   - Review flags
   - Paste-ready worksheet comments
   - QC check
6. Do not stop for minor gaps. Score the row and list the gap under Improvement or Review flags.
7. Only stop or ask Mike when the issue could materially change the score or make scoring unfair.

### Score table format

Use a short table before the full comments:

| Row | Suggested score | Main rationale |
|---|---:|---|
| F.1 Company Overview | X/10 | ... |

Keep the rationale short. Do not include weighted points or totals.

### Review flags

Include only material items:
- Missing section evidence.
- Weak support for a score.
- Project Manager or Senior Transit Planner not shown on F.3 references.
- F.5 schedule or timing issues.
- Actual pricing, rates, or dollar amounts shown.
- Anything that needs Mike's decision.

If there are no material flags, write:

```text
Review flags:
- No material flags noted.
```

### QC check

End every full-vendor review with:

```text
QC check:
- All 9 rows scored.
- No totals calculated.
- No pricing review included.
- No proponent comparison included.
- Comments are concise and Excel-ready.
```

Only adjust the QC check if one of those items is not true.

Workbook criteria rule:
- Always review the Excel evaluation criteria before responding.
- Base the score and comments on the Excel criteria for that row.
- If the reference guide and workbook differ, follow the workbook and note the difference if it affects scoring.
- Do not score from memory or from the proposal narrative alone.

For F.1 Company Overview:
- Review the F.1 Excel criteria first every time.
- Check all requested company overview items: years in business, staff/resources, services, office locations, transit capability, subconsultants, legal relationship, services, and percentage involvement.
- Do not give credit for a subconsultant meeting F.1 unless the F.1 criteria are actually addressed for that subconsultant.
- Do not use general proposal strength to fill missing F.1 information.

Use this helper when a proponent folder is available:

```powershell
python "C:\Users\Mike McConnell\Documents\my-skills\barrie-strategic-plan-rfp-scoring\scripts\inventory_submission.py" "<proponent-folder>"
```

The helper lists PDFs, suggests section matches, flags missing/unclear sections, and prints short previews. It does not edit or create scoring files.

## Exact rows to score

Score these worksheet rows:
- F.1 Company Overview
- F.2a Project Team Overview
- F.2b Project Manager
- F.2c Senior Transit Planner
- F.2d Additional Team Members
- F.3a Project Reference 1
- F.3b Project Reference 2
- F.4 Project Understanding and Approach
- F.5 Work Plan and Schedule

Do not score only the parent rows unless Mike asks.

## Rating scale

Use this scale exactly:
- 0-1 = Unsatisfactory / no acceptable response
- 2-3 = Poor / response is minimal
- 4-5 = Weak / partially meets requirements
- 6-7 = Good / meets minimum requirements
- 8-9 = Very Good / exceeds minimum requirements
- 10 = Excellent / exceeds minimum requirements in multiple areas

## Score band rules

- Use the lower score in a band when evidence is thin, vague, or only partly supported.
- Use the higher score in a band when evidence is clear, specific, and well supported.
- Minimum-only responses normally stay at 6-7.
- Use 8-9 only when the submission clearly goes beyond the minimum requirements.
- Use 9 more often than 10 for strong rows.
- Use 10 only when the response is clearly exceptional and exceeds requirements in multiple clear areas.
- Small gaps should be noted, but do not automatically lower the score if they do not affect delivery risk or the evaluation criteria.
- Missing or unclear evidence is a gap. Do not infer.
- Firm reputation is not evidence unless the submission connects it to this project.

## Output format

Use this format for each scored row:

```text
F.2b Project Manager
Suggested score: X/10

Minimum:
- ...

Preference:
- ...

Improvement:
- ...
```

Keep each row concise:
- Minimum: 2-3 bullets max.
- Preference: 2-3 bullets max.
- Improvement: 1-2 bullets max.
- Obvious flags: 1-2 bullets max, only if material.
- Use fewer bullets if the score rationale is clear.
- Do not list every supporting fact. Pick the key score-driving points.
- Combine related points into one bullet where practical.
- If the criterion is clearly met through a CV or required document, a short note is enough. Do not restate every detail.

For F.3 rows, include the project name if known:

```text
F.3a Project Reference 1
Suggested score: X/10

Client/Project Name:
- ...

Minimum:
- ...

Preference:
- ...

Improvement:
- ...
```

For F.3 rows:
- Always check whether the proposed Project Manager and/or Senior Transit Planner worked on the reference project.
- Mention this by name in the comments.
- Treat PM/Senior Transit Planner participation as support for a higher preference score.
- Do not make it a minimum requirement. Minimum is still at least one proposed team member participated.
- If PM/Senior Transit Planner involvement is not shown, list it as an improvement only when it affects the score.

If needed, add a short section after the scored rows:

```text
Obvious flags:
- ...
```

Only include obvious flags when there are material gaps, risks, or unclear items. Examples: missing files, pricing shown in the uncosted matrix, missing project dates, or contradictory information.

When scoring a full vendor, use `Review flags` instead of `Obvious flags`.

## Comment style

Write like Mike's evaluator notes:
- Point form.
- Short and practical.
- Concise. Fewer bullets are better.
- Plain language.
- Direct wording.
- Working-note style is okay. Short fragments are okay.
- Do not over-polish the wording.
- No long paragraphs.
- No filler.
- No AI-sounding summary language.
- No consultant-style wording.
- Do not intentionally add spelling mistakes or typos.
- Use specific evidence from the submission.
- Mention project names, dates, roles, values, percentages, or years of experience only when they affect the score.
- Keep comments suitable for paste-in to the workbook.
- Focus on the best evidence, the main gap, and why the score lands where it does.

Avoid:
- robust
- innovative
- comprehensive
- cutting-edge
- leverage
- demonstrates a deep understanding
- uniquely positioned
- best-in-class
- it may be advisable

Prefer:
- Shows...
- Provides...
- Identifies...
- Includes...
- Does not show...
- Missing...
- Unclear whether...

## Calibration rule

Before scoring all proponents, score one full proponent first as calibration. After Mike reviews the first output, keep the same evidence standard and wording style for the rest.

Arcadis is the calibration anchor:
- Strong rows usually score 9, not 10.
- Small gaps are noted but do not automatically lower the score.
- Use 10 only for clearly exceptional responses.
- Keep comments shorter than the first draft.

## Mike calibration notes

Use these style and scoring lessons from Mike's edits:


### Workbook calibration from Mike edits

Use Mike's edited Arcadis and Dillon workbook notes as the current tone/score anchor:
- Keep comments shorter than the draft markdown. One or two useful bullets per heading is usually enough.
- `Meets minimum` is acceptable where the CV or required document covers the minimum. Do not restate every detail.
- Do not over-credit firm size/history in F.1. If the company overview does not clearly tie resources or subconsultants to this scope, 6-7 may be more appropriate.
- For F.1, give preference credit for project-scope fit, not just general firm experience.
- For F.2a, score 9 only when team structure, roles, and previous work together are clear. Use 8 where one of those is only partly supported.
- For F.2b and F.2c, strong experience can still land at 8 if a designation, Council/contracted-operations link, or detailed example is missing.
- For F.2d, coverage of the required areas meets minimum. Use 9 only where added team depth clearly exceeds the scope in multiple areas.
- For F.3, keep the project name short and focus on whether the PM and/or Senior Transit Planner participated.
- For F.5, do not treat hours as pricing. Only flag costs if rates or dollar values are shown.
- Natural evaluator-note wording is okay. Do not over-polish.


### KPMG workbook calibration from Mike edits

Use Mike's edited KPMG tab to tighten the review standard:
- F.4 needs the `how`, not just a list of tasks. If the approach only identifies scope items but does not explain how the work will be done, a 4-5 may be appropriate.
- Incorrect local context matters. If a proposal gets a known Barrie project or phase wrong, list it as a real gap.
- F.5 sequencing matters. Vision/values/targets should come before service plan development, and late Council engagement can create re-work risk.
- A partially complete F.5 response with poor sequencing can be a 5 even if a schedule exists.
- F.2d can drop to 5 when the added team does not cover key scope areas well enough, even if basic strategy/fare support is present.
- F.3 references should be scored down where they are not similar transit strategic/master plans for a comparable municipality, even when the PM participated.
- Keep Mike's natural evaluator-note style, but do not intentionally add typos.

### F.2b Project Manager

- For Minimum, keep it very short if the CV covers the minimum requirements. Example: `Meets minimum when referencing CV`.
- For Preference, focus on the main score-driving items:
  - years above the 5-year requirement
  - public sector transit leadership from the strongest reference project
  - Council approval or advisory committee experience
- For Improvement, focus on the main gaps:
  - reference project not within the past 5 years
  - PMP/RPP/P.Eng. or similar designation would have been an asset
- Do not over-explain project management experience if the CV already establishes it.

### F.3 Project References

- For Minimum, confirm at least one proposed team member participated.
- For Preference, give added credit when the proposed Project Manager and/or Senior Transit Planner participated in the reference project.
- Mention the specific name and role. Example: `Senior Transit Planner Jeremy Cohen was Transit Planning Lead on this project.`
- If only additional team members participated, say that plainly and do not overstate continuity with the proposed key roles.

### F.4 Project Understanding and Approach

- For Minimum, keep the first bullets focused on whether the scope and delivery model are clearly covered:
  - Barrie's 2027-2032 plan
  - fixed route, ToD, and Specialized Transit
  - Staff-led, Joint, and Consultant-led model
  - main work streams from Appendix D
- For Preference, focus on the best score-driving items:
  - collaborative network design or shared scope approach
  - local Barrie research or local partner understanding
  - how the proponent will collaborate with City staff, including tools like SharePoint if useful
  - risks that are applicable to Barrie, even if a bit general
  - specific value add, such as Remix or other tools, only where it is tied to the work
- It is okay for F.4 preference comments to sound like evaluator notes, such as `I like the collaborative nature of network design...`
- Do not overstate "innovation". Say `Value add is...` or `Adds value through...`
- If there is no clear gap, leave Improvement blank or say `No major gap noted for this row.`

### F.5 Work Plan and Schedule

- For Minimum, focus on whether the work plan covers all chapters, follows the Staff-led/Joint/Consultant-led structure, and aligns with the July 2026 to August 2027 schedule.
- Treat a time-task matrix with named staff hours by task as meeting the matrix requirement when it is clear and shows the split between firms, such as Arcadis and Access Planning.
- Do not flag costs unless actual pricing, rates, or dollar amounts are clearly shown. Do not treat hour totals or firm-level hour splits as costs.
- Give preference credit for:
  - clear milestones, review periods, meetings, engagement periods, and dependencies
  - logical sequencing and work that can be done in parallel
  - regular City check-ins and review periods
  - realistic timing for network development, peer interviews, and internal workshops
- It is okay to say why the timing matters. Example: `I like how a full month is provided for network development.`
- For Improvement, identify timing issues that may affect delivery. Example: `Council engagement is in the middle of fleet/infrastructure/technology planning.`
- Arcadis F.5 calibration: 9/10 where the schedule is clear, the matrix is hours-based, sequencing is logical, and only minor timing concerns are noted.
