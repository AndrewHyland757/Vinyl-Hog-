from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Album(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    stock = models.IntegerField(
        default=1, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
