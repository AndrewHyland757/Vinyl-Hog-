from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import Album, Condition, Genre, Artist
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def products(request):

    products = Album.objects.all()
    
    
    query= None
    conditions = None
    section_heading = "All Vinyl"
    section_text = "Our full selection of vinyl."
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
            requested_genre = request.GET['genre'].split(',')
            products = products.filter(genres__name__in=requested_genre) 
                
            conditions = Genre.objects.filter(name__in=requested_genre)

            section_heading = requested_genre[0].capitalize()

           
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # Searches the album title, artist name and genre for matches
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
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
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
    return redirect(reverse('products'))


    