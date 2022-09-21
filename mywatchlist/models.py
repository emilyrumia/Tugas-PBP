from django.db import models

# Create your models here.
class WatchList(models.Model):
    title_movie = models.TextField()
    release_date = models.TextField()
    rating_movie = models.TextField()
    review_movie = models.TextField()
    watched_status = models.TextField()

