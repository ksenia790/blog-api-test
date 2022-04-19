from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import (
	PostListSerializer, 
	PostDetailSerializer, 
	PostCreateSerializer, 
	CommentDetailSerializer,
	CommentListSerializer,
	)
from post.models import Post, Comment

# Comments
class CommentDetailAPIView(RetrieveAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentDetailSerializer

class CommentListAPIView(ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentListSerializer


#Post
class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer


class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer


class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer

