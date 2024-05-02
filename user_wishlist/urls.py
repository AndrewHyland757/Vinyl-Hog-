from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_wishlist, name='user-wishlist'),
    #path('wishlist_add/<str:pk>/', views.wishlist_add, name='wishlist-add'),
    path('wishlist_delete/<str:pk>/', views.wishlist_delete, name='wishlist-delete'),
]
