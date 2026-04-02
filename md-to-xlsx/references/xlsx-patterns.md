# Excel Patterns Reference

Detailed patterns for converting Markdown to Excel spreadsheets.

## Table of Contents
1. [Style Configuration](#style-configuration)
2. [Number Formatting](#number-formatting)
3. [Advanced Table Features](#advanced-table-features)
4. [Formula Generation](#formula-generation)
5. [Complete Multi-Sheet Template](#complete-multi-sheet-template)

---

## Style Configuration

### Full Style Setup
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, NamedStyle
from openpyxl.utils import get_column_letter

# Color definitions (consistent with docx styling)
COLORS = {
    'dark_blue': '1F4E79',
    'medium_blue': '2E75B6',
    'light_gray': 'F2F2F2',
    'white': 'FFFFFF',
    'dark_gray': '333333',
    'border_gray': 'CCCCCC'
}

# Border style
thin_border = Border(
    left=Side(style='thin', color=COLORS['border_gray']),
    right=Side(style='thin', color=COLORS['border_gray']),
    top=Side(style='thin', color=COLORS['border_gray']),
    bottom=Side(style='thin', color=COLORS['border_gray'])
)

# Named styles for reuse
def create_styles(wb):
    # Header style
    header_style = NamedStyle(name='header')
    header_style.font = Font(bold=True, color=COLORS['white'], name='Arial', size=10)
    header_style.fill = PatternFill('solid', fgColor=COLORS['dark_blue'])
    header_style.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    header_style.border = thin_border
    wb.add_named_style(header_style)
    
    # Data style
    data_style = NamedStyle(name='data')
    data_style.font = Font(name='Arial', size=10)
    data_style.alignment = Alignment(vertical='center')
    data_style.border = thin_border
    wb.add_named_style(data_style)
    
    # Alternating row style
    alt_style = NamedStyle(name='alt_row')
    alt_style.font = Font(name='Arial', size=10)
    alt_style.fill = PatternFill('solid', fgColor=COLORS['light_gray'])
    alt_style.alignment = Alignment(vertical='center')
    alt_style.border = thin_border
    wb.add_named_style(alt_style)
    
    # Total row style
    total_style = NamedStyle(name='total')
    total_style.font = Font(bold=True, name='Arial', size=10)
    total_style.fill = PatternFill('solid', fgColor=COLORS['medium_blue'])
    total_style.font = Font(bold=True, color=COLORS['white'], name='Arial', size=10)
    total_style.border = thin_border
    wb.add_named_style(total_style)
```

---

## Number Formatting

### Format Codes
```python
NUMBER_FORMATS = {
    'integer': '#,##0',
    'decimal': '#,##0.00',
    'currency': '$#,##0.00',
    'currency_negative': '$#,##0.00;[Red]($#,##0.00)',
    'percent': '0.0%',
    'percent_int': '0%',
    'date': 'YYYY-MM-DD',
    'date_long': 'MMMM D, YYYY',
    'accounting': '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'
}

def apply_number_format(cell, value, col_header):
    """Apply appropriate number format based on column header and value."""
    header_lower = col_header.lower()
    
    # Currency columns
    if any(word in header_lower for word in ['price', 'cost', 'revenue', 'amount', '$']):
        cell.number_format = NUMBER_FORMATS['currency']
    # Percentage columns
    elif any(word in header_lower for word in ['rate', 'percent', '%', 'growth']):
        cell.number_format = NUMBER_FORMATS['percent']
    # Date columns
    elif any(word in header_lower for word in ['date', 'time', 'created', 'updated']):
        cell.number_format = NUMBER_FORMATS['date']
    # Integer detection
    elif isinstance(value, int) or (isinstance(value, float) and value.is_integer()):
        cell.number_format = NUMBER_FORMATS['integer']
    # Decimal detection
    elif isinstance(value, float):
        cell.number_format = NUMBER_FORMATS['decimal']
```

### Type Conversion
```python
import re
from datetime import datetime

def convert_value(raw_value, col_header=''):
    """Convert string value to appropriate Python type."""
    value = str(raw_value).strip()
    
    # Empty check
    if not value or value == '-':
        return None
    
    # Currency: $1,234.56
    if re.match(r'^\$[\d,]+\.?\d*$', value):
        return float(value.replace('$', '').replace(',', ''))
    
    # Percentage: 12.5%
    if re.match(r'^-?[\d,]+\.?\d*%$', value):
        return float(value.replace('%', '').replace(',', '')) / 100
    
    # Negative in parentheses: (123.45)
    if re.match(r'^\([\d,]+\.?\d*\)$', value):
        return -float(value.replace('(', '').replace(')', '').replace(',', ''))
    
    # Date: 2024-01-15
    if re.match(r'^\d{4}-\d{2}-\d{2}$', value):
        return datetime.strptime(value, '%Y-%m-%d')
    
    # Integer: 1,234
    if re.match(r'^-?[\d,]+$', value):
        return int(value.replace(',', ''))
    
    # Decimal: 1,234.56
    if re.match(r'^-?[\d,]+\.\d+$', value):
        return float(value.replace(',', ''))
    
    # Default: text
    return value
```

---

## Advanced Table Features

### Auto Column Width
```python
def auto_column_width(ws, min_width=8, max_width=50):
    """Automatically adjust column widths based on content."""
    for column_cells in ws.columns:
        max_length = 0
        column_letter = get_column_letter(column_cells[0].column)
        
        for cell in column_cells:
            if cell.value:
                cell_length = len(str(cell.value))
                if cell_length > max_length:
                    max_length = cell_length
        
        adjusted_width = min(max(max_length + 2, min_width), max_width)
        ws.column_dimensions[column_letter].width = adjusted_width
```

### Freeze Panes
```python
# Freeze header row
ws.freeze_panes = 'A2'

# Freeze first column and header row
ws.freeze_panes = 'B2'
```

### Auto Filter
```python
from openpyxl.utils import get_column_letter

def add_auto_filter(ws, headers):
    """Add auto-filter to header row."""
    last_col = get_column_letter(len(headers))
    last_row = ws.max_row
    ws.auto_filter.ref = f"A1:{last_col}{last_row}"
```

### Data Validation (Dropdown)
```python
from openpyxl.worksheet.datavalidation import DataValidation

def add_dropdown(ws, col_letter, options, start_row=2, end_row=100):
    """Add dropdown validation to a column."""
    dv = DataValidation(
        type="list",
        formula1=f'"{",".join(options)}"',
        showDropDown=False
    )
    dv.add(f'{col_letter}{start_row}:{col_letter}{end_row}')
    ws.add_data_validation(dv)
```

### Conditional Formatting
```python
from openpyxl.formatting.rule import ColorScaleRule, FormulaRule
from openpyxl.styles import PatternFill

def add_color_scale(ws, cell_range):
    """Add red-yellow-green color scale."""
    rule = ColorScaleRule(
        start_type='min', start_color='F8696B',  # Red
        mid_type='percentile', mid_value=50, mid_color='FFEB84',  # Yellow
        end_type='max', end_color='63BE7B'  # Green
    )
    ws.conditional_formatting.add(cell_range, rule)

def highlight_negative(ws, cell_range):
    """Highlight negative values in red."""
    red_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')
    red_font = Font(color='9C0006')
    rule = FormulaRule(
        formula=['A1<0'],
        fill=red_fill,
        font=red_font
    )
    ws.conditional_formatting.add(cell_range, rule)
```

---

## Formula Generation

### Summary Row Formulas
```python
def add_summary_row(ws, data_start_row, data_end_row, headers):
    """Add a summary row with SUM formulas for numeric columns."""
    summary_row = data_end_row + 1
    
    for col, header in enumerate(headers, 1):
        col_letter = get_column_letter(col)
        cell = ws.cell(row=summary_row, column=col)
        
        if col == 1:
            cell.value = "Total"
            cell.font = Font(bold=True)
        else:
            # Check if column appears numeric (sample first data cell)
            sample = ws.cell(row=data_start_row, column=col).value
            if isinstance(sample, (int, float)):
                cell.value = f"=SUM({col_letter}{data_start_row}:{col_letter}{data_end_row})"
        
        cell.style = 'total'
```

### Calculated Columns
```python
def add_calculated_column(ws, col_index, formula_template, start_row=2):
    """Add a calculated column with formulas.
    
    formula_template: Use {row} placeholder for row number
    Example: "=B{row}*C{row}" for quantity * price
    """
    for row in range(start_row, ws.max_row + 1):
        formula = formula_template.format(row=row)
        ws.cell(row=row, column=col_index, value=formula)
```

---

## Complete Multi-Sheet Template

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
header_align = Alignment(horizontal='center', vertical='center', wrap_text=True)
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

def extract_tables(markdown):
    tables = []
    current_header = "Data"
    lines = markdown.split('\n')
    table_lines = []
    
    for line in lines:
        if line.startswith('## '):
            current_header = line[3:].strip()[:31]
        elif line.startswith('|'):
            table_lines.append(line)
        elif table_lines and not line.startswith('|'):
            if len(table_lines) > 2:
                tables.append((current_header, '\n'.join(table_lines)))
            table_lines = []
    
    if table_lines and len(table_lines) > 2:
        tables.append((current_header, '\n'.join(table_lines)))
    
    return tables

def convert_value(raw):
    value = str(raw).strip()
    if not value:
        return None
    if re.match(r'^\$[\d,]+\.?\d*$', value):
        return float(value.replace('$', '').replace(',', ''))
    if re.match(r'^[\d,]+\.?\d*%$', value):
        return float(value.replace('%', '').replace(',', '')) / 100
    if re.match(r'^[\d,]+$', value):
        return int(value.replace(',', ''))
    if re.match(r'^[\d,]+\.\d+$', value):
        return float(value.replace(',', ''))
    return value

def create_sheet(ws, headers, rows):
    # Headers
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = border
    
    # Data
    for row_idx, row_data in enumerate(rows, 2):
        for col_idx, raw_value in enumerate(row_data, 1):
            value = convert_value(raw_value)
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.font = data_font
            cell.border = border
            if row_idx % 2 == 0:
                cell.fill = alt_fill
    
    # Column widths
    for col in range(1, len(headers) + 1):
        max_len = max(
            len(str(ws.cell(row=r, column=col).value or ''))
            for r in range(1, len(rows) + 2)
        )
        ws.column_dimensions[get_column_letter(col)].width = min(max_len + 2, 50)
    
    # Freeze header
    ws.freeze_panes = 'A2'
    
    # Auto filter
    last_col = get_column_letter(len(headers))
    ws.auto_filter.ref = f"A1:{last_col}{len(rows) + 1}"

def markdown_to_excel(markdown, output_path):
    wb = Workbook()
    wb.remove(wb.active)
    
    tables = extract_tables(markdown)
    if not tables:
        # No structured tables found, create single sheet
        tables = [("Data", markdown)]
    
    for sheet_name, table_md in tables:
        try:
            headers, rows = parse_table(table_md)
            if headers and rows:
                ws = wb.create_sheet(title=sheet_name)
                create_sheet(ws, headers, rows)
        except Exception as e:
            print(f"Warning: Could not parse table for {sheet_name}: {e}")
    
    if wb.sheetnames:
        wb.save(output_path)
        print(f"Created: {output_path}")
    else:
        print("No valid tables found in markdown")

# Usage
markdown_to_excel(markdown_content, '/mnt/user-data/outputs/workbook.xlsx')
```
