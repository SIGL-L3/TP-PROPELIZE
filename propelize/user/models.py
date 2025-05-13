from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)

    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username
