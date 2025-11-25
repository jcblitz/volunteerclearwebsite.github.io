# VolunteerClear Blog

This directory contains the Pelican-powered blog for VolunteerClear.

## Setup

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

### Directory Structure

```
blog/
├── content/              # Blog posts and pages (Markdown)
│   ├── images/          # Images for blog posts
│   └── extra/           # Extra files (robots.txt, etc.)
├── output/              # Generated static site (gitignored)
├── pelicanconf.py       # Development configuration
├── publishconf.py       # Production configuration
├── requirements.txt     # Python dependencies
├── Makefile            # Build commands
└── README.md           # This file
```

## Writing Blog Posts

### Create a New Post

Create a new Markdown file in `content/`:

```markdown
Title: Your Post Title
Date: 2025-11-24 10:00
Category: Category Name
Tags: tag1, tag2, tag3
Slug: url-friendly-slug
Author: Author Name
Summary: Brief summary for listings and SEO
Status: published

Your content here...
```

### Post Metadata

- **Title**: Post title (required)
- **Date**: Publication date and time (required)
- **Category**: Single category for organization
- **Tags**: Comma-separated tags for topics
- **Slug**: URL-friendly identifier (becomes the URL)
- **Author**: Author name
- **Summary**: Brief description (used in listings and meta tags)
- **Status**: `published` or `draft`

### Categories

Current categories:
- Announcements
- Best Practices
- Tips & Guides
- Case Studies
- Product Updates

### Tags

Use relevant tags like:
- volunteer-management
- background-checks
- compliance
- safety
- nonprofit
- volunteer-screening

## Building the Blog

### Development Build

Generate the site for local testing:

```bash
make html
```

Output will be in `output/` directory.

### Development Server

Run a local server with auto-reload:

```bash
make devserver
```

Visit http://localhost:8000 to preview.

Press Ctrl+C to stop the server.

### Production Build

Generate the site for deployment:

```bash
make publish
```

This uses production settings from `publishconf.py`.

### Clean Build

Remove generated files:

```bash
make clean
```

## Deployment

### Integrated Deployment (Recommended)

The blog automatically deploys with your main site:

```bash
npm run build
```

This command:
1. Builds your Vue app
2. Builds the Pelican blog with `make publish`
3. Copies blog output to `dist/blog/`
4. Everything is ready for deployment

The blog uses relative URLs, so it works seamlessly in both development and production.

### Manual Deployment

If you need to build the blog separately:

```bash
cd blog
make publish
```

Output will be in `blog/output/`

### GitHub Actions Integration

Add to your `.github/workflows/deploy.yml`:

```yaml
- name: Setup Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'

- name: Install Pelican
  run: |
    cd blog
    pip install -r requirements.txt

- name: Build Blog
  run: |
    cd blog
    make publish

- name: Copy Blog to Dist
  run: |
    mkdir -p dist/blog
    cp -r blog/output/* dist/blog/
```

## Customization

### Theme

The default theme is simple. To customize:

1. Download a Pelican theme or create your own
2. Place it in `blog/themes/`
3. Update `pelicanconf.py`:
   ```python
   THEME = 'themes/your-theme-name'
   ```

Popular themes:
- [Pelican Themes Repository](https://github.com/getpelican/pelican-themes)
- Flex (modern, responsive)
- Elegant (feature-rich)
- Bootstrap (clean, simple)

### Styling to Match Main Site

To match your Vue app's styling:

1. Create a custom theme based on your Tailwind CSS
2. Copy your color scheme and fonts
3. Use the same header/footer components
4. Ensure consistent navigation

### Adding Features

Install Pelican plugins for additional features:

```bash
pip install pelican-plugins
```

Popular plugins:
- `sitemap` - Generate XML sitemap
- `seo` - Enhanced SEO features
- `related_posts` - Show related articles
- `read_time` - Calculate reading time
- `search` - Add search functionality

## SEO Optimization

### Already Configured

- Clean URLs (no .html extensions)
- Semantic HTML structure
- RSS/Atom feeds
- robots.txt
- Sitemap generation

### To Add

1. **Open Graph images**: Add featured images to posts
2. **Schema markup**: Add Article schema to theme
3. **Internal linking**: Link between related posts
4. **Meta descriptions**: Use Summary field effectively

## Content Strategy

### Recommended Posting Schedule

- 1-2 posts per week during early access
- Mix of educational and promotional content
- Respond to common customer questions

### Content Ideas

1. **Educational**:
   - Background check requirements by state
   - Volunteer retention strategies
   - Compliance checklists
   - Safety protocols

2. **Product Updates**:
   - New features
   - Customer success stories
   - Tips for using VolunteerClear

3. **Industry News**:
   - Regulatory changes
   - Best practices
   - Trends in volunteer management

## Maintenance

### Regular Tasks

- [ ] Write and publish new posts weekly
- [ ] Update old posts with new information
- [ ] Check for broken links monthly
- [ ] Review analytics to see popular topics
- [ ] Respond to comments (if enabled)
- [ ] Update categories/tags as needed

### Monitoring

Track these metrics:
- Page views per post
- Time on page
- Bounce rate
- Conversion to sign-ups
- Search rankings for target keywords

## Troubleshooting

### Build Errors

**Error**: `ModuleNotFoundError: No module named 'pelican'`
**Solution**: Install dependencies: `pip3 install -r requirements.txt`

**Error**: `WARNING: No valid files found in content`
**Solution**: Ensure posts have `Status: published` in metadata

**Warning**: `Feeds generated without SITEURL set properly may not be valid`
**Solution**: This is expected when using relative URLs. The feeds will still work correctly. You can ignore this warning.

### Styling Issues

**Problem**: Blog looks different from main site
**Solution**: Create custom theme matching your Tailwind CSS design

### URL Issues

**Problem**: Links not working after deployment
**Solution**: Check `SITEURL` in `publishconf.py` matches your domain

## Resources

- [Pelican Documentation](https://docs.getpelican.com/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Pelican Themes](https://github.com/getpelican/pelican-themes)
- [Pelican Plugins](https://github.com/pelican-plugins)

## Support

Questions about the blog setup? [Contact the team](https://www.volunteerclear.com/#contact)
