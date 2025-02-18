from django.shortcuts import render, redirect, get_object_or_404
from .forms import ThreadForm, PostForm
from .models import Thread, Post

# Create your views here.
def thread_list(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    
    threads = Thread.objects.all()
    return render(request, 'Thread_list.html', {'threads': threads, 'form': form})

def post_to_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  
            post.thread = thread
            post.picture.save(form.cleaned_data.get('picture').name, form.cleaned_data.get('picture'))
            post.save()  
            return redirect('post_to_thread', id=thread.id)

    else:
        form = PostForm()

    return render(request, 'post_to_thread.html', {'thread': thread, 'posts': posts, 'form': form})

def thread_delete(request,id):
    thread = get_object_or_404(Thread,id=id)
    thread.delete()
    return redirect('thread_list')

def post_delete(request,id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id 
    post.delete()
    return redirect('post_to_thread', id=thread_id)


def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_list') 
    else:
        form = ThreadForm(instance=thread)
    
    return render(request, 'thread_edit.html', {'form': form, 'thread': thread})




def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_to_thread', id=post.thread.id)  # Возвращаемся на страницу треда
    else:
        form = PostForm(instance=post)

    return render(request, 'post_edit.html', {'form': form, 'post': post})
