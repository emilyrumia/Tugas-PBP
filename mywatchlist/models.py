from django.db import models

# Create your models here.
class WatchList(models.Model):
    title_movie = models.TextField()
    release_date = models.CharField(max_length=800)
    rating_movie = models.CharField(max_length=4)
    review_movie = models.TextField()
    watched_status = models.CharField(max_length=200)

