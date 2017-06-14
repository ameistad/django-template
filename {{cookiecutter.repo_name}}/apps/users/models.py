from django.contrib.auth.models import AbstractUser


# Overriding the user model is recommended so you can customize it in the future.
# https://docs.djangoproject.com/en/stable/topics/auth/customizing/#auth-custom-user
class User(AbstractUser):
    pass
