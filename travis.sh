rm -Rf my_django_project/
cookiecutter . --no-input
pip install -r my_django_project/requirements/testing.txt
cd my_django_project/
python manage.py migrate
python manage.py createsuperuser --username testuser --email testuser@example.com
py.test tests