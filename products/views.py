from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album
#from .models import Album


def products(request):

    products = Album.objects.all()
    context = {
        "albums": products
    }

    return render(request, 'products/products.html', context)


def product(request, product_id):

    product = get_object_or_404(Album, id=product_id)
    context = {
        "album": product
    }

    return render(request, 'products/product.html', context)



    