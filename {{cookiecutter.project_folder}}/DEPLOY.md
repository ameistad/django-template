## Deploying to Dokku

### Git (Client side)
$ cd {{ cookiecutter.project_folder }}
$ git init
$ git add .
$ git commit -m "first commit"
$ git remote add dokku dokku@<server>:{{ cookiecutter.project_folder }}

### Installing PostgreSQL plugin (Server side)
$ cd /var/lib/dokku/plugins
$ git clone https://github.com/Kloadut/dokku-pg-plugin postgresql
$ dokku plugins-install

### Create app, database and set config (Server side)
$ dokku apps:create {{ cookiecutter.project_folder }}
$ dokku postgresql:create {{ cookiecutter.project_folder }}
$ dokku config:set {{ cookiecutter.project_folder }} DJANGO_SETTINGS_MODULE='config.settings.production'

### Push repository to Dokku (Client side)
$ git push dokku master

### Link database (Server side)
$ dokku postgresql:link {{ cookiecutter.project_folder }} {{ cookiecutter.project_folder }}

### Migrate and create super user (Server side)
$ dokku run {{ cookiecutter.project_folder }} python manage.py migrate
$ dokku run {{ cookiecutter.project_folder }} python manage.py createsuperuser

### Viewing logs on Dokku
$ docker ps
$ docker attach <CONTAINER ID>


## Deploying to Heroku (Client side)

### Git
$ cd {{ cookiecutter.project_folder }}
$ git init
$ git add .
$ git commit -m "first commit"

## Heroku
Install Heroku toolbelt - https://toolbelt.heroku.com/
$ heroku create --buildpack https://github.com/heroku/heroku-buildpack-python --region eu {{ cookiecutter.project_folder }}
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_SETTINGS_MODULE='config.settings.production'
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku open

