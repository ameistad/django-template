# Deploying to Dokku
This template was tested successfully on [Digital Ocean](https://digitalocean.com) with Dokku 0.4.5 on Ubuntu 14.04.    

First make sure you have a PostgreSQL plugin installed on your Dokku VPS
```sh
$ dokku plugin:install https://github.com/Kloadut/dokku-pg-plugin postgresql
```

Optional alias to run all commands client side.    
Add this to start up script, e.g .bash_profile or .bashrc.
```
alias dokku="ssh -t root@{{ cookiecutter.dokku_server }} dokku"
```

### Deploying to Dokku 
Git (Client side)
```sh
$ cd {{ cookiecutter.repo_name }}
$ git init && git add -A && git commit -m "First commit"
$ git remote add dokku dokku@{{ cookiecutter.dokku_server }}:{{ cookiecutter.repo_name }}
```

Create app, database and set environment variables (Server side)
```sh
$ dokku apps:create {{ cookiecutter.repo_name }}
$ dokku postgresql:create {{ cookiecutter.repo_name }}
$ dokku config:set {{ cookiecutter.repo_name }} DJANGO_SECRET_KEY=`openssl rand -base64 32`
$ dokku config:set {{ cookiecutter.repo_name }} DJANGO_SETTINGS_MODULE='config.settings.production'
$ dokku postgresql:link {{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}
```

Push repository to Dokku (Client side)
```sh
$ git push dokku master
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
