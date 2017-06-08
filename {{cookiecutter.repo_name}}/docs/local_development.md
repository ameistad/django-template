# Local development
PostgreSQL neees to be installed.
For Mac OS X [Postgres.app](http://postgresapp.com/) is recommended.

Install virtual environment.
```sh
$ cd your_projects_dir
$ cd your_environments_dir
$ python3 -m venv {{ cookiecutter.project_name }}
$ source {{ cookiecutter.project_name }}/bin/activate
```

Install requirements.
```sh
$ cd {{ cookiecutter.project_name }}
$ pip install -r requirements/development.txt
```

# Create a new database with PostgreSQL.
# Postgres.app recommended on macOS.
```sh
$ createdb {{ cookiecutter.project_name }}
```

Migrate and start development server.
```sh
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
