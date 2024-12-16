from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    def __str__(self: 'Movie') -> str:
        return self.title
