from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
   


class Condition(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Condition'

    def __str__(self):
        return str(self.name)


class Album(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")

    stock = models.IntegerField(
        default=1, validators=[MinValueValidator(0)])
    on_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField(null=True, blank=True)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
        

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=200)



    def __str__(self):
        return str(self.name)


