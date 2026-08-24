# Submission File Process

Use this process before scoring any proponent.

## Expected folder setup

Each proponent should have its own folder, for example:

```text
Submissions/
- Arcadis/
  - Company Overview.pdf
  - Project Team Qualifications and Experience.pdf
  - Relevant Project Experience.pdf
  - Project Understanding and Approach.pdf
  - Work Plan and Schedule.pdf
- Dillon/
- KPMG/
```

File names do not need to be exact, but they should make the section clear.

## Inventory first

Before scoring:
1. Run the inventory helper on the proponent folder.
2. Confirm which PDF maps to each Section F area.
3. Flag missing or unclear files.
4. Only start scoring once the file map is clear enough.

Helper command:

```powershell
python "C:\Users\Mike McConnell\Documents\my-skills\barrie-strategic-plan-rfp-scoring\scripts\inventory_submission.py" "<proponent-folder>"
```

## Expected file mapping

| RFP area | Likely file content |
|---|---|
| F.1 | Company overview, firm profile, office locations, subconsultants |
| F.2 | Project team, org chart, PM CV, Senior Transit Planner CV, other team CVs |
| F.3 | Relevant project experience, project references, client references |
| F.4 | Project understanding, approach, methodology, risk, QA/QC |
| F.5 | Work plan, Gantt chart, schedule, uncosted time task matrix |

## Missing or unclear files

If a file is missing:
- Do not infer the evidence from other sections unless the same evidence is clearly included elsewhere.
- Say which worksheet rows may be affected.
- Ask Mike for the missing file if scoring cannot be completed fairly.

If a file could map to more than one section:
- State the likely mapping.
- Use the PDF text preview to confirm.
- Ask for confirmation only if the mapping is still unclear.

## Obvious flags to watch for

Flag these separately from the Section F scoring comments:
- Missing section PDF.
- File appears to be the wrong section.
- Pricing, hourly rates, or costs shown in the uncosted time task matrix.
- Missing project dates in F.3.
- Project reference is older than five years without a clear reason.
- Unclear completion status for an underway project.
- Contradictory team roles, dates, or availability.
- More than 15% of hours assigned to unnamed resources in F.5.

Do not turn obvious flags into a compliance review unless Mike asks.
