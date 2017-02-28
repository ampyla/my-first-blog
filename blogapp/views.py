from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Comments
from django.utils import timezone
from .form import PostForm
from .form import CommentForm
from django.shortcuts import redirect
from django.contrib import auth
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'username':auth.get_user(request).username})

def post_edit_comment(request, pk):
    #post = get_object_or_404(Post, pk=pk)
    #return render(request, 'blog/post_detail.html', {'post': post})
    if request.method == 'POST' and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_post =get_object_or_404(Post, pk=pk)
            comment.save()
            request.session.set_expiry(60)
            request.session['pause']=True
    return redirect('post_detail', pk=pk)
            #return redirect('post_details', pk=pk)

def post_detail(request, pk):
    form = CommentForm()
    args = {}
    args['post'] = get_object_or_404(Post, pk=pk)
    args['comments'] = Comments.objects.filter(comments_post_id = pk)
    args['form'] = form
    return render(request, 'blog/post_detail.html',args)



def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def addlike(request, pk):
    like = get_object_or_404(Post, pk=pk)
    like.like += 1
    like.save()
    return redirect('/')



