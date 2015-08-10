# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}  
A Django project by {{ cookiecutter.author_name }} <{{ cookiecutter.email }}>

# Local development
Installing virtual environment
```sh
$ cd your_projects_dir
$ cd your_environments_dir
$ python3.4 -m venv project_name
$ source project_name/bin/activate
```

Installing requirements 
```sh
$ cd {{ cookiecutter.repo_name }}
$ pip install -r requirements/local.txt
```

PostgreSQL setup
```sh
$ createdb {{ cookiecutter.repo_name }}
```
Edit config/settings/local.py and set database USER and password.

Migrate and start development server
```sh
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```


### See DEPLOY.md for instructions on how to deploy the site to Dokku and Heroku.
