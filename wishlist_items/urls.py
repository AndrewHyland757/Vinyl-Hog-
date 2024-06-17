from django.urls import path
from . import views


urlpatterns = [
    path("", views.wishlist_items, name="wishlist-items"),
    path("add/<int:product_id>/", views.add_wishlist_item, name="add-wishlist"),
    path("delete/<int:product_id>/", views.delete_wishlist_item, name="delete-wishlist"),
]
