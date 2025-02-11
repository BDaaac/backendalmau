from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/list.html", {"todos": todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, "todos/detail.html", {"todo": todo})

def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm()
    return render(request, "todos/form.html", {"form": form})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect("todo_list")
