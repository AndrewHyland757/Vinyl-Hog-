from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from products.models import Album
from django.contrib import messages

# Create your views here.


def basket(request):
    '''
    A view that renders the basket contents page.
    '''

    return render(request, 'basket/basket.html')


def add_basket(request, product_id):
    '''
    Add a quantity of the specified product to the shopping basket.
    '''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    product = get_object_or_404(Album, id=product_id)

    if quantity <= product.stock:
        if product_id in list(basket.keys()):
            total_quantity = int(basket[product_id]) + quantity
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


def update_basket(request, product_id):
    '''
    Updates the basket quantity of a product.
    '''
    basket = request.session.get('basket', {})
    product = get_object_or_404(Album, id=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if product_id in list(basket.keys()):
        if quantity <= product.stock:
            basket[product_id] = quantity
            messages.success(
                request, f'{product.title} quantity updated successfully.')
        else:
            messages.error(request, 'Not enough stock to fulfil this order')

    request.session['basket'] = basket
    return redirect(redirect_url)


def delete_basket_item(request, product_id):
    '''
    Deletes a basket item.
    '''
    basket = request.session.get('basket', {})
    product = get_object_or_404(Album, id=product_id)
    redirect_url = request.POST.get('redirect_url')

    if product_id in list(basket.keys()):
        basket.pop(product_id)
        messages.success(request, f'{product.title} removed from basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)
