import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Production settings - use relative URLs for flexibility
SITEURL = ''
RELATIVE_URLS = True

# Feed settings for production (relative paths)
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TAG_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# Analytics
# GOOGLE_ANALYTICS = 'G-XXXXXXXXXX'  # Add your GA ID here
