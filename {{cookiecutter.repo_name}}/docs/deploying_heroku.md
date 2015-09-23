# Deploying to Heroku
Install [Heroku toolbelt](https://toolbelt.heroku.com/)  
All commands are run client side.

Git
```sh
$ cd {{ cookiecutter.repo_name }}
$ git init && git add -A && git commit -m "First commit"
```

Deploying the app
```sh
$ heroku create --buildpack https://github.com/heroku/heroku-buildpack-python --region eu {{ cookiecutter.repo_name }}
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32`
$ heroku config:set DJANGO_SETTINGS_MODULE='config.settings.production'
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku open
```
