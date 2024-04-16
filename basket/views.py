from django.shortcuts import render, redirect

# Create your views here.

def basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_basket(request, product_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if product_id in list(basket.keys()):
        basket[product_id] += quantity
    else:
        basket[product_id] = quantity

    

    request.session['basket'] = basket
    return redirect(redirect_url)

