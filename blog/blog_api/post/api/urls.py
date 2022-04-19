from django.urls import path
from .views import (
    PostListAPIView, 
    PostDetailAPIView, 
    PostCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
    )

app_name = 'post' 

urlpatterns = [
    path('comments/', CommentListAPIView.as_view(), name="comments"),
    path('posts/', PostListAPIView.as_view(), name="post_list"),
    path('posts/create/', PostCreateAPIView.as_view(), name="create"),
    path('comments/<slug:pk>/', CommentDetailAPIView.as_view(), name="thread"),
    path('posts/<slug:pk>/', PostDetailAPIView.as_view(), name="detail"),
    ]