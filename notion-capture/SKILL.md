---
name: notion-capture
description: Capture meeting notes, project ideas, or task lists and create structured entries in Notion. Use when the user wants to turn rough notes into Notion tasks or projects.
---

# Notion Quick Capture

Capture meeting notes, project ideas, or task lists and create structured entries in Notion.

## Trigger
User invokes `/notion-capture` followed by meeting notes, project description, or task list.

## Workflow

1. **Parse the input** to identify:
   - Project name (if creating a new project)
   - Individual tasks/action items
   - Due dates (look for "by [date]", "next week", "end of month", etc.)
   - Priority signals ("urgent", "high priority", "when you get a chance" = low)
   - Assignees (names mentioned)
   - Context clues for Tags (work-related = Work, personal = Personal)

2. **Ask clarifying questions** if needed:
   - Is this a new project or tasks for an existing project?
   - What priority level? (if not clear from context)
   - Any specific due dates? (if not mentioned)

3. **Create entries in Notion** using the MCP tools:

### For Projects (collection://ddce64cd-e64f-409e-bc98-82af09611364)
```
Properties:
- "Projects and Tasks": [project name]
- "Status": Planning | In progress | Backlog
- "Priority": Low | Medium | High
- "date:Dates:start": [start date]
- "date:Dates:end": [end date if range]
- "Summary": [brief description]
```

### For Tasks in Mike Tasks (collection://ce7acfb8-fbfb-4e8b-8ffd-50fc8ae79b80)
```
Properties:
- "Task name": [descriptive task name]
- "Status": Not started | In progress
- "Priority": Low | Medium | High
- "date:Due:start": [due date]
- "Tags": ["Work"] | ["Personal"] | ["Improvement"]
- "Lift": Light | Heavy (based on complexity)
- "Summary": [brief description]
- "Project": [link to project if applicable]
```

### For Work Tasks in Project List (collection://281213ec-88cd-81e3-9ff0-000b591d594b)
Use this for transit/work-specific tasks with Plan categories:
```
Properties:
- "Task Name": [task name]
- "Status": Not started | In progress
- "Priority": Low | Medium | High
- "Plan": [select from existing options if work-related]
- "date:Due:start": [due date]
- "Progress Notes": [any notes]
```

Plan options for work tasks:
- "1.1 Route 2 Launch"
- "1.2 TOD Zone E.F.H Launch"
- "1.3 Route 8 Adjustments"
- "1.4 Allandale Terminal Movement"
- "1.5 100.101 Improvements"
- "1.6 2025 Stop Infrastructure"
- "0.1 Milestones"
- "Allandale Customer Service"

4. **Confirm creation** by listing what was created with links.

## Example Input
```
From today's standup: Need to finish the Route 2 schedule updates by Friday.
Also coordinate with Operations on the new stop locations - medium priority.
Personal note: look into that budgeting app idea when I have time.
```

## Example Output
Created in Notion:
- Task: "Finish Route 2 schedule updates" (High, Due: Friday, Work, Plan: 1.1 Route 2 Launch)
- Task: "Coordinate with Operations on new stop locations" (Medium, Work, Plan: 1.1 Route 2 Launch)
- Task: "Explore budgeting app idea" (Low, Personal)

## Tips for Users
- Include dates naturally: "by Friday", "next week", "end of Q1"
- Mention priority: "urgent", "ASAP", "when possible"
- Context helps: "for work", "personal project", "home task"
- Name people to auto-assign
