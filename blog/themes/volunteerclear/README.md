# VolunteerClear Blog Theme

A custom Pelican theme designed to match the VolunteerClear Vue application design.

## Features

- **Tailwind-inspired styling** - Uses the same color palette and design system as the main site
- **Inter font** - Matches the main site typography
- **Responsive design** - Mobile-first approach
- **Clean, modern layout** - Professional blog appearance
- **SEO optimized** - Proper meta tags and structured data
- **Accessible** - Semantic HTML and ARIA labels

## Design System

### Colors

The theme uses CSS custom properties matching the main site:

- **Primary**: Blue shades (#2563eb, #1d4ed8)
- **Gray**: Neutral shades for text and backgrounds
- **Backgrounds**: White with subtle gray accents

### Typography

- **Font Family**: Inter (with system font fallbacks)
- **Headings**: Bold, clear hierarchy
- **Body**: 1.0625rem (17px) for comfortable reading
- **Line Height**: 1.75 for body text

### Components

#### Header
- Blue gradient background matching main site
- Site title and subtitle
- Navigation menu with links back to main site

#### Articles
- Clean card-based layout
- Clear typography hierarchy
- Tag badges with rounded corners
- Read more buttons

#### Footer
- Dark background (gray-900)
- Multi-column layout
- Links to main site sections
- Social media links

## Customization

### Colors

Edit `static/css/style.css` and update the CSS custom properties:

```css
:root {
  --primary-600: #2563eb;  /* Your primary color */
  --primary-700: #1d4ed8;  /* Darker shade */
  /* ... */
}
```

### Fonts

The theme uses Inter from Google Fonts. To change:

1. Update the font link in `templates/base.html`
2. Update the font-family in `static/css/style.css`

### Layout

The theme uses a centered layout with max-width of 800px for articles. To adjust:

```css
main {
  max-width: 800px;  /* Change this */
  margin: 3rem auto;
  padding: 0 1.5rem;
}
```

## Templates

### Available Templates

- `base.html` - Base template with header, footer, and common elements
- `index.html` - Blog homepage with article list
- `article.html` - Individual article page
- `page.html` - Static page template
- `archives.html` - All posts chronologically
- `categories.html` - Category listing
- `category.html` - Posts in a category
- `tags.html` - Tag cloud
- `tag.html` - Posts with a tag
- `author.html` - Posts by author

### Template Variables

All standard Pelican variables are available. Key ones:

- `{{ SITENAME }}` - Site name
- `{{ SITESUBTITLE }}` - Site subtitle
- `{{ article.title }}` - Article title
- `{{ article.content }}` - Article content
- `{{ article.date }}` - Publication date
- `{{ article.author }}` - Author name
- `{{ article.tags }}` - Article tags
- `{{ article.category }}` - Article category

## Configuration

### Required Settings

In `pelicanconf.py`:

```python
THEME = 'themes/volunteerclear'
SITENAME = 'VolunteerClear Blog'
SITESUBTITLE = 'Insights on volunteer management, safety, and compliance'
```

### Recommended Settings

```python
# Menu items in header
MENUITEMS = (
    ('Archives', '/blog/archives.html'),
    ('Categories', '/blog/categories.html'),
    ('Tags', '/blog/tags.html'),
)

# Links in footer
LINKS = (
    ('Get Started', '/#contact'),
    ('Features', '/#features'),
    ('Pricing', '/#pricing'),
)

# Social links
SOCIAL = (
    ('Twitter', 'https://twitter.com/volunteerclear'),
    ('LinkedIn', 'https://linkedin.com/company/volunteerclear'),
)

# Display settings
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
```

## Responsive Breakpoints

The theme uses these breakpoints:

- **Mobile**: < 768px
- **Desktop**: ≥ 768px

Mobile adjustments:
- Smaller font sizes
- Reduced padding
- Stacked navigation

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

The theme is optimized for performance:

- Minimal CSS (8KB)
- No JavaScript required
- System fonts with Google Fonts fallback
- Efficient CSS selectors

## Accessibility

- Semantic HTML5 elements
- Proper heading hierarchy
- Alt text support for images
- Keyboard navigation friendly
- High contrast ratios

## Future Enhancements

Potential improvements:

- [ ] Dark mode toggle
- [ ] Search functionality
- [ ] Comments integration
- [ ] Reading time estimates
- [ ] Related posts
- [ ] Social sharing buttons
- [ ] Newsletter signup form

## License

This theme is part of the VolunteerClear project.
