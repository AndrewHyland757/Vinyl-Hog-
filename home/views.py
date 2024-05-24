from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import views
from products.models import Album
from blog.models import RecommendationPost

# Create your views here.


def home(request):

    albums = Album.objects.all()
    albums_by_date = Album.objects.all().order_by('-date_added')
    recent_added_albums = albums_by_date[0:8]

    posts = RecommendationPost.objects.all()
    
   
    posts_by_date = RecommendationPost.objects.all().order_by('-created_on')
    recent_added_posts = posts_by_date[0:3]
    posts_two_to_five = posts_by_date[1:4]
    first_post = posts_by_date[0]

    context = {
        "albums": albums,
        "recent_added_albums": recent_added_albums,
        "recent_added_posts": recent_added_posts,
        "first_post": first_post,
        "posts_two_to_five": posts_two_to_five,
    }

    return render(request, 'home/home.html', context)
