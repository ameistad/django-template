# Deploying on Digital Ocean

```sh
# Create a Digital Ocean Docker droplet with a personal access token.
# https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-api-v2
$ docker-machine create -d digitalocean --digitalocean-access-token=ACCESS_TOKEN {{ cookiecutter.repo_name }}

# Check that the machine is running.
$ docker-machine ls

# Load Docker environment into the shell and set {{ cookiecutter.repo_name }} as the active machine.
$ eval "$(docker-machine env  {{ cookiecutter.repo_name }})"

# Build images as defined in docker-compose.yml.
$ docker-compose build

# Start services in detached mode.
$ docker-compose up -d

# Unset Docker environment variables when finished.
$ eval "$(docker-machine env -u)"
```

