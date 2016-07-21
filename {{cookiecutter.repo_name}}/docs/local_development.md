# Local development
PostgreSQL neees to be installed. 
For Mac OS X [Postgres.app](http://postgresapp.com/) is recommended.

Install virtual environment.
```sh
$ cd your_projects_dir
$ cd your_environments_dir
$ python3 -m venv gulpsetup
$ source gulpsetup/bin/activate
```

Install requirements and create a database.
```sh
$ cd gulpsetup
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

Install Gulp globally and install dependencies.
```sh
$ npm install -g gulp
$ npm install --save-dev
```

Run Gulp
```sh
$ gulp
```sh
