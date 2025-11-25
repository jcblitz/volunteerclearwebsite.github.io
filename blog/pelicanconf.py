AUTHOR = 'VolunteerClear Team'
SITENAME = 'VolunteerClear Blog'
SITEURL = ''
SITESUBTITLE = 'Insights on volunteer management, safety, and compliance'

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu items (shown in header navigation)
MENUITEMS = (
    ('Archives', '/blog/archives.html'),
    ('Categories', '/blog/categories.html'),
    ('Tags', '/blog/tags.html'),
)

# Blogroll - Links shown in footer
LINKS = (
    ('Get Started', '/#contact'),
    ('Features', '/#features'),
    ('Pricing', '/#pricing'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/volunteerclear'),
    ('LinkedIn', 'https://linkedin.com/company/volunteerclear'),
)

# Display settings
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_PAGINATION = 10

# URL settings
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Theme settings
THEME = 'themes/volunteerclear'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']

# Plugins
PLUGIN_PATHS = []
PLUGINS = []

# Static paths
STATIC_PATHS = ['images', 'extra']

# Extra files
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Metadata
DEFAULT_METADATA = {
    'status': 'draft',
}

# Formatting for dates
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
