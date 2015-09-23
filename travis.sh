rm -Rf my_django_project/
cookiecutter . --no-input
pip install -r my_django_project/requirements/testing.txt
cd my_django_project/
py.test tests