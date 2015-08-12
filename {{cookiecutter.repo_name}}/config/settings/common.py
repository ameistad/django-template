# -*- coding: utf-8 -*-
"""
Django settings for {{ cookiecutter.project_name }}.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

# Build paths inside the project like this: join(BASE_DIR, "directory")
from os.path import dirname, join


BASE_DIR = dirname(dirname(dirname(__file__)))

# Secret key
# https://docs.djangoproject.com/en/stable/ref/settings/#secret-key
# Todo: do something reasonable with this.
SECRET_KEY = 'CHANGE_THIS!'

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

# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC' # Europe/Oslo

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