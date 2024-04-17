from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from products.models import Album
from django.contrib import messages

# Create your views here.

def basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')

"""
def add_basket(request, product_id): # ID passed in form action URL
   
    quantity = int(request.POST.get('quantity')) # From form
    redirect_url = request.POST.get('redirect_url')  # From form
    basket = request.session.get('basket', {}) # Get session or new
    product = get_object_or_404(Album, id=product_id)  #pk=item_id

    if product_id in list(basket.keys()):
        basket[product_id] += quantity # Add more of these objects to the list in basket
        
    else:
        basket[product_id] = quantity

    

    request.session['basket'] = basket # Make the updated or newly created basket the basket
    print(basket)
    return redirect(redirect_url)
"""

def add_basket(request, product_id): # ID passed in form action URL
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity')) # From form
    redirect_url = request.POST.get('redirect_url')  # From form
    basket = request.session.get('basket', {}) # Get session or create new
    product = get_object_or_404(Album, id=product_id)  # Identify product from model

    if quantity <= product.stock:
        if product_id in list(basket.keys()):
            total_quantity = int(basket[product_id]) + quantity # Add quantity in form to existing quantity(amount of product on basket list)
            if total_quantity <= product.stock:
                basket[product_id] = int(basket[product_id]) + quantity
                messages.success(
                    request, f'{product.title} was successfully added to basket')
            else:
                messages.error(
                    request, 'Not enough stock to fulfil this order.')
        else:
            basket[product_id] = quantity
            messages.success(
                request, f'{product.title} was successfully added to your basket')
    else:
        messages.error(request, 'Not enough stock to fulfil this order.')
    request.session['basket'] = basket
    return redirect(redirect_url)

