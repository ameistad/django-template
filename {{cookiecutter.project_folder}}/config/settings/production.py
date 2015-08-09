# -*- coding: utf-8 -*-
# Production settings
# https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

from .common import *  # noqa
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ('gunicorn', )

# Get DATABASE_URL from environment variable
# https://github.com/kennethreitz/dj-database-url
DATABASES = {'default': dj_database_url.config()}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
