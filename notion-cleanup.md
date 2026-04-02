# Notion Cleanup Helper

Bulk update, fix, or remove problematic Notion entries.

## Trigger
User invokes `/notion-cleanup` to fix issues found in review or perform bulk updates.

## Databases

### Mike Tasks (collection://ce7acfb8-fbfb-4e8b-8ffd-50fc8ae79b80)
- Data source ID: ce7acfb8-fbfb-4e8b-8ffd-50fc8ae79b80

### Projects (collection://ddce64cd-e64f-409e-bc98-82af09611364)
- Data source ID: ddce64cd-e64f-409e-bc98-82af09611364

### Project List - Work (collection://281213ec-88cd-81e3-9ff0-000b591d594b)
- Data source ID: 281213ec-88cd-81e3-9ff0-000b591d594b

## Cleanup Operations

### 1. Delete Orphaned Tasks
Find and offer to delete tasks named "Task" with no real content:
```
1. Search for tasks with title "Task"
2. Check if they have meaningful content
3. List them for user confirmation
4. Delete upon approval (move to Archived status or actual delete)
```

### 2. Bulk Status Updates
User says: "Mark all Route 2 tasks as Done"
```
1. Search for tasks matching criteria
2. List what will be updated
3. Confirm with user
4. Update Status property on each
```

### 3. Add Missing Metadata
User says: "Add due dates to all tasks without them"
```
1. Search for tasks where Due is empty
2. List them
3. Ask user for default due date or individual dates
4. Update each task
```

### 4. Priority Sweep
User says: "Set all 'Not started' tasks older than 2 weeks to Low priority"
```
1. Find matching tasks
2. Show list
3. Confirm
4. Bulk update Priority field
```

### 5. Archive Completed
User says: "Archive all Done tasks older than 30 days"
```
1. Find Done tasks with old timestamps
2. List them
3. Confirm
4. Change Status to Archived
```

### 6. Link Orphaned Tasks to Projects
User says: "Link unassigned tasks to projects"
```
1. Find tasks with empty Project relation
2. List them with context
3. Suggest project matches based on content
4. Update relations upon confirmation
```

## Confirmation Protocol

ALWAYS confirm before bulk operations:
```
I found X items matching your criteria:
1. [Item 1] - [current state]
2. [Item 2] - [current state]
...

Should I proceed with [action] on all X items? (yes/no/select specific)
```

## Common Cleanup Scenarios

### After Weekly Review
```
User: "Fix the issues from the review"
Action:
1. Reference the review findings
2. Propose fixes for each category
3. Execute approved changes
```

### Project Completion
```
User: "Close out the Route 2 Launch project"
Action:
1. Find all tasks linked to Route 2
2. Mark remaining as Done or Canceled
3. Update project status to Done
4. Add completion date
```

### Fresh Start
```
User: "Clean slate - archive everything old and start fresh"
Action:
1. Archive all Done items
2. Move stale Not started to Backlog
3. Review In progress items
4. Clear orphaned entries
```

## Safety Rules

1. **Never delete without confirmation** - Always list items first
2. **Prefer Archive over Delete** - Use Status: Archived when possible
3. **Show before/after** - Display what will change
4. **Batch wisely** - For 10+ items, confirm in groups
5. **Preserve relations** - Warn if deleting linked items

## Valid Property Values Reference

### Mike Tasks Status
- Not started, Blocked, In progress, Done, Archived

### Projects Status
- Backlog, Planning, In progress, Paused, Done, Canceled

### Priority (all databases)
- Low, Medium, High

### Tags (Mike Tasks)
- Personal, Work, Improvement

### Lift (Mike Tasks)
- Light, Heavy

### Plan (Project List - Work)
- 1.1 Route 2 Launch
- 1.2 TOD Zone E.F.H Launch
- 1.3 Route 8 Adjustments
- 1.4 Allandale Terminal Movement
- 1.5 100.101 Improvements
- 1.6 2025 Stop Infrastructure
- 0.1 Milestones
- Allandale Customer Service
