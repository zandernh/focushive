from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, CreateUserForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def my_login(request):
    return render(request, 'my-login.html')


# - CREATE a Task

def createTask(request):

    form = TaskForm()

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("view-tasks")
        
    context = {'form' : form}

    return render(request, 'create-task.html', context=context)

# - READ a Task

def viewTask(request):

    tasks = Task.objects.all()

    context = {'tasks' : tasks}

    return render(request, 'view-tasks.html', context=context)


# - UPDATE a Task

def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect("view-tasks")
        
    context = {'form': form}

    return render(request, 'update-task.html', context=context)

# - DELETE a Task

def deleteTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    return render(request, 'delete-task.html')


# - REGISTERING / CREATING a User

def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponse("User was registered successfully")
        
    context = {'form' : form}
    
    return render(request, 'register.html', context=context)