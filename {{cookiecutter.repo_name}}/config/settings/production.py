# -*- coding: utf-8 -*-
# Production settings
# https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ['*']

# Gunicorn WSGI HTTP Server.
INSTALLED_APPS += ('gunicorn', )

# Simplified static file serving with whitenoise.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Email
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='{{ cookiecutter.repo_name }} <noreply@{{ cookiecutter.domain_name }}>')

INSTALLED_APPS += ("anymail", )
ANYMAIL = {
    "MAILGUN_API_KEY": env('DJANGO_MAILGUN_API_KEY'),
}
EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"
