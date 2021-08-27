from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogOverview, name="blog-overview"),
    path('posts/', views.listPosts, name="posts"),
    path('create-post/', views.createPost, name="create-post"),
]