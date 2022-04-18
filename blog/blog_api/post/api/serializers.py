from rest_framework.serializers import ModelSerializer
from post.models import Post


class PostCreateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		    'title',
            'author',
            'body',
            'publish',
		]

class PostDetailSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		    'id',
            'title',
            'slug',
            'author',
            'body',
            'publish',
		]

class PostListSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		    'id',
            'title',
            'slug',
            'author',
            'body',
            'publish',
		]