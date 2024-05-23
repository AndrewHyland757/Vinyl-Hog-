from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import Album, Condition, Genre, Artist
from .forms import ProductForm, ArtistForm, GenreForm



def products(request):
    '''
    Displayes the products.
    '''
    products = Album.objects.all()
    artists = Artist.objects.all()
    genres = Genre.objects.all()

    query = None
    conditions = None
    section_heading = "All Vinyl"
    section_text = "Our full selection of vinyl."
    recent_added_products = None
    sort = None
    direction = None
    requested_artist_products = None

    if request.GET:

        if 'recent' in request.GET:
            products = Album.objects.all().order_by('-date_added')
            section_text = "Recently added vinyl."

        if 'sale' in request.GET:
            products = Album.objects.filter(on_sale=True)
            section_heading = "On Sale Vinyl"
            section_text = "Our full library of on sale vinyl."

        if 'artist' in request.GET:
            '''
            Displays items depending on the artist.
            '''
            requested_artist = request.GET['artist'].split(',')
            products = products.filter(artist__name__in=requested_artist)
            section_heading = requested_artist[0].capitalize()
            section_text = "Our full library of vinyl."

        if 'condition' in request.GET:
            '''
            Displays items depending on the condition.
            '''
            requested_condition = request.GET['condition'].split(',')
            if requested_condition == ["fresh"]:
                products_by_date = products.order_by('-date_added')
                products = products_by_date[0:12]
                section_heading = "New Releases"
                section_text = "Check out our latest releases."
            else:
                products = products.filter(condition__name__in=requested_condition)
                conditions = Condition.objects.filter(name__in=requested_condition)

                if requested_condition == ["New"]:
                    section_heading = "New Vinyl"
                    section_text = "Our full library of brand new vinyl."
                else:
                    section_heading = "Used Vinyl"
                    section_text = "Our full library of high quality used vinyl."

        if 'genre' in request.GET:
            '''
            Displays items depending on genre.
            '''
            requested_genre = request.GET['genre'].split(',')
            products = products.filter(genres__name__in=requested_genre)
            #conditions = Genre.objects.filter(name__in=requested_genre)
            section_heading = requested_genre[0].capitalize()
     
        if 'q' in request.GET:
            '''
            Displays items depending on search request.
            '''
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(artist__name__icontains=query)
            products = products.filter(queries)
            

    context = {
        
        "section_text": section_text,
        "albums": products,
        'current_conditions': conditions,
        'search_term': query,
        "section_heading": section_heading,
        "artists": artists,
        "genres": genres,
    }

    return render(request, 'products/products.html', context)


def product(request, product_id):
    '''
    Displays a single product.
    '''
    product = get_object_or_404(Album, id=product_id)

    if product.stock <= 0:
        product_stock = "Out of stock"
    else:
        product_stock = product.stock

    context = {
        "product": product,
        'product_stock': product_stock,
    }

    return render(request, 'products/product.html', context)

