# Deployment with Docker
This is an example how you would deploy the project to Digital Ocean with Docker.

### 1. Make sure settings are correct
- Check that the `.env` file is setyp correctly.
- Check that domain is correct in `docker-compose.yml`

### 2. Create Diffie-Hellman Parameters
This creates DH Parameters with a 2048 bit long safe prime. This defines OpenSSL performs the
Diffie-Hellman (DH) exchange and is used by letsencrypt.
```sh
$ openssl dhparam -out docker/nginx/dhparams.pem 2048
```

### 3. Create a Digital Ocean Docker droplet with a personal access token.
https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-api-v2
```sh
$ docker-machine create --driver digitalocean --digitalocean-region=ams2 --digitalocean-access-token=ACCESS_TOKEN {{ cookiecutter.repo_name }}
```

### 4. Check that the machine is running.
```sh
$ docker-machine ls
```

### 5. Load Docker environment into the shell and set {{ cookiecutter.repo_name }} as the active machine.
```sh
$ eval "$(docker-machine env  {{ cookiecutter.repo_name }})"
```

### 6. Build images as defined in docker-compose.yml.
```sh
$ docker-compose build
```

### 7. Start services in detached mode.
```sh
$ docker-compose up -d
```

### 8. Migrate and create superuser.
```sh
$ docker-compose run django python manage.py migrate
$ docker-compose run django python manage.py createsuperuser
```

### 9. Unset Docker environment variables when finished.
```sh
$ eval "$(docker-machine env -u)"
```

# Administrate docker-machine
### Check logs
```sh
$ docker-compose logs
```

### SSH into the machine
You might need to reset the root password on http://digitalocean.com
```sh
$ docker-machine ssh {{ cookiecutter.repo_name }}
``
