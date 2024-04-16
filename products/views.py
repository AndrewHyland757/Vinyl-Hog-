from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
#from .models import Album


def products(request):

    products = Album.objects.all()
    context = {
        "albums": products
    }

    return render(request, 'products/products.html', context)


def product(request, pk):

    product = Album.objects.get(id=pk)
    context = {
        "album": product
    }

    return render(request, 'products/product.html', context)