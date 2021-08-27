from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogOverview, name="blog-overview"),
    path('posts/', views.listPost, name="posts")
]