from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from autoslug import AutoSlugField

from .forms import CommentForm, PostForm
from .models import Post, Category

# Create your views here.
def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blogFunc/detail.html', {'post': post, 'form': form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    return render(request, 'blogFunc/category.html', {'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'blogFunc/search.html', {'posts': posts, 'query': query})

def create_newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            add_form = form.save(commit=False)
            add_form.user = request.user
            add_form.save()
        return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blogFunc/create_newpost.html', {'form':form})

def delete_post(request):
    list_posts = Post.objects.filter(user=request.user)
    return render(request, 'blogFunc/delete_post.html', {'posts': list_posts})

def confirm_delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('delete_post')