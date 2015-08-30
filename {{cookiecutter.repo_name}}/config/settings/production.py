# -*- coding: utf-8 -*-
# Production settings
# https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

from .common import *  # noqa


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ('gunicorn', )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

