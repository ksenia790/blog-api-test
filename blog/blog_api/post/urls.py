from django.urls import path
from . import views

app_name = 'post' #blog

urlpatterns=[
    path('', views.post_list, name="post_list"),
    path('<slug:post>/', views.post_detail, name="post_detail"),
    path('comment/reply/', views.reply_page, name="reply"),
]