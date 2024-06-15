from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Album
from .models import WishlistItem

# Create your views here.


@login_required
def wishlist_items(request):
    '''
    Renders wishlist page with list of items user has saved.
    '''
   
    wishlist_items = None
    
    if request.user:
        if WishlistItem.objects.filter(user=request.user):
            wishlist_items = WishlistItem.objects.filter(user=request.user)

    template = 'wishlist_items/wishlist_items.html'
    context = {
            "wishlist_items": wishlist_items,
        }

    return render(request, template)


@login_required
def add_wishlist_item(request, product_id):
    """
    Creates an instance in the WishlistItem model by
    assigning a user to the selected product.
    """
   
    product = get_object_or_404(Album, pk=product_id)
    user = request.user

    if WishlistItem.objects.filter(user=user, product=product).exists():
        messages.info(request, f'{product.title} is already on your wishlist!')
    else:
        WishlistItem.objects.create(user=user, product=product)
        messages.add_message(request, 27, " added to your wishlist!")
        
    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)


def delete_wishlist_item(request, product_id):
    '''
    Function to delete an wishlist item assigned to a user.
    '''
    instance = None
    user = request.user
    wishlist = WishlistItem.objects.filter(user=user)
    product = get_object_or_404(Album, id=product_id)

    for item in wishlist:
        if item.product == product:
            instance = item
            instance.delete()
            wishlist = WishlistItem.objects.filter(user=user)
            messages.success(request, f'"{product.title}" removed your wishlist!')

    redirect_url = 'wishlist-items'

    return redirect(redirect_url)