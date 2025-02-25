from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("posts:list")
        else:
            return render(request, "posts/login.html", {"error": "Invalid credentials"})
    return render(request, "posts/login.html")

def logout_view(request):
    logout(request)
    return redirect("posts:login")

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "posts/my_posts.html", {"posts": posts})

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "posts/post_detail.html", {"post": post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts:list")
    else:
        form = PostForm()
    return render(request, "posts/post_form.html", {"form": form})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect("posts:list")
    return HttpResponseForbidden()
