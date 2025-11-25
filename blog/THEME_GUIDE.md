# VolunteerClear Blog Theme Guide

## Overview

The blog uses a custom Pelican theme designed to match the main VolunteerClear Vue application.

## Design Consistency

### Colors

Both sites use the same color palette:

| Element | Color | Usage |
|---------|-------|-------|
| Primary | `#2563eb` (blue-600) | Links, buttons, accents |
| Primary Dark | `#1d4ed8` (blue-700) | Hover states, gradients |
| Text | `#111827` (gray-900) | Headings, body text |
| Text Secondary | `#374151` (gray-700) | Body text, descriptions |
| Background | `#ffffff` (white) | Main background |
| Background Alt | `#f9fafb` (gray-50) | Subtle backgrounds |

### Typography

Both sites use the **Inter** font family:

- **Headings**: Bold (700), clear hierarchy
- **Body**: Regular (400), 17px base size
- **Links**: Medium (500) weight
- **Line Height**: 1.75 for comfortable reading

### Components

#### Header
- **Main Site**: Fixed navigation with transparent/white background
- **Blog**: Blue gradient header with site title and navigation
- **Consistency**: Both use white text on blue, same font

#### Content Cards
- **Main Site**: Sections with rounded corners, subtle shadows
- **Blog**: Article cards with same styling
- **Consistency**: Same border-radius (0.5rem), same shadows

#### Buttons/Links
- **Main Site**: Blue buttons with hover effects
- **Blog**: Blue links and "Read More" buttons
- **Consistency**: Same blue color, same hover transitions

#### Footer
- **Main Site**: Dark footer with links
- **Blog**: Dark footer (gray-900) with similar layout
- **Consistency**: Same background color, same link styling

## Layout Differences

### Main Site (Vue SPA)
- Single-page application
- Smooth scroll between sections
- Full-width hero sections
- Interactive components

### Blog (Static HTML)
- Multi-page site
- Traditional navigation
- Centered content (800px max-width)
- Focus on readability

These differences are intentional - the blog prioritizes reading experience while the main site prioritizes conversion.

## Customizing the Theme

### Changing Colors

Edit `blog/themes/volunteerclear/static/css/style.css`:

```css
:root {
  --primary-600: #2563eb;  /* Your primary color */
  --primary-700: #1d4ed8;  /* Darker shade */
  --gray-900: #111827;     /* Text color */
  /* ... */
}
```

### Changing Fonts

1. Update font link in `blog/themes/volunteerclear/templates/base.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=YourFont:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

2. Update CSS in `static/css/style.css`:
```css
body {
  font-family: 'YourFont', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
```

### Adjusting Layout

To change article width, edit `static/css/style.css`:

```css
main {
  max-width: 800px;  /* Change this value */
  margin: 3rem auto;
  padding: 0 1.5rem;
}
```

### Adding Custom Sections

To add a sidebar or custom section, edit the relevant template in `blog/themes/volunteerclear/templates/`.

For example, to add a sidebar to articles, edit `article.html`:

```html
<div style="display: grid; grid-template-columns: 1fr 300px; gap: 2rem;">
  <article>
    <!-- existing article content -->
  </article>
  
  <aside>
    <h3>Related Posts</h3>
    <!-- sidebar content -->
  </aside>
</div>
```

## Best Practices

### Writing Blog Posts

1. **Use clear headings** - H2 for main sections, H3 for subsections
2. **Keep paragraphs short** - 3-4 sentences max
3. **Use lists** - Break up text with bullet points
4. **Add links** - Link to relevant main site pages
5. **Include CTAs** - End posts with calls to action

### Images

When adding images to posts:

1. Place images in `blog/content/images/`
2. Optimize images (compress, resize)
3. Use descriptive filenames
4. Always include alt text

```markdown
![Descriptive alt text](/images/your-image.jpg)
```

### Code Blocks

The theme supports syntax highlighting:

```markdown
```python
def hello_world():
    print("Hello, World!")
```
```

### Blockquotes

Use blockquotes for emphasis:

```markdown
> Important: Always verify volunteer clearances before allowing contact with children.
```

## Responsive Design

The theme is mobile-first and responsive:

### Mobile (< 768px)
- Single column layout
- Smaller font sizes
- Reduced padding
- Stacked navigation

### Desktop (≥ 768px)
- Wider content area
- Larger typography
- More whitespace
- Horizontal navigation

## Performance

The theme is optimized for speed:

- **CSS**: 8KB minified
- **No JavaScript**: Pure HTML/CSS
- **Font Loading**: Preconnect to Google Fonts
- **Images**: Lazy loading supported

## Accessibility

The theme follows accessibility best practices:

- Semantic HTML5 elements
- Proper heading hierarchy (H1 → H2 → H3)
- High contrast ratios (WCAG AA compliant)
- Keyboard navigation support
- Alt text for images
- ARIA labels where needed

## SEO Features

Built-in SEO optimization:

- Meta descriptions from article summaries
- Open Graph tags for social sharing
- Twitter Card support
- Semantic HTML structure
- Clean URLs
- Sitemap generation
- RSS/Atom feeds

## Testing

Before deploying theme changes:

1. **Build locally**: `cd blog && make html`
2. **Test in browser**: `make devserver` → http://localhost:8000
3. **Check responsive**: Test on mobile and desktop
4. **Validate HTML**: Use W3C validator
5. **Test links**: Ensure all navigation works
6. **Check performance**: Use Lighthouse

## Troubleshooting

### Theme not applying

**Problem**: Blog still shows default theme
**Solution**: 
1. Check `blog/pelicanconf.py` has `THEME = 'themes/volunteerclear'`
2. Run `make clean && make publish`
3. Verify `blog/output/theme/css/style.css` exists

### Styles look broken

**Problem**: CSS not loading
**Solution**:
1. Check browser console for 404 errors
2. Verify CSS file path in HTML
3. Clear browser cache
4. Rebuild: `make clean && make publish`

### Colors don't match

**Problem**: Blog colors different from main site
**Solution**:
1. Compare CSS variables in both projects
2. Update `blog/themes/volunteerclear/static/css/style.css`
3. Rebuild and test

## Support

For theme issues or questions:

1. Check `blog/themes/volunteerclear/README.md`
2. Review Pelican documentation: https://docs.getpelican.com/
3. Contact the development team

## Future Enhancements

Planned improvements:

- [ ] Dark mode support
- [ ] Search functionality
- [ ] Reading progress indicator
- [ ] Table of contents for long articles
- [ ] Related posts section
- [ ] Author bio cards
- [ ] Newsletter signup integration
- [ ] Comments system (Disqus/Commento)
