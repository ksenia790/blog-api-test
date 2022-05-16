from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm


def post_list(request):
    '''
    Returns all published posts.
    '''

    posts = Post.published.all()
    paginator = Paginator(posts, 10)
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
    ''' 
    Returns particular published post by it's slug-name. 
    '''

    post = get_object_or_404(Post,slug=post,status='published')
    # List of active comments for particular post
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm(data=request.POST) 
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
        else:
            comment_form = CommentForm()

    return render(request, 'post_detail.html',{'post':post,'comments':comments,'comment_form':comment_form})

# Handling reply, reply view.
def reply_page(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id') 
            parent_id = request.POST.get('parent') 
            post_url = request.POST.get('post_url')
            reply = form.save(commit=False)
            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.children = Comment(id=parent_id)
            reply.save()
            return redirect(post_url+'#'+str(reply.id))
     return redirect("/")
