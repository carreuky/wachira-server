from django.urls import path
from .views import BlogListCreateView, BlogDetailView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog_list_create'),
    path('blogs/<int:id>/', BlogDetailView.as_view(), name='blog_detail'),
]
