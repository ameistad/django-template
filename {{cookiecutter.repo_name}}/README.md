# {{ cookiecutter.project_name }}  
{{ cookiecutter.author_name }} <{{ cookiecutter.email }}>

### Local development quick start
Installing virtual environment
```sh
$ cd your_projects_dir
$ cd your_environments_dir
$ python3.4 -m venv {{ cookiecutter.repo_name }}
$ source {{ cookiecutter.repo_name }}/bin/activate
```

Installing requirements and create PostgreSQL database
```sh
$ cd {{ cookiecutter.repo_name }}
$ pip install -r requirements/local.txt
$ createdb {{ cookiecutter.repo_name }}
```

Migrate and start development server
```sh
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```


### See DEPLOY.md for instructions on how to deploy the site to Dokku and Heroku.
