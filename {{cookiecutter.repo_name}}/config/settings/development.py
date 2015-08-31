# -*- coding: utf-8 -*-
# Local configuration

from .base import *  # noqa


DEBUG = True

# Django debug toolbar
INSTALLED_APPS += ('debug_toolbar', )

ALLOWED_HOSTS = []