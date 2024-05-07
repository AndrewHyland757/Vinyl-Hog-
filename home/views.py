from django.shortcuts import render, redirect, reverse, get_object_or_404
from . import views
from products.models import Album
from blog.models import RecommendationPost
from django.contrib.auth.decorators import login_required

# Create your views here.
     

def home(request):

    albums = Album.objects.all()
    albums_with_imgs = Album.objects.exclude(featured_image = "default.jpg")
    albums_by_date = Album.objects.all().order_by('-date_added')
    recent_added_albums =  albums_by_date[0:8]
    
    posts = RecommendationPost.objects.all()
    posts_by_date = RecommendationPost.objects.all().order_by('-created_on')
    recent_added_posts =  posts_by_date[0:3]

    context = {
    "albums": albums,
    "recent_added_albums": recent_added_albums,
    "recent_added_posts": recent_added_posts,
    }
    
    return render(request, 'home/home.html', context)




