from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogOverview, name="blog-overview"),
    path('posts/', views.listPosts, name="posts"),
    path(r'post/<str:slug>', views.listPost, name="post"),
    path('create-post/', views.createPost, name="create-post"),
]