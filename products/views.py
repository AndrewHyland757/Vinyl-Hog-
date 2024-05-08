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

    query = None
    conditions = None
    section_heading = "All Vinyl"
    section_text = "Our full selection of vinyl."
    recent_added_products = None
    sort = None
    direction = None
    requested_artist_products = None

    if request.GET:

        if 'artist' in request.GET:
            '''
            Displays items depending on the artist.
            '''
            requested_artist = request.GET['artist'].split(',')
            products = products.filter(artist__name__in=requested_artist)

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
                    section_text = "Our full library of brand new vinyl just for you."
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

'''
****************************
PRODUCT MANAGEMNET
****************************
'''

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Successfully added album "{product.title}"!')
            return redirect(reverse('product', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        template = 'products/add_product.html'
        context = {
            'form': form,
        }

    return render(request, template, context)




@login_required
def product_management(request):

    products = Album.objects.all().order_by('title')
    sub_title = "All Products"

    if request.GET:
        
        if 'artist' in request.GET:
            '''
            Displays items depending on the artist.
            '''
            
            requested_artist = request.GET['artist'].split(',')
            products = products.filter(artist__name__in=requested_artist)
            artist_name = requested_artist[0]
            sub_title  = f'Albums by: {artist_name}'
        
        if 'genre' in request.GET:
            '''
            Displays items depending on genre.
            '''
            requested_genre = request.GET['genre'].split(',')
            products = products.filter(genres__name__in=requested_genre)
            sub_title  = f'Albums in {requested_genre[0].capitalize()} genre.'
            

        if 'stock' in request.GET:
            requested_stock = request.GET['stock'].split(',')

            if requested_stock == ["in_stock"]:
                products = Album.objects.filter(stock__gte=1)
                sub_title = "Products in stock"

            elif requested_stock == ["out_stock"]:
                products = Album.objects.filter(stock=0)
                sub_title = "Products out of stock"

    template = 'products/product_management.html'
    context = {
        'sub_title': sub_title,
        'products': products,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Album, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Album, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('product-management'))

'''
****************************
ARTIST MANAGEMNET
****************************
'''

@login_required
def artist_management(request):

    artists = Artist.objects.all().order_by('name')
    template = 'products/artist_management.html'
    context = {
        'artists': artists,
    }
    return render(request, template, context)

@login_required
def add_artist(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save()
            messages.success(request, f'Successfully added artist "{artist.name}"!')
            return redirect(reverse('product-management'))
        else:
            messages.error(request, 'Failed to add artist. Please ensure the form is valid.')
    else:
        form = ArtistForm()
        
    template = 'products/add_artist.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_artist(request, artist_id):
    """ Edit an artist """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated artist!')
            return redirect('artist-management')
        else:
            messages.error(request, 'Failed to update artist. Please ensure the form is valid.')
    else:
        form = ArtistForm(instance=artist)
        messages.info(request, f'You are editing {artist.name}')

    template = 'products/edit_artist.html'
    context = {
        'form': form,
        'artist': artist,
    }

    return render(request, template, context)

'''
****************************
GENRE MANAGEMNET
****************************
'''


@login_required
def genre_management(request):

    genres = Genre.objects.all().order_by('name')
    template = 'products/genre_management.html'
    context = {
        'genres': genres,
    }
    return render(request, template, context)


@login_required
def edit_genre(request, genre_id):
    """ Edit an genre """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    genre = get_object_or_404(Genre, pk=genre_id)

    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES, instance=genre)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated genre name!')
            return redirect('genre-management')
        else:
            messages.error(request, 'Failed to update genre. Please ensure the form is valid.')
    else:
        form = GenreForm(instance=genre)
        messages.info(request, f'You are editing {genre.name}')

    template = 'products/edit_genre.html'
    context = {
        'form': form,
        'genre': genre,
    }

    return render(request, template, context)











@login_required
def add_genre(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES)
        if form.is_valid():
            genre = form.save()
            messages.success(request, f'Successfully added genre "{genre.name}"!')
            return redirect(reverse('product-management'))
        else:
            messages.error(request, 'Failed to add genre. Please ensure the form is valid.')
    else:
        form = GenreForm()

    template = 'products/add_genre.html'
    context = {
        'form': form,
    }

    return render(request, template, context)