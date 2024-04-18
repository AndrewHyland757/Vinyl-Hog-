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
    
    if product.stock <= 0:
        product_stock = "Out of stock"
    else:
        product_stock = product.stock

    condition = product.condition
    artist = product.artist
    title = product.title
    more_by_this_artist = Album.objects.filter(artist__exact = artist).exclude(title__exact = title)
    alternative_condition = Album.objects.filter(artist__exact = artist, title__exact = title).exclude(condition__exact = condition).exists()
    
    
   
    

    

     
        

   


    context = {
        "condition": condition,
        "product": product,
        "product_stock": product_stock,
        "more_by_this_artist": more_by_this_artist,
        "alternative_condition": alternative_condition    }

    print(condition)
    return render(request, 'products/product.html', context)






    