# django-template
[![Build Status](https://travis-ci.org/ameistad/django-template.svg?branch=master)](https://travis-ci.org/ameistad/django-template)
[![Updates](https://pyup.io/repos/github/ameistad/django-template/shield.svg)](https://pyup.io/repos/github/ameistad/django-template/)
[![Python 3](https://pyup.io/repos/github/ameistad/django-template/python-3-shield.svg)](https://pyup.io/repos/github/ameistad/django-template/)

My boilerplate for starting Django projects.

- Django 1.11 and Python 3.
- PostgreSQL in development and production.
- Deploys with Docker and uses [Caddy](https://caddyserver.com/ "Caddy HTTP Server") as a proxy.
- Default settings gets A+ ratings on [Mozilla Observatory](https://observatory.mozilla.org).

## Install
Uses [Cookiecutter](https://github.com/audreyr/cookiecutter "Cookiecutter project") for installing.
```sh
$ pip install cookiecutter
$ cookiecutter https://github.com/ameistad/django-template.git
```

See docs/ in generated project folder for instructions.
