from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("blog_posts", views.blog_posts, name='blog-posts'),
]