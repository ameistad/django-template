# -*- coding: utf-8 -*-
# Testing settings
# https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

from .base import *  # noqa

# Load environment files from file in development
env_file = join(dirname(__file__), 'development.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

DEBUG = True

ALLOWED_HOSTS = []
