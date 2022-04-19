from rest_framework.serializers import ModelSerializer, SerializerMethodField
from post.models import Post, Comment

# Comment Serializers
class CommentDetailSerializer(ModelSerializer):
	replies = SerializerMethodField()
	class Meta:
		model = Comment
		fields = [
    	    'id',
		    'post',
            'name',
            'body',
            'replies',
		]
	
	def get_replies(self, obj):
		if obj.is_parent:
			return CommentChildSerializer(obj.children(), many=True).data
		return None


class CommentListSerializer(ModelSerializer):
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

class CommentChildSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = [
		'id',
		'body',
		'created',
		]

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