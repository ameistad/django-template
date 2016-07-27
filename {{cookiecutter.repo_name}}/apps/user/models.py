from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse


class User(AbstractUser):

    name = models.CharField('Name', blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
