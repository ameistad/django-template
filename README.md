# dokku-django-template  
[![Build Status](https://travis-ci.org/ameistad/dokku-django-template.svg?branch=master)](https://travis-ci.org/ameistad/dokku-django-template)
[![Requirements Status](https://requires.io/github/ameistad/dokku-django-template/requirements.svg?branch=master)](https://requires.io/github/ameistad/dokku-django-template/requirements/?branch=master)

A simple [Django](http://www.djangoproject.com/ "Django project") template for deploying to [Dokku](http://progrium.viewdocs.io/dokku/ "Dokku documentation").


- [Cookiecutter](https://github.com/audreyr/cookiecutter "Cookiecutter project") for installing.
- Django 1.8 and Python 3.
- Django-environ for 12 factor inspired environment variables.
- PostgreSQL in development and production.
- Should deploy to both Dokku and Heroku.
- Whitenoise serving static files. 

## Template installation
```sh
$ pip install cookiecutter
$ cookiecutter https://github.com/ameistad/dokku-django-template.git
```

See README.md and DEPLOY.md in generated project folder for instructions.