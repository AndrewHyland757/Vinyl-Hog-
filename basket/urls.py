from django.urls import path
from . import views 


urlpatterns = [
    path("", views.basket, name='basket'),
    path("add/<str:product_id>", views.add_basket, name='add-basket'),
    
]

