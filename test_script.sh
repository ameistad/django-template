cookiecutter . --no-input --overwrite-if-exists
pip install -r my_django_project/requirements/testing.txt
cd my_django_project/
py.test tests