from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import stripe

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        "stripe_public_key": "pk_test_51P8JG3ECqW0pS3vWbIGOgoOz6xN9ZHbRdDhk0QYEJP2qm2ye4a0MQ6TWR0DrQiEiHarteXCKRcqi1GOq1C3qEUwM00g1d7Xhos",
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
