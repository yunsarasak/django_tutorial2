from pickle import FALSE
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
import logging

server_logger = logging.getLogger("django.server")

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    form = PostForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
            else:
                post.author = None
            post.publish_date = timezone.now()
            post.save()
            print('test')
            server_logger.info('test')
            return redirect('post_detail', pk=post.pk)
    else:
        return render(request, 'blog/post_edit.html', {'form': form})