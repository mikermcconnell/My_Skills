# Word Document Styling Reference

Complete styling configuration for professional Word documents.

## Table of Contents
1. [Color Scheme](#color-scheme)
2. [Document Setup](#document-setup)
3. [Paragraph Styles](#paragraph-styles)
4. [List Configuration](#list-configuration)
5. [Table Patterns](#table-patterns)
6. [Helper Functions](#helper-functions)
7. [Complete Template](#complete-template)

---

## Color Scheme

```javascript
const DARK_BLUE = "1F4E79";    // Primary headings, table headers
const MEDIUM_BLUE = "2E75B6";  // Secondary headings, accents
const LIGHT_GRAY = "F2F2F2";   // Alternating row shading
const WHITE = "FFFFFF";        // Header text, backgrounds
const DARK_GRAY = "333333";    // Heading 3, subtle text
```

---

## Document Setup

```javascript
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } }, // 11pt default
    paragraphStyles: [
      // Title - for cover pages
      { id: "Title", name: "Title", basedOn: "Normal",
        run: { size: 72, bold: true, color: DARK_BLUE, font: "Arial" },
        paragraph: { spacing: { before: 0, after: 200 }, alignment: AlignmentType.CENTER } },
      // Heading 1 - 16pt
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, color: DARK_BLUE, font: "Arial" },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      // Heading 2 - 13pt
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, color: MEDIUM_BLUE, font: "Arial" },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 } },
      // Heading 3 - 12pt
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, color: DARK_GRAY, font: "Arial" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 } },
    ]
  },
  numbering: { config: [] }, // Add list configs here
  sections: [{
    properties: {
      page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } // 1 inch margins
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: "Document Title", size: 18, color: "666666", font: "Arial" })]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Page ", size: 18, font: "Arial" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 18, font: "Arial" })
          ]
        })]
      })
    },
    children: [] // Document content goes here
  }]
});
```

---

## Paragraph Styles

### Headings
```javascript
// Heading 1
new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Section Title")] })

// Heading 2
new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Subsection")] })

// Heading 3
new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun("Sub-subsection")] })
```

### Body Text
```javascript
// Standard paragraph
new Paragraph({
  spacing: { after: 200 },
  children: [new TextRun({ text: "Body text content.", size: 22, font: "Arial" })]
})

// Paragraph with mixed formatting
new Paragraph({
  spacing: { after: 200 },
  children: [
    new TextRun({ text: "Regular text with ", size: 22, font: "Arial" }),
    new TextRun({ text: "bold", bold: true, size: 22, font: "Arial" }),
    new TextRun({ text: " and ", size: 22, font: "Arial" }),
    new TextRun({ text: "italic", italics: true, size: 22, font: "Arial" }),
    new TextRun({ text: " formatting.", size: 22, font: "Arial" })
  ]
})
```

### Table of Contents
```javascript
// Place after title, before content
new TableOfContents("Table of Contents", { hyperlink: true, headingStyleRange: "1-3" })
```

### Page Break
```javascript
// CRITICAL: Always wrap in Paragraph
new Paragraph({ children: [new PageBreak()] })
```

---

## List Configuration

### Numbering Config (add to Document numbering.config array)
```javascript
numbering: {
  config: [
    // Bullet list
    { reference: "bullet-list",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    // Numbered list - use unique reference for each independent list
    { reference: "numbered-list-1",
      levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    { reference: "numbered-list-2",
      levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
  ]
}
```

### List Items
```javascript
// Bullet item
new Paragraph({
  numbering: { reference: "bullet-list", level: 0 },
  children: [new TextRun({ text: "Bullet point text", size: 22, font: "Arial" })]
})

// Numbered item
new Paragraph({
  numbering: { reference: "numbered-list-1", level: 0 },
  children: [new TextRun({ text: "First numbered item", size: 22, font: "Arial" })]
})
```

**CRITICAL:** Each unique `reference` creates an independent list. Same reference = continues numbering. Different reference = restarts at 1.

---

## Table Patterns

### Border Definition
```javascript
const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };
```

### Header Cell Helper
```javascript
const headerCell = (text, width) => new TableCell({
  borders: cellBorders,
  width: { size: width, type: WidthType.DXA },
  shading: { fill: DARK_BLUE, type: ShadingType.CLEAR },
  children: [new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text, bold: true, color: WHITE, size: 20, font: "Arial" })]
  })]
});
```

### Regular Cell Helper
```javascript
const cell = (text, width, center = false, bold = false) => new TableCell({
  borders: cellBorders,
  width: { size: width, type: WidthType.DXA },
  children: [new Paragraph({
    alignment: center ? AlignmentType.CENTER : AlignmentType.LEFT,
    children: [new TextRun({ text, bold, size: 20, font: "Arial" })]
  })]
});
```

### Shaded Cell Helper (for alternating rows)
```javascript
const shadedCell = (text, width, center = false) => new TableCell({
  borders: cellBorders,
  width: { size: width, type: WidthType.DXA },
  shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
  children: [new Paragraph({
    alignment: center ? AlignmentType.CENTER : AlignmentType.LEFT,
    children: [new TextRun({ text, size: 20, font: "Arial" })]
  })]
});
```

### Table Example
```javascript
// Letter size with 1" margins = 9360 DXA usable width
new Table({
  columnWidths: [4680, 4680], // 2 equal columns
  rows: [
    new TableRow({ children: [headerCell("Column A", 4680), headerCell("Column B", 4680)] }),
    new TableRow({ children: [cell("Row 1 A", 4680), cell("Row 1 B", 4680)] }),
    new TableRow({ children: [shadedCell("Row 2 A", 4680), shadedCell("Row 2 B", 4680)] }),
    new TableRow({ children: [cell("Row 3 A", 4680), cell("Row 3 B", 4680)] }),
  ]
})
```

### Common Column Width Presets (9360 DXA total)
- 2 columns: `[4680, 4680]`
- 3 columns: `[3120, 3120, 3120]`
- 4 columns: `[2340, 2340, 2340, 2340]`
- Key-value (40/60): `[3744, 5616]`

---

## Helper Functions

### Parse Markdown Table to Data
```javascript
function parseMarkdownTable(mdTable) {
  const lines = mdTable.trim().split('\n');
  const headers = lines[0].split('|').filter(c => c.trim()).map(c => c.trim());
  const rows = lines.slice(2).map(line => 
    line.split('|').filter(c => c.trim()).map(c => c.trim())
  );
  return { headers, rows };
}
```

### Create Table from Parsed Data
```javascript
function createTable(headers, rows, colWidths) {
  const tableRows = [
    new TableRow({ children: headers.map((h, i) => headerCell(h, colWidths[i])) }),
    ...rows.map((row, rowIdx) => new TableRow({
      children: row.map((cell, colIdx) => 
        rowIdx % 2 === 1 ? shadedCell(cell, colWidths[colIdx]) : cell(cell, colWidths[colIdx])
      )
    }))
  ];
  return new Table({ columnWidths: colWidths, rows: tableRows });
}
```

---

## Complete Template

```javascript
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, TableOfContents, HeadingLevel,
  BorderStyle, WidthType, ShadingType, PageNumber, PageBreak } = require('docx');

// Colors
const DARK_BLUE = "1F4E79";
const MEDIUM_BLUE = "2E75B6";
const LIGHT_GRAY = "F2F2F2";
const WHITE = "FFFFFF";
const DARK_GRAY = "333333";

// Table helpers
const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

const headerCell = (text, width) => new TableCell({
  borders: cellBorders, width: { size: width, type: WidthType.DXA },
  shading: { fill: DARK_BLUE, type: ShadingType.CLEAR },
  children: [new Paragraph({ alignment: AlignmentType.CENTER,
    children: [new TextRun({ text, bold: true, color: WHITE, size: 20, font: "Arial" })] })]
});

const cell = (text, width, center = false, bold = false) => new TableCell({
  borders: cellBorders, width: { size: width, type: WidthType.DXA },
  children: [new Paragraph({ alignment: center ? AlignmentType.CENTER : AlignmentType.LEFT,
    children: [new TextRun({ text, bold, size: 20, font: "Arial" })] })]
});

const shadedCell = (text, width, center = false) => new TableCell({
  borders: cellBorders, width: { size: width, type: WidthType.DXA },
  shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
  children: [new Paragraph({ alignment: center ? AlignmentType.CENTER : AlignmentType.LEFT,
    children: [new TextRun({ text, size: 20, font: "Arial" })] })]
});

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal",
        run: { size: 72, bold: true, color: DARK_BLUE, font: "Arial" },
        paragraph: { spacing: { before: 0, after: 200 }, alignment: AlignmentType.CENTER } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, color: DARK_BLUE, font: "Arial" },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, color: MEDIUM_BLUE, font: "Arial" },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, color: DARK_GRAY, font: "Arial" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 } },
    ]
  },
  numbering: {
    config: [
      { reference: "bullet-list",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "numbered-list-1",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    ]
  },
  sections: [{
    properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    headers: {
      default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: "Document Title", size: 18, color: "666666", font: "Arial" })] })] })
    },
    footers: {
      default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: "Page ", size: 18, font: "Arial" }),
          new TextRun({ children: [PageNumber.CURRENT], size: 18, font: "Arial" })] })] })
    },
    children: [
      // Cover page
      new Paragraph({ spacing: { before: 2400 }, children: [] }),
      new Paragraph({ alignment: AlignmentType.CENTER, children: [
        new TextRun({ text: "DOCUMENT TITLE", size: 56, bold: true, color: DARK_BLUE, font: "Arial" })] }),
      new Paragraph({ children: [new PageBreak()] }),
      
      // Table of Contents
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Table of Contents")] }),
      new TableOfContents("Table of Contents", { hyperlink: true, headingStyleRange: "1-3" }),
      new Paragraph({ children: [new PageBreak()] }),
      
      // Content sections
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Section 1")] }),
      new Paragraph({ spacing: { after: 200 },
        children: [new TextRun({ text: "Section content goes here.", size: 22, font: "Arial" })] }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/mnt/user-data/outputs/document.docx", buffer);
  console.log("Document created!");
});
```
