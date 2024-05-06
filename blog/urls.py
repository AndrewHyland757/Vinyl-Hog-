from django.urls import path
from . import views 


urlpatterns = [
    
    path("", views.posts, name='posts'),
    path("post/<int:post_id>/", views.post, name='post'),
    path("post_management", views.blog_post_management, name='blog-post-management'),

    
    path('add/', views.add_post, name='add-post'),
    path('add_author/', views.add_author, name='add-author'),
]