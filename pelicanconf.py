#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pawel Chojnacki'
SITENAME = u'alxd'
SITESUBTITLE = u'open source transhumanist'
SITEURL = 'http://alxd.org'
IMAGE_PATH = 'images/logo-circ.png'


PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
# MENU = (
#           ('Facebook', 'https://www.facebook.com/chojnackipawel91'),
#           ('Diaspora*', 'https://joindiaspora.com/u/chojnacki'),
#           ('email', 'mailto:alxd (AT) alxd.org'),
#         )

THEME = "themes/skin-alxd"
# THEME = "themes/alxd.org"

DISPLAY_PAGES_ON_MENU = True
MAX_POSTS_ON_MAIN = 5
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 175

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
