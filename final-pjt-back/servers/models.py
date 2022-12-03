from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    id = models.IntegerField(primary_key=True)
    genre_ids = models.JSONField()
    adult = models.BooleanField()
    backdrop_path = models.TextField(null=True)
    original_language = models.TextField()
    popularity = models.IntegerField()
    poster_path = models.TextField(null=True)
    release_date = models.TextField()
    vote_average = models.FloatField()
    actors = models.JSONField(default=False)
    director = models.JSONField(null=True)
    # director =
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)
    content = models.CharField(max_length=50)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)


class SortedMovie(models.Model):
    title = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    genre_ids = models.JSONField()
    poster_path = models.TextField(null=True)
    release_date = models.TextField()
    actors = models.JSONField(default=False)