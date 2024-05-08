from django.db import models
from django.contrib.auth.models import User
from products.models import Album

# Create your models here.


class WishlistItem(models.Model):
    user = models.ForeignKey(User, null=False, blank=False,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Album, null=False, blank=False,
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)