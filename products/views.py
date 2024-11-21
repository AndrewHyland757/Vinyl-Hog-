from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import Album, Condition, Genre, Artist
from .forms import ProductForm, ArtistForm, GenreForm
from django.db import models
from django.db.models import Case, When, F
from basket.views import add_basket
from wishlist_items.views import add_wishlist_item
from django.http import JsonResponse
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)  # Cache for 15 minutes
def products(request):
    """
    Displays the products including filter and sort functionality.
    """
    products = Album.objects.all()
    artists = Artist.objects.all().order_by('name')
    genres = Genre.objects.all().order_by('name')
    query = None
    conditions = None
    section_heading = "All Vinyl"
    section_text = "Our full selection of vinyl."
    recent_added_products = None
    sort = None
    direction = None
    requested_artist_products = None
    artist_active = None
    genre_active = None
    sort = None

    if request.GET:
        if "recent" in request.GET:
            products = products.order_by("-date_added")
            section_text = "Recently added vinyl."

        if "artist" in request.GET:
            requested_artist = request.GET["artist"].split(',')
            products = products.filter(artist__name__in=requested_artist)
            section_heading = requested_artist[0]
            section_text = "Our full library of vinyl."

        if "category" in request.GET:
            requested_category = request.GET["category"].split(',')
            if requested_category == ["on_sale"]:
                products = products.filter(on_sale=True)
                section_heading = "On Sale Vinyl"
                section_text = "Our full library of on sale vinyl."

            elif requested_category == ["latest"]:
                section_heading = "Latest Releases"
                section_text = "Check out our latest releases."
                products = products.order_by("-date_added")

            else:
                products = products.filter(condition__name__in=requested_category)
                conditions = Condition.objects.filter(name__in=requested_category)

                if requested_category == ["New"]:
                    section_heading = "New Vinyl"
                    section_text = "Our full library of brand new vinyl."
                else:
                    section_heading = "Used Vinyl"
                    section_text = "Our full library of high quality used vinyl."

        if "genre" in request.GET:
            requested_genre = request.GET["genre"].split(',')
            products = products.filter(genres__name__in=requested_genre)
            section_heading = requested_genre[0].capitalize()
            genre_active = [requested_genre[0].capitalize(), requested_genre[0].lower()]

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(title__icontains=query) | Q(artist__name__icontains=query)
            section_heading = f'"{query}"'
            section_text = "Search results."
            products = products.filter(queries)

        # Apply sorting after all filters
        if "sort" in request.GET:
            sort = request.GET.get("sort")
            if sort == "price_asc":
                products = products.annotate(
                    effective_price=Case(
                        When(on_sale=True, then=F("sale_price")),
                        default=F("price"),
                        output_field=models.DecimalField()
                    )
                ).order_by("effective_price")
            elif sort == "price_desc":
                products = products.annotate(
                    effective_price=Case(
                        When(on_sale=True, then=F("sale_price")),
                        default=F("price"),
                        output_field=models.DecimalField()
                    )
                ).order_by("-effective_price")
            elif sort == "title_asc":
                products = products.order_by("title")
            elif sort == "title_desc":
                products = products.order_by("-title")

    context = {
        "section_text": section_text,
        "albums": products,
        "search_term": query,
        "section_heading": section_heading,
        "artists": artists,
        "genres": genres,
        "genre_active": genre_active,
        "artist_active": artist_active,
    }

    return render(request, "products/products.html", context)


def product(request, product_id):
    """
    Renders an individual product.
    """
    product = get_object_or_404(Album, id=product_id)

    if product.stock <= 0:
        product_stock = "Out of stock"
    else:
        product_stock = product.stock

    # Checks which form has been submitted and calls the relevant view
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "basket":
            return add_basket(request, product_id)
        elif form_type == "wishlist":
            return add_wishlist_item(request, product_id)

    context = {
        "product": product,
        "product_stock": product_stock,
    }

    return render(request, "products/product.html", context)
