# Notion Weekly Review

Analyze Notion workspace health and surface items needing attention.

## Trigger
User invokes `/notion-review` to get a status report on their Notion workspace.

## Databases to Analyze

### Mike Tasks (collection://ce7acfb8-fbfb-4e8b-8ffd-50fc8ae79b80)
Personal task database with:
- Status: Not started, Blocked, In progress, Done, Archived
- Priority: Low, Medium, High
- Tags: Personal, Work, Improvement
- Due dates, Subtasks, Parent-tasks

### Projects (collection://ddce64cd-e64f-409e-bc98-82af09611364)
Project tracking with:
- Status: Backlog, Planning, In progress, Paused, Done, Canceled
- Priority, Dates, Owner, Completion rollup
- Blocking dependencies

### Project List - Work (collection://281213ec-88cd-81e3-9ff0-000b591d594b)
Transit/work tasks with Plan categories

## Review Checklist

Search and report on:

### 1. Overdue Items
- Tasks with Due date in the past and Status not Done/Archived
- Projects with end Dates passed and Status not Done/Canceled

### 2. Due This Week
- Tasks due within the next 7 days
- Projects with dates ending this week

### 3. Stale Items
- Tasks "In progress" for more than 14 days (check timestamps)
- Tasks "Not started" created more than 30 days ago
- Projects in "Planning" for more than 30 days

### 4. Missing Metadata
- Tasks without Due dates
- Tasks without Priority set
- Tasks with generic names like "Task"
- Projects without Dates

### 5. Blocked Items
- Tasks with Status = "Blocked"
- Check what they're blocked by (Blocked by relation)

### 6. Orphaned Items
- Tasks not linked to any Project
- Empty description tasks

## Output Format

```
## Notion Weekly Review - [Date]

### Immediate Attention (Overdue)
- [ ] Task Name - Due: [date] - [link]

### Due This Week
- [ ] Task Name - Due: [date] - Priority: [X] - [link]

### Stale/Stuck Items
- [ ] Task Name - Status: In progress since [date] - [link]

### Needs Metadata
- [ ] Task Name - Missing: Due date, Priority - [link]

### Blocked
- [ ] Task Name - Blocked by: [blocker] - [link]

### Quick Wins (Light lift, ready to start)
- [ ] Task Name - Lift: Light - [link]

### Summary
- Total active tasks: X
- Overdue: X
- Due this week: X
- Blocked: X
- Needs cleanup: X

### Suggested Actions
1. [Specific suggestion based on findings]
2. [Another suggestion]
```

## Follow-up Prompts
After review, user can say:
- "Update [task] to Done"
- "Change priority on [task] to High"
- "Set due date for [task] to next Friday"
- "Delete the orphaned Task entries"
- "Run /notion-cleanup to fix the metadata issues"
