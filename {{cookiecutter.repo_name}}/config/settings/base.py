# -*- coding: utf-8 -*-
"""
Django settings for {{ cookiecutter.project_name }}.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

from os.path import dirname, join, exists
import environ

# Django-environ for using 12-factor environment variables.
# http://12factor.net/)
env = environ.Env()

# .env file to store environment variables.
env_file = join(dirname(__file__), 'development.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))

# Secret key from environment variables
# https://docs.djangoproject.com/en/stable/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party app

    # Own apps
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
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
    'default': env.db(),
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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [join(BASE_DIR, 'static')]

STATIC_ROOT = 'staticfiles'
