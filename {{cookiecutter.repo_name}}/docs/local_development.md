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
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

# Gulp for Sass compiling.
Make sure [Node.js](https://nodejs.org/en/) is installed. 

Install Gulp globally
```sh
$ npm install -g gulp

Install dependencies as defined in package.json to {{ cookiecutter.repo_name}}/node_modules/
```sh
$ npm install
```

Run Gulp
```sh
$ gulp
```sh
