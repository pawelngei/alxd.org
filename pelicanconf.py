#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = "Pawel Ngei"
SITENAME = "alxd - solarpunk hacker"
SITETITLE = "alxd"
SITESUBTITLE = "solarpunk | hacker"

# SITEURL = 'https://alxd.org'
SITEURL = "localhost:8000"
SITELOGO = "images/logo-circ.png"
FAVICON = "images/favicon.ico"

BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
USE_GOOGLE_FONTS = False

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Solarpunk Prompts", "https://podcast.tomasino.org/@SolarpunkPrompts"),
    ("Glider Ink", "https://glider.ink/"),
    ("solarpunk.pl", "https://solarpunk.pl/"),
)

SOCIAL = (
    ("envelope", "mailto:alxd@alxd_PLEASE_DELETE_THIS_CAPTION_.org"),
    ("mastodon", "https://writing.exchange/@alxd"),
    ("github", "https://github.com/pawelngei"),
    ("linkedin", "https://www.linkedin.com/in/paul-ngei-19227983"),
    ("rss", "feeds/all.atom.xml"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
    "local_icons": True,
}

COPYRIGHT_YEAR = datetime.now().year

TIMEZONE = "Europe/Warsaw"

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PATH = "content"
STATIC_PATHS = ["images", "slides", "content/slides", "scripts"]

THEME = "themes/Flex"

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["post_stats"]

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 175

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
