from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
	'''Returns all published posts.'''

	#posts = Post.objects.filter(status="published")
	posts = Post.published.all()
	return render(request, 'post_list.html', {'posts':posts})

def post_detail(request, post):
	''' Returns published post by it's slug-name. '''

	post = get_object_or_404(Post, slug=post, status='published')
	return render(request, 'post_detail.html', {'posts':posts})