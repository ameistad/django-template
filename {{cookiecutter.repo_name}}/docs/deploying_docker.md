# Deployment with Docker
This is an example how you could deploy the project to Digital Ocean with Docker.

__Make sure settings are correct__
- Check that the `.env` file is setyp correctly.
- Check that domain is correct in `docker-compose.yml`

__Diffie-Hellman Parameters__
This creates DH Parameters with a 2048 bit long safe prime.
```sh
$ openssl dhparam -out docker/nginx/dhparams.pem 2048
```

__Create a Digital Ocean Docker droplet with a personal access token.__
https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-api-v2
```sh
$ docker-machine create --driver digitalocean --digitalocean-region=ams2 --digitalocean-access-token=ACCESS_TOKEN {{ cookiecutter.repo_name }}
```

__Check that the machine is running.__
```sh
$ docker-machine ls
```

__Load Docker environment into the shell and set {{ cookiecutter.repo_name }} as the active machine.__
```sh
$ eval "$(docker-machine env  {{ cookiecutter.repo_name }})"
```
Make sure the result of `docker-machine active` returns {{ cookiecutter.repo_name }}

__Build images as defined in docker-compose.yml.__
```sh
$ docker-compose build
```

__Start services in detached mode.__
```sh
$ docker-compose up -d
```

__Migrate and create superuser.__
```sh
$ docker-compose run django python manage.py migrate
$ docker-compose run django python manage.py createsuperuser
```

__Unset Docker environment variables when finished.__
```sh
$ eval "$(docker-machine env -u)"
```

# Administrate the remote docker-machine
__Check logs__
```sh
$ docker-compose logs
```

__SSH into the machine__
You might need to reset the root password on http://digitalocean.com
```sh
$ docker-machine ssh {{ cookiecutter.repo_name }}
``
