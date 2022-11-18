from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    id = models.IntegerField(primary_key=True)
    genre_ids = models.JSONField()
    adult = models.BooleanField()
    backdrop_path = models.TextField()
    original_language = models.TextField()
    popularity = models.IntegerField()
    poster_path = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)
    content = models.CharField(max_length=50)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)