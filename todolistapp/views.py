from django.shortcuts import render,redirect
from .models import Todo,Todo_likes
from .forms import TodoForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    form = TodoForm()
    todo_list = Todo.objects.order_by('id')
    context= {'todo' : todo_list, 'form':form}
    return render(request,'todolistapp/index.html',context)

def addtodo(request):
    form = TodoForm(request.POST)
    new_todo = Todo(text=request.POST['text'])
    new_todo.save()
    return redirect('index')

def completed(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def like(request,todo_id):
    user = request.user
    todo = Todo.objects.get(id=todo_id)
    like, created = Todo_likes.objects.get_or_create(
        user = user,
        todo = todo
    )
    if not created:
        return redirect('index')
    else:
        return redirect('index')