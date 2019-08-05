from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    point = models.IntegerField(default=0)
