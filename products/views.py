from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Album, Condition, Genre
#from .models import Album


def products(request):

    products = Album.objects.all()
    
    
    query= None
    conditions = None
    section_heading = "All Vinyl"
    recent_added_products = None
    sort = None
    direction = None
    


    if request.GET:
        
        
        if 'condition' in request.GET:
            requested_condition = request.GET['condition'].split(',')
            
            if requested_condition == ["fresh"]:

                products_by_date = products.order_by('-date_added')
                products =  products_by_date[0:12]
                section_heading = "New Releases"

            else:
                

                products = products.filter(condition__name__in=requested_condition) 
                
                conditions = Condition.objects.filter(name__in=requested_condition)
               
                if requested_condition == ["New"]:
                    section_heading = "New Vinyl"
                else:
                    section_heading = "Used Vinyl"
            
       
        if 'genre' in request.GET:
            requested_genre = request.GET['genre'].split(',')
            products = products.filter(genres__name__in=requested_genre) 
                
            conditions = Genre.objects.filter(name__in=requested_genre)

            section_heading = requested_genre[0]

            


        
        

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # Searches the album title, artist name and genre for matches
            queries = Q(title__icontains=query) | Q(artist__name__icontains=query)
            products = products.filter(queries)

    
    context = {
        "albums": products,
        'current_conditions': conditions,
        'search_term': query,
        "section_heading": section_heading,
        
       
        
        
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






    