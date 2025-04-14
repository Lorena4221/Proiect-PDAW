from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    hours = models.JSONField(default=list)

    def __str__(self):
        return self.title
# Create your models here.
