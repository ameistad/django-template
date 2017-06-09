# -*- coding: utf-8 -*-
"""
Django settings for {{ cookiecutter.project_name }}.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import environ

# Django-environ for loading settings from environment variables.
env = environ.Env()

# Build paths inside the project like this: str(BASE_DIR.path('directory'))
BASE_DIR = environ.Path(__file__) - 3

# Secret key from environment variables
# https://docs.djangoproject.com/en/stable/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY', default='this_is_a_secret')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party app

    # Own apps
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR.path('templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
# Get databases from DATABASE_URL.
# https://django-environ.readthedocs.org/en/latest/
DATABASES = {
    'default': env.db('DATABASE_URL',
        default='postgres://{% if cookiecutter.windows == 'y' %}localhost{% endif %}/{{ cookiecutter.repo_name }}'),
}


# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'  # Example: Europe/Oslo

USE_I18N = False

USE_L10N = True

USE_TZ = True

# Managers
# https://docs.djangoproject.com/en/stable/ref/settings/#managers
ADMINS = (
    ("""{{ cookiecutter.author_name }}""", '{{ cookiecutter.email }}'),
)

MANAGERS = ADMINS

# Default admin url
ADMIN_URL = r'^admin/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(BASE_DIR.path('static')),
)

STATIC_ROOT = 'staticfiles'
