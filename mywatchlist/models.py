from unittest.mock import DEFAULT
from django.db import models

DEFAULT = 0

# Create your models here.
class WatchList(models.Model):
    title_movie = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    rating_movie = models.CharField(max_length=255)
    review_movie = models.TextField()
    watched_status = models.CharField(max_length=255)

