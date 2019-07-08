#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kael'
SITENAME = u'The Gay Movie Catalog'
SITEURL = 'https://thegaymoviecatalog.netlify.com/'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'C'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

###Custom Settings###
USE_FOLDER_AS_CATEGORY = True
SLUGIFY_SOURCE = 'title'
THEME = 'themes/gay-catalog'
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
ARTICLE_URL = '{category}/{slug}/'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DEFAULT_DATE_FORMAT= ('%d %b %Y')
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
DEFAULT_DATE= 'fs'
MARKDOWN = {
  'extension_configs': {
    'pyembed.markdown': {}
  }
}
PAGE_EXCLUDES = ['admin']
ARTICLE_EXCLUDES = ['admin']
#STATIC_PATHS = ['admin']
TEMPLATE_PAGES = {'admin/index.html': 'admin/index.html'}
STATIC_PATHS = ['uploads', 'admin']
CMS_ENV = "development"

DEFAULT_PAGINATION = 12
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
#CATEGORYS_URL = 'categories/'
#CATEGORYS_SAVE_AS = 'categories/index.html'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'