
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):

    def create_user(self, name, password=None):
        if not name:
            raise ValueError("L'utilisateur doit avoir une nom")

        user = self.model(name=name)

        if len(password)>=8:
            user.set_password(password)
        else:
            raise ValueError("Le mot de passer doit avoir au moins 8 caracteres")

        user.save(using=self._db)

        return user

    def create_superuser(self, name, password=None):
        user = self.create_user(name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return str(self.name)