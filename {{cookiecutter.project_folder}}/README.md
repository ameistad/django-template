# {{ cookiecutter.project_name }}
## {{ cookiecutter.description }}

# Local development
## Installing virtual environment
$ cd your_projects_dir
$ cd your_environments_dir
$ python3.4 -m venv project_name
$ source project_name/bin/activate

## Installing requirements 
$ cd {{ cookiecutter.project_folder }}
$ pip install -r requirements/local.txt
$ createdb {{ cookiecutter.project_folder }}

## Migrating database and starting development server
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver


See DEPLOY.md for instructions on how to deploy the site to Dokku and Heroku.
