# -*- coding: utf-8 -*-
# Production settings
# https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

from .base import *  # noqa


DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ('gunicorn', )

# Simplified static file serving with whitenoise.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
