# amei-django-template  
[![Build Status](https://travis-ci.org/ameistad/amei-django-template.svg?branch=master)](https://travis-ci.org/ameistad/amei-django-template)
[![Requirements Status](https://requires.io/github/ameistad/amei-django-template/requirements.svg?branch=master)](https://requires.io/github/ameistad/amei-django-template/requirements/?branch=master)

A simple [Django](http://www.djangoproject.com/ "Django project") template for deploying to [Dokku](http://progrium.viewdocs.io/dokku/ "Dokku documentation").


- [Cookiecutter](https://github.com/audreyr/cookiecutter "Cookiecutter project") for installing.
- Django 1.8 and Python 3.
- Django-environ for 12 factor inspired environment variables.
- PostgreSQL in development and production.
- Should deploy to both Dokku and Heroku.
- Whitenoise serving static files. 
- Detailed instructions for deployng to Dokku.

## Template installation
```sh
$ pip install cookiecutter
$ cookiecutter https://github.com/ameistad/dokku-django-template.git
```

See docs/ in generated project folder for instructions.