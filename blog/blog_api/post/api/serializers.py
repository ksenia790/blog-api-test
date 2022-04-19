from rest_framework.serializers import ModelSerializer
from post.models import Post, Comment

# Comment Serializers
class CommentDetailSerializer(ModelSerializer):
    class Meta:
    	model = Comment
    	fields = [
    	    'id',
		    'post',
            'name',
            'body',
            'email',
            'parent',
		]

class CommentListSerializer(ModelSerializer):
    class Meta:
    	model = Comment
    	fields = "__all__"

# Post Serializers

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