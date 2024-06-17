from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_management, name="product-management"),
    path("artists/", views.artist_management, name="artist-management"),
    path("genres/", views.genre_management, name="genre-management"),

    path("add_product/", views.add_product, name="add-product"),
    path("add_artist/", views.add_artist, name="add-artist"),
    path("add_genre/", views.add_genre, name="add-genre"),

    path("edit_product/<int:product_id>/", views.edit_product, name="edit-product"),
    path("edit_artist/<int:artist_id>/", views.edit_artist, name="edit-artist"),
    path("edit_genre/<int:genre_id>/", views.edit_genre, name="edit-genre"),

    path("delete_product/<int:product_id>/", views.delete_product, name="delete-product"),
    path("delete_artist/<int:artist_id>/", views.delete_artist, name="delete-artist"),
    path("delete_genre/<int:genre_id>/", views.delete_genre, name="delete-genre"),
]
