from django.urls import path
from . import views


urlpatterns = [
    path("", views.posts, name='posts'),
    path("post/<int:post_id>/", views.post, name='post'),
    path("post_management", views.blog_management, name='blog-management'),
    path('add/', views.add_post, name='add-post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit-post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete-post'),
]
