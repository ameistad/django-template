# -*- coding: utf-8 -*-
# Development settings

from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = []

# Development specific django packages.
INSTALLED_APPS += ('django_extensions', )

# Email backend that writes messages to console instead of sending them.
EMAIL_PORT = 1025
EMAIL_HOST = 'localhost'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
