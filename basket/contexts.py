from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Album


def basket_contents(request):

    delivery_threshold = settings.DELIVERY_THRESHOLD

    basket_items = []
    products_to_delete = []
    price_total = 0
    product_count = 0
    quantity = 0
    basket = request.session.get('basket', {})
    

    for product_id, quantity in basket.items():

        # Identifies product from model
        product = get_object_or_404(Album, id=product_id)
        
        # Checks if item is still in stock
        if product.stock <= 0:
            products_to_delete.append(product_id)
        
        
        price_sub_total = product.price * int(quantity)
        price_total += product.price * int(quantity)
        product_count += int(quantity)

        # Add these keys and values to the basket object
        basket_items.append({
            'product_id': product_id,
            'quantity': int(quantity), 
            'product': product,
            "price_sub_total": price_sub_total,

        })

    for product_id in products_to_delete:
        basket.pop(product_id)
        messages.error(request,
                    f'{product.title} is out of stock and has been removed from your basket')

    request.session['basket'] = basket


    if price_total > delivery_threshold or price_total == 0:
        delivery_fee = "Free"
        free_delivery_delta = 0
        grand_total = price_total

    else:
        free_delivery_delta = delivery_threshold - price_total
        delivery_fee = settings.DELIVERY_FEE
        
        grand_total = price_total + int(delivery_fee)

    
    

    
    context = {
        "price_sub_total": price_sub_total,
        "basket_items": basket_items,
        "product": product,
        'grand_total': grand_total,
        'delivery_fee': delivery_fee,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': delivery_threshold,
        'basket_items': basket_items,
        'price_total': price_total, # Total price of basket
        "quantity" : quantity, # Total no. of  individual product in basket
        'product_count': product_count, # Total no. of products in basket
        
    }

    return context