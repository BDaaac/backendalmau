from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def home_redirect(request):
    return redirect('thread_list')

from django.shortcuts import render, redirect
from .models import Thread
from .forms import ThreadForm

def thread_list(request):
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем новую тему
            return redirect("thread_list")  # Перенаправляем обратно на список тем
    else:
        form = ThreadForm()

    threads = Thread.objects.all()
    return render(request, "post/thread_list.html", {"threads": threads, "form": form})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import PostForm

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.thread = thread  # Привязываем пост к текущей теме
            new_post.save()
            return redirect('thread_detail', id=thread.id)
    else:
        form = PostForm()

    return render(request, "post/thread_detail.html", {"thread": thread, "posts": posts, "form": form})

def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == "POST":
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm(instance=thread)
    return render(request, "post/thread_form.html", {"form": form})

def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, "post/post_form.html", {"form": form})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)
