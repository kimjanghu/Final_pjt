from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Review

# Create your models here.
class User(AbstractUser):
    pass