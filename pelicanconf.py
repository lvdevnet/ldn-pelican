#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'luch'
SITENAME = u'LDN Pelican'
SITEURL = 'http://soulne4ny.github.com/ldn-pelican'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Blogroll
LINKS = (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
)

# Social widget
SOCIAL = (
    ('meetup', 'http://www.meetup.com/Latvian-Developers-Network/'),
)

DEFAULT_PAGINATION = 3

STATIC_PATHS = ['images']

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
