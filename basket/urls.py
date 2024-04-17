from django.urls import path
from . import views 


urlpatterns = [
    path("", views.basket, name='basket'),
    path("add/<str:product_id>", views.add_basket, name='add-basket'),
    path("update/<str:product_id>", views.update_basket, name='update-basket'),
    path("delete/<str:product_id>", views.delete_basket_item, name='delete-basket-item'),

  
    
]

