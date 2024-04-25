from django.shortcuts import render
from . import views
from products.models import Album
import random


# Create your views here.


def home(request):

     albums = Album.objects.all()
     
     '''
     Gets two random album covers for the homepage
     '''
     albums_with_imgs = Album.objects.exclude(featured_image = "default.jpg")
     used_covers = []
     random_album_1 = random.choice(albums_with_imgs)
     
     random_album_2 =random.choice(albums_with_imgs.exclude(title = random_album_1 ))
     
     albums_by_date = Album.objects.all().order_by('-date_added')

     recent_added_albums =  albums_by_date[0:8]
     

          
   
     

     context = {
        "albums": albums,
        "random_album_1": random_album_1,
        "random_album_2": random_album_2,
        "recent_added_albums": recent_added_albums,
         
    }

    
     print(albums_by_date)
     print(recent_added_albums)

     print(random_album_1)
     
     
     return render(request, 'home/home.html', context)



     

    
   
