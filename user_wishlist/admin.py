from django.contrib import admin
from .models import UserWishlist, WishlistItem

# Register your models here.


admin.site.register(UserWishlist)
admin.site.register(WishlistItem)

