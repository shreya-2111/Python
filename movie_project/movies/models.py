from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.name