from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import views
from products.models import Album
from blog.models import RecommendationPost

# Create your views here.


def home(request):
    """
    Renders home page.
    """
    albums = Album.objects.all()
    albums_by_date = Album.objects.all().order_by("-date_added")
    recent_added_albums = albums_by_date[0:8]
    posts = RecommendationPost.objects.all()
    post_1 = None
    posts_1_5 = None
    posts_by_date = RecommendationPost.objects.all().order_by("-created_on")

   

    if posts:
        post_1 = posts_by_date[0]
        posts_1_5 = posts_by_date[0:4]


    print ( posts_1_5)
    print (post_1)


    context = {
        "albums": albums,
        "recent_added_albums": recent_added_albums,
        "posts_1_5": posts_1_5,
        "post_1": post_1,
    }

    return render(request, "home/home.html", context)


