---
name: md-to-document
description: Router skill for converting Markdown files to professional documents. Analyzes Markdown content structure and routes to the appropriate converter skill (md-to-docx for Word, md-to-pptx for PowerPoint, md-to-xlsx for Excel). Use when user provides a Markdown file and requests conversion to a document format, or asks to "create a document from this markdown" without specifying format.
---

# Markdown to Document Router

Analyze Markdown content and route to the appropriate converter skill.

## Decision Logic

### Route to md-to-docx (Word) when:
- Content is primarily prose with headings and paragraphs
- Document structure includes: executive summaries, reports, proposals, plans
- Contains mixed content: text, lists, tables, images
- User mentions: "report", "document", "Word", "docx", "print-ready"
- **Default choice** when format is ambiguous

### Route to md-to-pptx (PowerPoint) when:
- Content has clear slide-like sections (short chunks)
- Markdown uses `---` horizontal rules as dividers
- Structure follows: title → bullet points pattern repeatedly
- Content is designed for presentation/speaking
- User mentions: "presentation", "slides", "PowerPoint", "pptx", "deck"

### Route to md-to-xlsx (Excel) when:
- Content is primarily tabular data
- Multiple Markdown tables present
- Data appears to need sorting, filtering, or calculations
- Content represents: inventories, tracking sheets, data exports
- User mentions: "spreadsheet", "Excel", "xlsx", "data", "table"

## Routing Workflow

1. **Analyze content structure:**
   ```
   Tables present?     → Count and assess prominence
   Slide markers?      → Look for `---` or `# Slide:` patterns
   Prose-heavy?        → Long paragraphs, varied formatting
   ```

2. **Check user intent:**
   - Explicit format request → Use that format
   - Keywords present → Match to format
   - Ambiguous → Default to Word (most versatile)

3. **Route to skill:**
   - Read the appropriate skill: `/mnt/skills/user/md-to-docx/SKILL.md`, `/mnt/skills/user/md-to-pptx/SKILL.md`, or `/mnt/skills/user/md-to-xlsx/SKILL.md`
   - Follow that skill's workflow

## Quick Reference

| Content Pattern | Format | Skill |
|-----------------|--------|-------|
| Reports, plans, proposals | Word | md-to-docx |
| Slide decks, presentations | PowerPoint | md-to-pptx |
| Data tables, tracking sheets | Excel | md-to-xlsx |
| Mixed/unclear | Word | md-to-docx |

## Example Routing Decisions

**Input:** Markdown with headings, paragraphs, a few tables, bullet lists
**Route:** md-to-docx (document structure, mixed content)

**Input:** Markdown with `---` separators, each section has title + 3-5 bullets
**Route:** md-to-pptx (presentation structure)

**Input:** Markdown with 5 large tables, minimal prose
**Route:** md-to-xlsx (data-centric)
