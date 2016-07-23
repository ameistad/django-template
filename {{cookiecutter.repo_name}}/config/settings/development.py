# -*- coding: utf-8 -*-
# Development settings

from .base import *  # noqa

# Load environment files from file in development
env_file = join(dirname(__file__), 'development.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

DEBUG = True

# Django debug toolbar
INSTALLED_APPS += ('debug_toolbar', )

ALLOWED_HOSTS = []
