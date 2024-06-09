
from django.conf import settings

from .models import WishlistItem


def wishlist_contents(request):

    wishlist_items = None
    user = request.user

    if user.is_authenticated and WishlistItem.objects.filter(user=user):
        wishlist_items = WishlistItem.objects.filter(user=user)

    context = {
        'wishlist_items': wishlist_items,
    }

    return context