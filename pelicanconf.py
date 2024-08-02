AUTHOR = 'Adam Sommer'
SITENAME = 'Appalachian FC'
SITEURL = "https://asommer70.github.io/appfc/"
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
# STYLESHEET_URL = '/static/css/site.css'
THEME = 'themes/appfc/'

PATH = "content"

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 12

# PAGE_URL = '{slug}'
# PAGE_SAVE_AS = '{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
