from django.db import models
from django.contrib.auth.models import AbstractUser
from servers.models import Movie
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50, null= True)
    point = models.IntegerField(default=0)
    # like_movies = models.ManyToManyField(Movie)
