# -*- coding: utf-8 -*-
# Development settings

from .base import *  # noqa

DEBUG = True

# Django debug toolbar.
INSTALLED_APPS += ('debug_toolbar', )

ALLOWED_HOSTS = []

# Email backend that writes messages to console instead of sending them.
EMAIL_PORT = 1025
EMAIL_HOST = 'localhost'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
