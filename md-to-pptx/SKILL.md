---
name: md-to-pptx
description: Convert Markdown files to professional PowerPoint presentations (.pptx). Parses markdown structure into slides, maps content to appropriate layouts (title, content, two-column), and generates polished presentations. Use when converting markdown to PowerPoint, creating presentations from markdown, or when user requests slides from markdown content.
---

# Markdown to PowerPoint Converter

Convert Markdown content to professionally styled PowerPoint presentations.

## Prerequisites

**Read the pptx skill first:** This skill builds on `/mnt/skills/public/pptx/SKILL.md`. Read that skill and its `html2pptx.md` reference for the complete PowerPoint creation workflow.

## Workflow

1. **Parse Markdown into slides** - Identify slide boundaries and content
2. **Map to slide layouts** - Determine layout for each slide
3. **Generate HTML slides** - Create HTML following html2pptx format
4. **Convert to PowerPoint** - Use html2pptx workflow from pptx skill
5. **Validate visually** - Check output for layout issues

## Markdown → Slide Parsing Rules

### Slide Boundaries (in order of precedence)
1. `---` horizontal rule = explicit slide break
2. `# Heading 1` = new slide (title slide or section)
3. `## Heading 2` = new slide (content slide)
4. Every ~5-7 bullet points = consider splitting

### Content Type Detection

| Markdown Pattern | Slide Layout |
|------------------|--------------|
| `# Title` alone or with subtitle | Title Slide |
| `## Heading` + bullets | Content Slide |
| `## Heading` + two lists | Two-Column |
| `## Heading` + paragraph | Statement Slide |
| Image only | Full Image Slide |
| Table | Table Slide |

### Speaker Notes
Content in HTML comments becomes speaker notes:
```markdown
## Slide Title
- Point 1
- Point 2

<!-- Speaker notes: Remember to mention the budget impact -->
```

## Markdown to Slide Mapping

### Title Slide
```markdown
# Presentation Title
Subtitle or tagline

---
```
→ Title centered, subtitle below, often with accent bar

### Content Slide
```markdown
## Section Title
- First bullet point
- Second bullet point  
- Third bullet point
```
→ Title in header zone, bullets in content zone

### Two-Column Slide
```markdown
## Comparison

**Left Column**
- Item A
- Item B

**Right Column**
- Item C
- Item D
```
→ Split content into two columns

### Statement Slide
```markdown
## Key Insight

A single impactful sentence or quote that deserves emphasis.
```
→ Large centered text, minimal other content

## Color Scheme (Consistent with docx styling)

```css
:root {
  --primary: #1F4E79;      /* Dark blue - titles, headers */
  --secondary: #2E75B6;    /* Medium blue - accents */
  --background: #FFFFFF;   /* White slides */
  --text: #333333;         /* Dark gray body text */
  --accent: #F2F2F2;       /* Light gray for subtle backgrounds */
}
```

## HTML Slide Template

Each slide is 960×540px (16:9 ratio). Basic structure:

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="slide">
    <div class="header">
      <h1>Slide Title</h1>
    </div>
    <div class="content">
      <ul>
        <li>Bullet point</li>
        <li>Another point</li>
      </ul>
    </div>
  </div>
</body>
</html>
```

## Quick Reference: Slide Limits

| Element | Guideline |
|---------|-----------|
| Title length | Max 8 words |
| Bullets per slide | 3-6 items |
| Words per bullet | Max 12 words |
| Slides per section | 5-8 slides |

## Output Workflow

1. Create `styles.css` with design system
2. Create `slide-N.html` for each slide
3. Run html2pptx conversion:
   ```bash
   mkdir -p html2pptx && tar -xzf /mnt/skills/public/pptx/html2pptx.tgz -C html2pptx
   NODE_PATH="$(npm root -g)" node convert.js 2>&1
   ```
4. Validate output visually
5. Save to `/mnt/user-data/outputs/`

## See Also

- `/mnt/skills/public/pptx/SKILL.md` - Full PowerPoint creation workflow
- `/mnt/skills/public/pptx/html2pptx.md` - HTML to PPTX conversion details
- `/mnt/skills/public/pptx/css.md` - CSS styling for slides
