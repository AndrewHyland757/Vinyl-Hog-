from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from products.models import Album
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.


def basket(request):
    '''
    A view that renders the basket contents page.
    '''

    return render(request, 'basket/basket.html')
    


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def add_basket(request, product_id):

    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    product = get_object_or_404(Album, id=product_id)
    
    product_id_str = str(product_id)  # Convert product_id to string

    
    if quantity <= product.stock:
        if product_id_str in list(basket.keys()):  # Check for string version
            total_quantity = int(basket[product_id_str]) + quantity
            if total_quantity <= product.stock:
                basket[product_id_str] = int(basket[product_id_str]) + quantity
                messages.success(request,  ' added to basket')
            else:
                messages.error(request, 'Not enough stock to fulfil this order')
        else:
            basket[product_id_str] = quantity  # Add string version
            messages.success(request, ' added to basket')
    else:
        messages.error(request, 'Not enough stock to fulfil this order')

    request.session['basket'] = basket
    return redirect(redirect_url)

    
"""

def add_basket(request, product_id):

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    product = get_object_or_404(Album, id=product_id)

    if quantity <= product.stock:
        if product_id in list(basket.keys()):
            total_quantity = int(basket[product_id]) + quantity
            if total_quantity <= product.stock:
                basket[product_id] = int(basket[product_id]) + quantity
                
                message = messages.success(
                    request, f'{product.title} added to basket.')
               
            else:
                message = messages.error(
                    request, 'Not enough stock to fulfil this order.')
        else:
            basket[product_id] = quantity
            
            message = messages.success(
                request, f'{product.title} added to your basket')
            
    else:
        message = messages.error(request, 'Not enough stock to fulfil this order.')

   
    request.session['basket'] = basket
  
    return message



   
"""





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
            messages.info(
                request, f'{product.title} quantity updated.')
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
        messages.info(request, f'{product.title} removed from basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)
