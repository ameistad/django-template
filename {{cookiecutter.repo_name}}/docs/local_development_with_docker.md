# Local development with Docker

## Install Docker
[Docker for Mac](https://docs.docker.com/docker-for-mac/)
[Docker for Windows](https://docs.docker.com/docker-for-windows/)

## Build and start containers
__Build docker containers__
```sh
$ docker-compose -f docker-dev build
```

__Set up Django__
```sh
$ docker-compose -f docker-dev.yml run django python manage.py migrate
$ docker-compose -f docker-dev.yml run django python manage.py createsuperuser
```

__Start containers__
```sh
$ docker-compose up
```
