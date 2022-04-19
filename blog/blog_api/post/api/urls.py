from django.urls import path
from .views import (
    PostListAPIView, 
    PostDetailAPIView, 
    PostCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
    )


app_name = 'post' 

urlpatterns=[
    path('', CommentListAPIView.as_view(), name="comments"),
    path('<slug:pk>/', CommentDetailAPIView.as_view(), name="thread"),
    path('all/', PostListAPIView.as_view(), name="list"),
    path('create/', PostCreateAPIView.as_view(), name="create"),
    path('<slug:pk>/', PostDetailAPIView.as_view(), name="detail"),
    
]