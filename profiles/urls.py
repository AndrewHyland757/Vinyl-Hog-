from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    #path('admin_page', views.admin_page, name='admin_page'),
    #path('wishlist', views.wishlist, name='wishlist'),
]