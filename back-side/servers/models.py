from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    genre_ids = models.JSONField()
    adult = models.BooleanField()
    backdrop_path = models.TextField()
    original_language = models.TextField()
    popularity = models.IntegerField()
    poster_path = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()

