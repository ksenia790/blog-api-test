from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, PostCreateAPIView


app_name = 'post' 

urlpatterns=[
    path('', PostListAPIView.as_view(), name="list"),
    path('create/', PostCreateAPIView.as_view(), name="create"),
    path('<slug:pk>/', PostDetailAPIView.as_view(), name="detail"),
    
    # path('comment/reply/', views.reply_page, name="reply"),
]