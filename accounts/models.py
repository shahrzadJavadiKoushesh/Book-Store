from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class CustomUser(AbstractUser):  # username, firstname, lastname, email, password, ... + age
    age = models.PositiveIntegerField(null=True, blank=True)
