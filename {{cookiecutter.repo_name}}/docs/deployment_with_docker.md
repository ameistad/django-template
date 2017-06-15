# Deployment with Docker
This is an example how you could deploy the project to Digital Ocean with Docker.

__Make sure settings are correct__

* Change POSTGRES_USER, POSTGRES_PASSWORD and SECRET_KEY in `.env`.

* Check that domain is correct in `docker-compose.yml`.

__Create a Digital Ocean Docker droplet with a personal access token.__
[Get Digital Ocean access token](https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-api-v2)
[Docker Digital Ocean driver](https://docs.docker.com/machine/drivers/digital-ocean/)
```sh
$ docker-machine create --driver digitalocean --digitalocean-region=ams2 --digitalocean-access-token=ACCESS_TOKEN {{ cookiecutter.repo_name }}
```

__Check that the machine is running.__
```sh
$ docker-machine ls
```

__Set domain record__
Make sure {{ cookiecutter.domain_name }} points to your new docker-machine.

__Load Docker environment into the shell and set {{ cookiecutter.repo_name }} as the active machine.__
```sh
$ eval "$(docker-machine env {{ cookiecutter.repo_name }})"
```

Make sure the result of `docker-machine active` returns {{ cookiecutter.repo_name }}

__Build images as defined in docker-compose.yml.__
```sh
$ docker-compose build
```
__Migrate and create superuser.__
```sh
$ docker-compose run django python manage.py migrate
$ docker-compose run django python manage.py createsuperuser
```

__Start services in detached mode.__
```sh
$ docker-compose up -d
```

__Unset Docker environment variables when finished.__
```sh
$ eval "$(docker-machine env -u)"
```

## Administrate the remote docker-machine
__Check logs__
```sh
$ docker-compose logs
```

__SSH into the machine__
You might need to reset the root password on http://digitalocean.com
```sh
$ docker-machine ssh {{ cookiecutter.repo_name }}
```
