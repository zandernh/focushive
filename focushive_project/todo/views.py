from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def my_login(request):
    return render(request, 'my-login.html')


# Create a Task

def createTask(request):

    form = TaskForm()

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("view-tasks")
        
    context = {'form' : form}

    return render(request, 'create-task.html', context=context)

# Read a Task

def viewTask(request):

    tasks = Task.objects.all()

    context = {'tasks' : tasks}

    return render(request, 'view-tasks.html', context=context)