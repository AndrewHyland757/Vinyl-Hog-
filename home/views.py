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
    recent_added_posts = posts_by_date[1:4]
    recent_added_posts_2 = posts_by_date[4:7]
   
    first_post = posts_by_date[0]
    
    

    context = {
        "albums": albums,
        "recent_added_albums": recent_added_albums,
        "recent_added_posts": recent_added_posts,
        "recent_added_posts_2": recent_added_posts_2,
        "first_post": first_post,
 
    }

    return render(request, 'home/home.html', context)


def blog_posts(request):

    

    posts = RecommendationPost.objects.all()
    
   
    posts_by_date = RecommendationPost.objects.all().order_by('-created_on')
    recent_added_posts = posts_by_date[1:4]
    recent_added_posts_2 = posts_by_date[4:7]
   
    first_post = posts_by_date[0]
    second_post = posts_by_date[1]
    third_post = posts_by_date[2]
    fourth_post = posts_by_date[5]

    context = {
       
        "recent_added_posts": recent_added_posts,
        "recent_added_posts_2": recent_added_posts_2,
        "first_post": first_post,
        "second_post": second_post,
        "third_post": third_post,
        "fourth_post": fourth_post,

 
    }

    return render(request, 'home/blog_posts.html', context)