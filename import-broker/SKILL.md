---
name: import-broker
description: Parse brokerage transactions into the import format expected by this Investing app. Use when working on this Investing project and the user wants to import transactions from Wealthsimple, Questrade, TD, or another broker, or when they paste brokerage transaction data and need it transformed into an app-ready CSV.
---

# Import Broker Skill

Help users import transactions from their brokerage accounts by parsing various formats.

## Triggers

- User asks to "import transactions", "import from Wealthsimple/Questrade/TD", "parse broker data"
- `/import-broker` command
- User pastes transaction data and asks for help importing

## Supported Brokers

| Broker | Status | Input Method |
|--------|--------|--------------|
| Wealthsimple Trade | Implemented | Copy-paste transaction details |
| Questrade | Placeholder | CSV export |
| TD Direct Investing | Placeholder | CSV export |
| Interactive Brokers | Placeholder | Flex Query CSV |
| Generic CSV | Supported | Standard CSV format |

## Workflow

### 1. Identify the Broker Format

Analyze pasted data for indicators:

**Wealthsimple**: Standalone tickers, "Market buy/sell", "X shares x $Y.YY USD", Canadian account types (TFSA/RRSP)
**Questrade**: CSV with Transaction Date, Symbol, Action, Quantity, Price columns
**Generic CSV**: Header row with symbol, quantity, price, action

### 2. Parse the Data

```python
from src.data.bank_parsers import parse_bank_format, BANK_PARSERS
result = parse_bank_format(user_text, 'wealthsimple')
```

### 3. Validate and Preview

Show parsed transactions in a table format.

### 4. Generate Import CSV

Output CSV ready for portfolio import.

### 5. Import Instructions

Direct user to Portfolio page → Import CSV → Paste → Select portfolio → Confirm.

## Adding a New Broker Parser

Update `src/data/bank_parsers.py` with new parser function and register in BANK_PARSERS dict.
