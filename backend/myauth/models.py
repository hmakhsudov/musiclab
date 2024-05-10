from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    favorite_genres = models.ManyToManyField('testsapp.Genre', related_name='users', blank=True)

    def __str__(self):
        return self.username
