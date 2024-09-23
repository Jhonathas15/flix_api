from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=[
        MinValueValidator(0, 'Avaliação não pode ser menor que 0.'),
        MaxValueValidator(5, 'Avalizção não pode ser maior que 5.'),
    ])
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.movie
