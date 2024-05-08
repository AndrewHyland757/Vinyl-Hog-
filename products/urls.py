from django.urls import path
from . import views


urlpatterns = [
    path("", views.products, name='products'),
    path("product/<int:product_id>", views.product, name='product'),
    path('product_management/', views.product_management, name='product-management'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('add_genre/', views.add_genre, name='add_genre'),
]