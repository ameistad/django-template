"""
WSGI config for {{ cookiecutter.project_name }}.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)