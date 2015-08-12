# -*- coding: utf-8 -*-
# Production settings
# https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

from .common import *  # noqa
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ('gunicorn', )

# Get DATABASE_URL from environment variable
# https://github.com/kennethreitz/dj-database-url
DATABASES = {
    'default': dj_database_url.config()
}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

Todo
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST = os.environ['EMAIL_HOST']
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
# EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']

# SECRET_KEY = os.environ['SECRET_KEY']
