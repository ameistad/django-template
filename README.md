# django-template  
[![Build Status](https://travis-ci.org/ameistad/amei-django-template.svg?branch=master)](https://travis-ci.org/ameistad/amei-django-template)
[![Requirements Status](https://requires.io/github/ameistad/amei-django-template/requirements.svg?branch=master)](https://requires.io/github/ameistad/amei-django-template/requirements/?branch=master)

My boilerplate for starting Django projects.

- Django 1.9 and Python 3.
- [Twelve-factor](http://12factor.net/) inpired environment variables with django-environ.
- PostgreSQL in development and production.
- Docker, Dokku or Heroku

## Install
Uses [Cookiecutter](https://github.com/audreyr/cookiecutter "Cookiecutter project") for installing.
```sh
$ pip install cookiecutter
$ cookiecutter https://github.com/ameistad/django-template.git
```

See docs/ in generated project folder for instructions on local development and deploying.