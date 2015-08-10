# dokku-django-template

A simple [Django](http://www.djangoproject.com/ "Django project") template for deploying to [Dokku](http://progrium.viewdocs.io/dokku/ "Dokku documentation").

This template is mostly for personal learning and proably does not use best practices.


- [Cookiecutter](https://github.com/audreyr/cookiecutter "Cookiecutter project") for installing
- PostgreSQL in development and production.
- Should deploy to both Dokku and Heroku.
- Whitenoise serving static files. 
- Django 1.8 and Python 3

## Template installation
```sh
$ pip install cookiecutter
$ cookiecutter https://github.com/ameistad/amei-django-template.git
```

See README.md and DEPLOY.md in generated project folder for instructions.