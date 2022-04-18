from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer
from post.models import Post

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer


class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer


class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer

