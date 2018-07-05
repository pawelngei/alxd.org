#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Pawel Ngei'
SITENAME = 'alxd'
SITETITLE = 'alxd'
SITESUBTITLE = u'hacker with a story to tell'

SITEURL = 'https://alxd.org'
SITELOGO = '/images/logo-circ.png'
# FAVICON = '/images/favicon.ico'

BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

MENUITEMS = (('Archives', '/archives.html'),)

SOCIAL = (
    ('envelope-o', 'mailto:alxd (AT) alxd.org'),
    ('github', 'https://github.com/pawelngei'),
    ('twitter', 'https://twitter.com/pawelngei'),
    ('linkedin', 'https://www.linkedin.com/in/pawel-ngei-19227983/'),
    ('rss', 'feeds/all.atom.xml'),
)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 5

TIMEZONE = 'Europe/Warsaw'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PATH = 'content'
STATIC_PATHS = ['images', 'slides', 'content/slides', 'scripts']

THEME = "themes/Flex"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['post_stats']

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 175

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
