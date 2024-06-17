from django.urls import path
from . import views


urlpatterns = [
    path("", views.products, name="products"),
    path("product/<int:product_id>/", views.product, name="product"),
]
