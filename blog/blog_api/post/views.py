from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request):
    '''Returns all published posts.'''

    #posts = Post.objects.filter(status="published")
    posts = Post.published.all()

    paginator = Paginator(posts, 10) # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        
    return render(request,'post_list.html',{'posts':posts, page:'pages'})


def post_detail(request, post):
    ''' Returns particular published post by it's slug-name. '''

    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'post_detail.html', {'post':post})