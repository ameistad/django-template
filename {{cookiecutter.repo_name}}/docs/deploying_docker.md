# Deploying on Digital Ocean

## Create a Digital Ocean Docker droplet with a personal access token.
https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-api-v2
```sh
$ docker-machine create --driver digitalocean --digitalocean-region=ams2 --digitalocean-access-token=ACCESS_TOKEN {{ cookiecutter.repo_name }}
```

## Check that the machine is running.
```sh
$ docker-machine ls
```

## Load Docker environment into the shell and set {{ cookiecutter.repo_name }} as the active machine.
```sh
$ eval "$(docker-machine env  {{ cookiecutter.repo_name }})"
```

## Build images as defined in docker-compose.yml.
```sh
$ docker-compose build
```

## Start services in detached mode.
```sh
$ docker-compose up -d
```

## Migrate and create superuser.
```sh
$ docker-compose run django migrate
$ docker-compose run django createsuperuser
```

## Unset Docker environment variables when finished.
```sh
$ eval "$(docker-machine env -u)"
```