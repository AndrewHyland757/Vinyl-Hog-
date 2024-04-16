from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Album


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for product_id, quantity in basket.items():
        product = get_object_or_404(Album, id=product_id)  #pk=item_id
        
        total += quantity
        product_count += quantity
        basket_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    
    context = {
        'basket_items': basket_items,
        'total': total,
        "quantity" : quantity,
        'product_count': product_count,
        
    }

    return context

