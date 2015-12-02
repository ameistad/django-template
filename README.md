# amei-django-template  
[![Build Status](https://travis-ci.org/ameistad/amei-django-template.svg?branch=master)](https://travis-ci.org/ameistad/amei-django-template)
[![Requirements Status](https://requires.io/github/ameistad/amei-django-template/requirements.svg?branch=master)](https://requires.io/github/ameistad/amei-django-template/requirements/?branch=master)

A simple [Django](http://www.djangoproject.com/ "Django project") template for deploying to [Dokku](http://progrium.viewdocs.io/dokku/ "Dokku documentation").


- [Cookiecutter](https://github.com/audreyr/cookiecutter "Cookiecutter project") for installing.
- Django 1.9 and Python 3.
- [Twelve-factor](http://12factor.net/) inpired environment variables with django-environ.
- PostgreSQL in development and production.
- Should deploy to both Dokku and Heroku.
- Whitenoise serving static files. 
- Detailed instructions for deploying to Dokku.

## Instructions
```sh
$ pip install cookiecutter
$ cookiecutter https://github.com/ameistad/dokku-django-template.git
```

See docs/ in generated project folder for instructions on local development and deploying.