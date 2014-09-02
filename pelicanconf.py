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

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# THEME = "notmyidea"
THEME = "themes/skin-alxd"

# PLUGINS = ['i18n_subtitles']

DISPLAY_PAGES_ON_MENU = True
MAX_POSTS_ON_MAIN = 5
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 175

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
