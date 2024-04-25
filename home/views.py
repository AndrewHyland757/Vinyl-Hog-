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
     used_covers.append(random_album_1)
     
     random_album_2 =random.choice(albums_with_imgs.exclude(title = random_album_1 ))
     random_album_3 =random.choice(albums_with_imgs.exclude(title = random_album_1).exclude(title = random_album_2 ))
     random_album_4 =random.choice(albums_with_imgs.exclude(title = random_album_1).exclude(title = random_album_2 ).exclude(title = random_album_3 ))

     

          
   
     

     context = {
        "albums": albums,
        "random_album_1": random_album_1,
        "random_album_2": random_album_2,
        "random_album_3": random_album_3,
        "random_album_4": random_album_4, 
    }

     print(used_covers)
     print(random_album_2)
     
     
     return render(request, 'home/home.html', context)



     

    
   
