from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='movie', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_name


class PeopleRating(models.Model):
    name = models.CharField(max_length=60)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='people')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
