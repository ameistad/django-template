# -*- coding: utf-8 -*-
# Local configuration

from .common import *  # noqa


DEBUG = True

# Django debug toolbar
INSTALLED_APPS += ('debug_toolbar', )

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ cookiecutter.repo_name }}',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}