---
name: md-to-docx
description: Convert Markdown files to professional Word documents (.docx) with municipal/corporate styling. Creates print-ready documents with proper heading hierarchy, styled tables, headers/footers, and table of contents. Use when converting markdown to Word, creating reports from markdown, or when user requests a professional document from markdown content.
---

# Markdown to Word Document Converter

Convert Markdown content to professionally styled Word documents using docx-js.

## Workflow

1. **Parse Markdown structure** - Identify headings, paragraphs, lists, tables, code blocks
2. **Read style reference** - See [references/docx-styles.md](references/docx-styles.md) for complete styling configuration
3. **Generate JavaScript** - Create docx-js script following patterns in reference
4. **Execute and output** - Run script, save to `/mnt/user-data/outputs/`

## Markdown → Word Mapping

| Markdown | Word Element | Style |
|----------|--------------|-------|
| `#` | Heading 1 | 16pt bold, dark blue |
| `##` | Heading 2 | 13pt bold, medium blue |
| `###` | Heading 3 | 12pt bold, dark gray |
| Paragraphs | Body text | 11pt Arial |
| `- item` | Bullet list | Proper Word list |
| `1. item` | Numbered list | Proper Word list |
| `| table |` | Table | Bordered, header shading |
| `**bold**` | Bold | TextRun bold: true |
| `*italic*` | Italic | TextRun italics: true |
| `---` | Page break | new PageBreak() |

## Quick Start Template

```javascript
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, TableOfContents, HeadingLevel,
  BorderStyle, WidthType, ShadingType, PageNumber, PageBreak } = require('docx');

// Professional color scheme
const DARK_BLUE = "1F4E79";
const MEDIUM_BLUE = "2E75B6";
const LIGHT_GRAY = "F2F2F2";

// See references/docx-styles.md for complete configuration
```

## Key Requirements

1. **Always use proper Word lists** - Never use unicode bullets (•), always use `numbering` config with `LevelFormat.BULLET`
2. **Set column widths on tables** - Use both `columnWidths` array AND individual cell widths
3. **Page breaks in paragraphs** - Always wrap: `new Paragraph({ children: [new PageBreak()] })`
4. **Override built-in heading styles** - Use IDs: "Heading1", "Heading2", "Heading3" with `outlineLevel` for TOC
5. **Use ShadingType.CLEAR** - Never use ShadingType.SOLID (causes black backgrounds)

## Output Location

Save generated documents to: `/mnt/user-data/outputs/[filename].docx`
