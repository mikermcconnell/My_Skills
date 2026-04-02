# PowerPoint Slide Patterns Reference

Detailed patterns for converting Markdown content to HTML slides.

## Table of Contents
1. [CSS Design System](#css-design-system)
2. [Slide Layout Templates](#slide-layout-templates)
3. [Content Parsing Functions](#content-parsing-functions)
4. [Conversion Script Template](#conversion-script-template)

---

## CSS Design System

Create `styles.css` for consistent styling across all slides:

```css
:root {
  /* Primary colors - matches docx styling */
  --primary: #1F4E79;
  --secondary: #2E75B6;
  --text-dark: #333333;
  --text-light: #FFFFFF;
  --background: #FFFFFF;
  --accent-light: #F2F2F2;
  
  /* Typography */
  --font-family: 'Arial', 'Helvetica Neue', sans-serif;
  --title-size: 44px;
  --heading-size: 32px;
  --body-size: 24px;
  --small-size: 18px;
  
  /* Spacing */
  --padding: 40px;
  --gap: 20px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  width: 960px;
  height: 540px;
  font-family: var(--font-family);
  background: var(--background);
  color: var(--text-dark);
}

.slide {
  width: 100%;
  height: 100%;
  padding: var(--padding);
  display: flex;
  flex-direction: column;
}

/* Header zone */
.header {
  margin-bottom: var(--gap);
}

.header h1 {
  font-size: var(--heading-size);
  font-weight: bold;
  color: var(--primary);
  border-bottom: 3px solid var(--secondary);
  padding-bottom: 10px;
}

/* Content zone */
.content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

/* Bullet lists */
ul {
  list-style: none;
  padding-left: 0;
}

ul li {
  font-size: var(--body-size);
  margin-bottom: 16px;
  padding-left: 30px;
  position: relative;
}

ul li::before {
  content: "•";
  color: var(--secondary);
  font-weight: bold;
  position: absolute;
  left: 0;
}

/* Two-column layout */
.two-column {
  display: flex;
  gap: 40px;
}

.two-column .column {
  flex: 1;
}

.two-column .column h2 {
  font-size: var(--body-size);
  font-weight: bold;
  color: var(--secondary);
  margin-bottom: 16px;
}

/* Title slide */
.title-slide {
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title-slide h1 {
  font-size: var(--title-size);
  color: var(--primary);
  border: none;
  margin-bottom: 20px;
}

.title-slide .subtitle {
  font-size: var(--heading-size);
  color: var(--secondary);
}

/* Statement slide */
.statement-slide {
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 60px;
}

.statement-slide p {
  font-size: 36px;
  color: var(--primary);
  line-height: 1.4;
}

/* Accent bar */
.accent-bar {
  width: 100%;
  height: 8px;
  background: var(--secondary);
  position: absolute;
  bottom: 0;
  left: 0;
}

/* Footer */
.footer {
  font-size: var(--small-size);
  color: #666666;
  text-align: right;
  margin-top: auto;
  padding-top: var(--gap);
}
```

---

## Slide Layout Templates

### Title Slide
```html
<!DOCTYPE html>
<html>
<head><link rel="stylesheet" href="styles.css"></head>
<body>
  <div class="slide title-slide">
    <h1>Presentation Title</h1>
    <div class="subtitle">Subtitle or Date</div>
    <div class="accent-bar"></div>
  </div>
</body>
</html>
```

### Content Slide (Bullets)
```html
<!DOCTYPE html>
<html>
<head><link rel="stylesheet" href="styles.css"></head>
<body>
  <div class="slide">
    <div class="header">
      <h1>Section Title</h1>
    </div>
    <div class="content">
      <ul>
        <li>First key point with supporting detail</li>
        <li>Second key point explaining the concept</li>
        <li>Third point with actionable insight</li>
      </ul>
    </div>
    <div class="footer">Page 2</div>
  </div>
</body>
</html>
```

### Two-Column Slide
```html
<!DOCTYPE html>
<html>
<head><link rel="stylesheet" href="styles.css"></head>
<body>
  <div class="slide">
    <div class="header">
      <h1>Comparison Title</h1>
    </div>
    <div class="content two-column">
      <div class="column">
        <h2>Option A</h2>
        <ul>
          <li>Advantage one</li>
          <li>Advantage two</li>
        </ul>
      </div>
      <div class="column">
        <h2>Option B</h2>
        <ul>
          <li>Advantage one</li>
          <li>Advantage two</li>
        </ul>
      </div>
    </div>
  </div>
</body>
</html>
```

### Statement Slide
```html
<!DOCTYPE html>
<html>
<head><link rel="stylesheet" href="styles.css"></head>
<body>
  <div class="slide statement-slide">
    <p>"A powerful quote or key message that deserves emphasis and stands alone."</p>
  </div>
</body>
</html>
```

### Section Divider
```html
<!DOCTYPE html>
<html>
<head><link rel="stylesheet" href="styles.css"></head>
<body>
  <div class="slide title-slide" style="background: var(--primary);">
    <h1 style="color: white; border: none;">Section Name</h1>
    <div class="accent-bar" style="background: white;"></div>
  </div>
</body>
</html>
```

---

## Content Parsing Functions

### Parse Markdown into Slides
```javascript
function parseMarkdownToSlides(markdown) {
  const slides = [];
  
  // Split by horizontal rules first
  const sections = markdown.split(/\n---\n/);
  
  for (const section of sections) {
    const trimmed = section.trim();
    if (!trimmed) continue;
    
    // Detect slide type
    const slide = detectSlideType(trimmed);
    slides.push(slide);
  }
  
  return slides;
}

function detectSlideType(content) {
  const lines = content.split('\n').filter(l => l.trim());
  const firstLine = lines[0] || '';
  
  // Title slide: # Heading with minimal content
  if (firstLine.startsWith('# ') && lines.length <= 3) {
    return {
      type: 'title',
      title: firstLine.replace(/^# /, ''),
      subtitle: lines[1] || ''
    };
  }
  
  // Content slide: ## Heading with bullets
  if (firstLine.startsWith('## ')) {
    const title = firstLine.replace(/^## /, '');
    const bullets = lines.slice(1)
      .filter(l => l.startsWith('- ') || l.startsWith('* '))
      .map(l => l.replace(/^[-*] /, ''));
    
    // Check for two-column pattern
    const boldHeaders = lines.filter(l => l.match(/^\*\*[^*]+\*\*$/));
    if (boldHeaders.length >= 2) {
      return { type: 'two-column', title, content: parseColumns(lines.slice(1)) };
    }
    
    // Check for statement (single paragraph, no bullets)
    if (bullets.length === 0 && lines.length === 2) {
      return { type: 'statement', content: lines[1] };
    }
    
    return { type: 'content', title, bullets };
  }
  
  // Default to content
  return { type: 'content', title: '', bullets: lines };
}

function parseColumns(lines) {
  const columns = { left: { title: '', items: [] }, right: { title: '', items: [] } };
  let currentColumn = 'left';
  
  for (const line of lines) {
    if (line.match(/^\*\*[^*]+\*\*$/)) {
      if (columns.left.title) currentColumn = 'right';
      columns[currentColumn].title = line.replace(/\*\*/g, '');
    } else if (line.startsWith('- ') || line.startsWith('* ')) {
      columns[currentColumn].items.push(line.replace(/^[-*] /, ''));
    }
  }
  
  return columns;
}
```

### Generate HTML from Slide Object
```javascript
function generateSlideHTML(slide, index) {
  switch (slide.type) {
    case 'title':
      return `<!DOCTYPE html>
<html><head><link rel="stylesheet" href="styles.css"></head>
<body>
<div class="slide title-slide">
  <h1>${escapeHtml(slide.title)}</h1>
  ${slide.subtitle ? `<div class="subtitle">${escapeHtml(slide.subtitle)}</div>` : ''}
  <div class="accent-bar"></div>
</div>
</body></html>`;

    case 'content':
      return `<!DOCTYPE html>
<html><head><link rel="stylesheet" href="styles.css"></head>
<body>
<div class="slide">
  <div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
  <div class="content">
    <ul>
      ${slide.bullets.map(b => `<li>${escapeHtml(b)}</li>`).join('\n      ')}
    </ul>
  </div>
  <div class="footer">${index + 1}</div>
</div>
</body></html>`;

    case 'two-column':
      return `<!DOCTYPE html>
<html><head><link rel="stylesheet" href="styles.css"></head>
<body>
<div class="slide">
  <div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
  <div class="content two-column">
    <div class="column">
      <h2>${escapeHtml(slide.content.left.title)}</h2>
      <ul>${slide.content.left.items.map(i => `<li>${escapeHtml(i)}</li>`).join('')}</ul>
    </div>
    <div class="column">
      <h2>${escapeHtml(slide.content.right.title)}</h2>
      <ul>${slide.content.right.items.map(i => `<li>${escapeHtml(i)}</li>`).join('')}</ul>
    </div>
  </div>
</div>
</body></html>`;

    case 'statement':
      return `<!DOCTYPE html>
<html><head><link rel="stylesheet" href="styles.css"></head>
<body>
<div class="slide statement-slide">
  <p>${escapeHtml(slide.content)}</p>
</div>
</body></html>`;

    default:
      return '';
  }
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
```

---

## Conversion Script Template

Complete script to convert markdown to PowerPoint:

```javascript
const fs = require('fs');
const path = require('path');
const pptxgen = require('pptxgenjs');
const { html2pptx } = require('./html2pptx');

async function convertMarkdownToPptx(markdownPath, outputPath) {
  // Read markdown
  const markdown = fs.readFileSync(markdownPath, 'utf-8');
  
  // Parse into slides
  const slides = parseMarkdownToSlides(markdown);
  
  // Create working directory
  const workDir = '/home/claude/pptx-work';
  fs.mkdirSync(workDir, { recursive: true });
  
  // Write CSS
  fs.writeFileSync(path.join(workDir, 'styles.css'), CSS_CONTENT);
  
  // Generate HTML files
  slides.forEach((slide, i) => {
    const html = generateSlideHTML(slide, i);
    fs.writeFileSync(path.join(workDir, `slide-${i}.html`), html);
  });
  
  // Create PowerPoint
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  
  // Convert each slide
  for (let i = 0; i < slides.length; i++) {
    await html2pptx(path.join(workDir, `slide-${i}.html`), pptx);
  }
  
  // Save
  await pptx.writeFile(outputPath);
  console.log(`Created: ${outputPath}`);
}

// Run
convertMarkdownToPptx(
  '/mnt/user-data/uploads/input.md',
  '/mnt/user-data/outputs/presentation.pptx'
);
```
