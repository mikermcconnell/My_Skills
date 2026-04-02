---
name: md-to-xlsx
description: Convert Markdown files containing tables to professional Excel spreadsheets (.xlsx). Parses markdown tables, applies professional formatting, and creates multi-sheet workbooks. Use when converting markdown tables to Excel, creating spreadsheets from markdown data, or when user requests Excel output from markdown content.
---

# Markdown to Excel Converter

Convert Markdown tables and structured data to professionally styled Excel spreadsheets.

## Prerequisites

**Read the xlsx skill:** This skill builds on `/mnt/skills/public/xlsx/SKILL.md` for Excel creation patterns and formula best practices.

## Workflow

1. **Parse Markdown tables** - Extract table headers, rows, and data types
2. **Identify structure** - Determine sheets, data relationships
3. **Generate Excel** - Create workbook with openpyxl
4. **Apply formatting** - Headers, column widths, number formats
5. **Recalculate if needed** - Use recalc.py for formula evaluation
6. **Save to outputs** - Write to `/mnt/user-data/outputs/`

## Markdown Table Parsing

### Standard Markdown Table
```markdown
| Name | Value | Category |
|------|-------|----------|
| Item A | 100 | Type 1 |
| Item B | 200 | Type 2 |
```

### Parsing Logic
```python
def parse_markdown_table(md_table):
    lines = md_table.strip().split('\n')
    # Line 0: headers
    headers = [c.strip() for c in lines[0].split('|') if c.strip()]
    # Line 1: separator (skip)
    # Line 2+: data rows
    rows = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.split('|') if c.strip()]
        if cells:
            rows.append(cells)
    return headers, rows
```

## Data Type Detection

| Pattern | Excel Format | Example |
|---------|--------------|---------|
| Integer | `#,##0` | 1000 → 1,000 |
| Decimal | `#,##0.00` | 1000.50 |
| Percentage | `0.0%` | 15% |
| Currency | `$#,##0.00` | $1,000.00 |
| Date | `YYYY-MM-DD` | 2024-01-15 |
| Text | General | Everything else |

```python
import re

def detect_type(value):
    if re.match(r'^\$[\d,]+\.?\d*$', value):
        return 'currency', float(value.replace('$', '').replace(',', ''))
    if re.match(r'^[\d,]+\.?\d*%$', value):
        return 'percent', float(value.replace('%', '').replace(',', '')) / 100
    if re.match(r'^\d{4}-\d{2}-\d{2}$', value):
        return 'date', value
    if re.match(r'^[\d,]+$', value):
        return 'integer', int(value.replace(',', ''))
    if re.match(r'^[\d,]+\.\d+$', value):
        return 'decimal', float(value.replace(',', ''))
    return 'text', value
```

## Excel Styling (Consistent with docx)

### Color Scheme
```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

DARK_BLUE = "1F4E79"
MEDIUM_BLUE = "2E75B6"
LIGHT_GRAY = "F2F2F2"
WHITE = "FFFFFF"

# Header style
header_font = Font(bold=True, color=WHITE, name='Arial', size=10)
header_fill = PatternFill('solid', fgColor=DARK_BLUE)
header_align = Alignment(horizontal='center', vertical='center')

# Data cell style
data_font = Font(name='Arial', size=10)
alt_row_fill = PatternFill('solid', fgColor=LIGHT_GRAY)

# Border
thin_border = Border(
    left=Side(style='thin', color='CCCCCC'),
    right=Side(style='thin', color='CCCCCC'),
    top=Side(style='thin', color='CCCCCC'),
    bottom=Side(style='thin', color='CCCCCC')
)
```

## Complete Conversion Template

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import re

# Colors
DARK_BLUE = "1F4E79"
LIGHT_GRAY = "F2F2F2"
WHITE = "FFFFFF"

# Styles
header_font = Font(bold=True, color=WHITE, name='Arial', size=10)
header_fill = PatternFill('solid', fgColor=DARK_BLUE)
header_align = Alignment(horizontal='center', vertical='center')
data_font = Font(name='Arial', size=10)
alt_fill = PatternFill('solid', fgColor=LIGHT_GRAY)
border = Border(
    left=Side(style='thin', color='CCCCCC'),
    right=Side(style='thin', color='CCCCCC'),
    top=Side(style='thin', color='CCCCCC'),
    bottom=Side(style='thin', color='CCCCCC')
)

def parse_table(md_table):
    lines = md_table.strip().split('\n')
    headers = [c.strip() for c in lines[0].split('|') if c.strip()]
    rows = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.split('|') if c.strip()]
        if cells:
            rows.append(cells)
    return headers, rows

def create_excel(headers, rows, output_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"
    
    # Write headers
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = border
    
    # Write data with alternating rows
    for row_idx, row_data in enumerate(rows, 2):
        for col_idx, value in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.font = data_font
            cell.border = border
            if row_idx % 2 == 0:
                cell.fill = alt_fill
    
    # Auto-adjust column widths
    for col in range(1, len(headers) + 1):
        max_len = max(
            len(str(ws.cell(row=r, column=col).value or ''))
            for r in range(1, len(rows) + 2)
        )
        ws.column_dimensions[get_column_letter(col)].width = min(max_len + 2, 50)
    
    # Freeze header row
    ws.freeze_panes = 'A2'
    
    wb.save(output_path)
    print(f"Created: {output_path}")

# Usage
markdown = """
| Name | Value | Category |
|------|-------|----------|
| Item A | 100 | Type 1 |
| Item B | 200 | Type 2 |
"""
headers, rows = parse_table(markdown)
create_excel(headers, rows, '/mnt/user-data/outputs/data.xlsx')
```

## Multiple Tables → Multiple Sheets

When markdown contains multiple tables:

```python
def extract_tables(markdown):
    """Extract all tables from markdown with their preceding headers."""
    tables = []
    current_header = "Sheet1"
    lines = markdown.split('\n')
    table_lines = []
    
    for line in lines:
        if line.startswith('## '):
            current_header = line[3:].strip()[:31]  # Excel sheet name limit
        elif line.startswith('|'):
            table_lines.append(line)
        elif table_lines and not line.startswith('|'):
            if len(table_lines) > 2:  # Has data (header + separator + rows)
                tables.append((current_header, '\n'.join(table_lines)))
            table_lines = []
    
    if table_lines and len(table_lines) > 2:
        tables.append((current_header, '\n'.join(table_lines)))
    
    return tables

# Create multi-sheet workbook
wb = Workbook()
wb.remove(wb.active)  # Remove default sheet

for sheet_name, table_md in extract_tables(markdown):
    headers, rows = parse_table(table_md)
    ws = wb.create_sheet(title=sheet_name)
    # Apply formatting as above...
```

## Output Location

Save generated spreadsheets to: `/mnt/user-data/outputs/[filename].xlsx`

## See Also

- `/mnt/skills/public/xlsx/SKILL.md` - Full Excel creation patterns
- `/mnt/skills/public/xlsx/recalc.py` - Formula recalculation
