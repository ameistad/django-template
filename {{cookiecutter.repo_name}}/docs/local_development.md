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

Install requirements and create a database.
```sh
$ cd {{ cookiecutter.project_name }}
$ pip install -r requirements/development.txt
$ createdb gulpsetup
```

Migrate and start development server.
```sh
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

# Gulp
Make sure [Node.js](https://nodejs.org/en/) is installed. 

Install Gulp globally and dependencies.
```sh
$ npm install -g gulp
$ npm install
```

Run Gulp
```sh
$ gulp
```sh
