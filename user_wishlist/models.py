
from django.db import models
from django.contrib.auth.models import User

from products.models import Album
from profiles.models import UserProfile

# Create your models here.


class UserWishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)



class WishlistItem(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Album, null=False, blank=False, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.product)