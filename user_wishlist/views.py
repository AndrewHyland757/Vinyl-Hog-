from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from profiles.models import UserProfile
from products.models import Album
from .models import UserWishlist, WishlistItem


# Create your views here.


@login_required
def user_wishlist(request):
    ''' Renders wishlist page '''

    wishlist_items = None
    user = request.user
    #profile = get_object_or_404(UserProfile, user=request.user)

    #wishlist = UserWishlist.objects.filter(user=user).order_by('-created')


    if WishlistItem.objects.filter(user=user):

        wishlist_items = WishlistItem.objects.filter(user=user)
    
    context = {
        'wishlist': wishlist_items,
    }
    template = 'user_wishlist/user_wishlist.html'

    return render(request, template, context)


