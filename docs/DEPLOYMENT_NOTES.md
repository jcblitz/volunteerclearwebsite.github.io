# Deployment Notes

## Project Structure

This project consists of two parts:

1. **Vue SPA** (main marketing site) - Single-page application at `/`
2. **Pelican Blog** (static blog) - Static HTML blog at `/blog/`

## How It Works

### Navigation

The main site navigation includes a "Blog" link that:
- Uses a regular `<a href="/blog/">` tag
- Does NOT prevent default behavior (unlike other nav links)
- Causes a full page navigation to the blog

### Blog Navigation

The blog includes links back to the main site:
- "← Back to VolunteerClear" → `/`
- "Get Started" → `/#contact`
- "Features" → `/#features`
- "Pricing" → `/#pricing`

These work because both sites use relative URLs.

## Building

### Development

```bash
# Build everything
npm run build

# Preview locally
npm run preview
```

Then visit:
- Main site: http://localhost:4173/
- Blog: http://localhost:4173/blog/

### Production

```bash
npm run build
```

This will:
1. Build the Vue app → `dist/`
2. Build the Pelican blog → `blog/output/`
3. Copy blog to → `dist/blog/`

Deploy the entire `dist/` folder.

## Deployment Checklist

- [ ] Run `npm run build`
- [ ] Verify `dist/index.html` exists (main site)
- [ ] Verify `dist/blog/index.html` exists (blog)
- [ ] Test navigation between main site and blog
- [ ] Deploy entire `dist/` folder to hosting

## Server Configuration

### GitHub Pages

No special configuration needed. The default setup works.

### Netlify / Vercel

No special configuration needed. Deploy `dist/` folder.

### Custom Server (Nginx/Apache)

Ensure your server:
1. Serves `dist/` as the web root
2. Serves static files from `dist/blog/`
3. Falls back to `index.html` for SPA routes (main site only)

Example Nginx config:

```nginx
server {
    listen 80;
    server_name www.volunteerclear.com;
    root /var/www/volunteerclear/dist;
    
    # Blog - serve static files
    location /blog/ {
        try_files $uri $uri/ =404;
    }
    
    # Main site - SPA fallback
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

## Troubleshooting

### Blog link goes to top of page

**Problem**: Clicking "Blog" scrolls to top instead of navigating
**Solution**: Ensure the link doesn't have `@click.prevent` - it should allow default navigation

### Blog shows 404

**Problem**: `/blog/` returns 404
**Solution**: 
- Verify `dist/blog/index.html` exists after build
- Check server configuration allows serving static files from `/blog/`

### Blog links back to main site don't work

**Problem**: Clicking "Back to VolunteerClear" doesn't work
**Solution**: Links use relative URLs (`/`) which should work. Check browser console for errors.

### Styles look different between main site and blog

**Expected**: The blog uses Pelican's default theme, which looks different from the Vue app. This is normal. To match styles, you'd need to create a custom Pelican theme.

## Future Improvements

### Custom Theme

The blog uses a custom theme (`blog/themes/volunteerclear/`) that matches the main site:

- Same color palette (blue primary, gray neutrals)
- Inter font family
- Similar header with blue gradient
- Responsive design
- Clean, modern layout

To customize the theme, see `blog/themes/volunteerclear/README.md`

### Add Blog to Main Site Navigation Highlight

Currently, the blog link doesn't highlight when you're on the blog. To fix:

1. Add a check in NavigationBar.vue to detect if current URL is `/blog/`
2. Apply active styles to the Blog link

### Shared Analytics

Both sites should use the same Google Analytics ID. Update:
- Main site: Already configured in `index.html`
- Blog: Add to `blog/publishconf.py`: `GOOGLE_ANALYTICS = 'G-XXXXXXXXXX'`

## Questions?

See:
- `BLOG_SETUP.md` - Blog setup and usage
- `blog/README.md` - Detailed blog documentation
- `SEO_CHECKLIST.md` - SEO optimization tasks
