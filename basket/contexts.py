from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Album


def basket_contents(request):

    delivery_threshold = settings.DELIVERY_THRESHOLD
    delivery_fee = settings.DELIVERY_FEE
    basket_items = []
    products_to_delete = []
    price_total = 0
    product_count = 0
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
        delivery_fee = 0
        free_delivery_delta = 0
    else:
        free_delivery_delta = delivery_threshold - price_total

    grand_total = price_total + delivery_fee
    
    context = {
        
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': delivery_threshold,
        'basket_items': basket_items,
        'price_total': price_total, # Total price of basket
        "quantity" : quantity, # Total no. of  individual product in basket
        'product_count': product_count, # Total no. of products in basket
        
    }

    return context





def cart_contents(request):
    '''
    Handles the shopping cart contents
    '''
    delivery_threshold = settings.DELIVERY_THRESHOLD
    delivery_fee = settings.DELIVERY_FEE
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    items_to_remove = []
    discount = request.session.get('discount')
    discount_amount = 0

    for item_id, quantity in cart.items():
        book = get_object_or_404(Book, pk=item_id)
        # remove items that are out of stock
        if book.in_stock is False:
            items_to_remove.append(item_id)

        total += book.product_price * int(quantity)
        product_count += int(quantity)
        cart_items.append({
            'item_id': item_id,
            'quantity': int(quantity),
            'book': book,
        })

    for item_id in items_to_remove:
        cart.pop(item_id)
        messages.error(request,
                       f'{book.title} is out of stock and has been removed')

    request.session['cart'] = cart

    # Apply discount to total amount excluding delivery
    if discount:
        discount_amount = (total * discount)/100
        total -= discount_amount

    if total > delivery_threshold or total == 0:
        delivery_fee = 0
        free_delivery_delta = 0
    else:
        free_delivery_delta = delivery_threshold - total

    grand_total = total + delivery_fee

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery_fee': delivery_fee,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': delivery_threshold,
        'grand_total': grand_total,
        'discount_amount': discount_amount,
    }
    return context