# Newsletter Project

Use this reference when changing the presentation layer of the Newsletter repo at `C:\Users\Mike McConnell\Documents\mike_apps\Newsletter`.

## Files To Open First

- `README.md` for output locations and CLI commands
- `src/newsletter_pipeline/rendering.py` for the weekly issue HTML and CSS
- `tests/test_rendering.py` for structural expectations that current changes must preserve or update intentionally

## Current Output Shape

The repo generates:

- weekly HTML issues in `data/issues/weekly-YYYY-MM-DD.html`
- weekly PDFs in `data/issues/weekly-YYYY-MM-DD.pdf`
- convenience PDFs in `data/drafts/weekly-YYYY-MM-DD.pdf`
- editorial review pages in `data/editorial/review-week-YYYY-MM-DD.html`

The main weekly issue already uses an editorial, magazine-like layout with:

- a masthead
- a lead feature card
- supporting rail cards
- section cards
- event cards with optional imagery

## Design Constraints

- HTML is used for both screen reading and Letter-sized PDF export, so print rules matter.
- Images are optional. Layouts must still read cleanly when no image exists.
- Structural copy such as branding and section labels may be asserted in tests.
- The design should feel editorial and local, not like a generic dashboard.

## Recommended Change Strategy

Start in `src/newsletter_pipeline/rendering.py`:

- adjust root tokens first
- then update related component groups together
- keep mobile and `@media print` rules aligned with the new direction

If the weekly issue changes meaningfully:

- render a fresh HTML issue
- inspect both cover and body layout
- run `pytest tests/test_rendering.py`

## What Good Looks Like Here

- strong cover hierarchy
- fast scan of top picks and section breaks
- readable summaries and metadata
- restrained decorative treatment
- polished print output without fragile page-break behavior
