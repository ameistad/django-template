## Deploying to Dokku
Template is tested on Digital Ocean with Dokku 0.3.22 on Ubuntu 14.04  
Sign up to Digital Ocean with my [referral link](https://www.digitalocean.com/?refcode=22eaf729706a) to get $10 credit.


Optional alias to run all commands except postgresql install on the client side.
Add this to start up script e.g .bash_profile or .bashrc.
```
alias dokku="ssh -t root@<server> dokku"
```

Git (Client side)
```sh
$ cd {{ cookiecutter.repo_name }}
$ git init && git add -A && git commit -m "First commit"
$ git remote add dokku dokku@<server>:{{ cookiecutter.repo_name }}
```

Installing PostgreSQL plugin (Server side)
```sh
$ cd /var/lib/dokku/plugins
$ git clone https://github.com/Kloadut/dokku-pg-plugin postgresql
$ dokku plugins-install
```

Create app, database and set config (Server side)
```sh
$ dokku apps:create {{ cookiecutter.repo_name }}
$ dokku postgresql:create {{ cookiecutter.repo_name }}
$ dokku config:set {{ cookiecutter.repo_name }} DJANGO_SETTINGS_MODULE='config.settings.production'
```

Push repository to Dokku (Client side)
```sh
$ git push dokku master
```

Link database (Server side)
```sh
$ dokku postgresql:link {{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}
```

Migrate and create super user (Server side)
```sh
$ dokku run {{ cookiecutter.repo_name }} python manage.py migrate
$ dokku run {{ cookiecutter.repo_name }} python manage.py createsuperuser
```

Viewing logs on Dokku (Server side)
```sh
$ docker ps
$ docker attach <CONTAINER ID>
```


## Deploying to Heroku (Client side)
Install [Heroku toolbelt](https://toolbelt.heroku.com/)

Git
```sh
$ cd {{ cookiecutter.repo_name }}
$ git init && git add -A && git commit -m "First commit"
```

Installing the app
```sh
$ heroku create --buildpack https://github.com/heroku/heroku-buildpack-python --region eu {{ cookiecutter.repo_name }}
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_SETTINGS_MODULE='config.settings.production'
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku open
```
