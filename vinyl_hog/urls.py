"""vinyl_hog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("products/", include("products.urls")),
    path("basket/", include("basket.urls")),
    path("checkout/", include("checkout.urls")),
    path("profile/", include("profiles.urls")),
    path("blog/", include("blog.urls")),
    path("product_management/", include("product_management.urls")),
    path("wishlist/", include("wishlist_items.urls")),
    path("shipping/", views.footer_shipping, name="footer-shipping"),
    path("returns/", views.footer_returns, name="footer-returns"),
    path("our_story/", views.footer_our_story, name="footer-our-story"),
    path("planet_vinylhog/", views.footer_planet_vinylhog, name="footer-planet-vinylhog"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "vinyl_hog.views.handler404"
