from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, UserLoginForm, CreateTaskForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import Task

# Create your views here.

# ----------------------------------- Homepage ----------------------------------------------- #
# -------------------------------------------------------------------------------------------- #

def home(request):
    return render(request, 'index.html')


# ----------------------------------- User Registration -------------------------------------- #
# -------------------------------------------------------------------------------------------- #

def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')
        
    context = {'form' : form}
    
    return render(request, 'register.html', context=context)


# -------------------------------------- User Login ------------------------------------------ #
# -------------------------------------------------------------------------------------------- #

def login(request):

    form = UserLoginForm()

    if request.method == "POST":

        form = UserLoginForm(request, request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")
    
    context = {'form' : form}

    return render(request, 'login.html', context=context)


# -------------------------------------- User Dashboard -------------------------------------- #
# -------------------------------------------------------------------------------------------- #

@login_required(login_url="login")
def dashboard(request):

    return render(request, 'profile/dashboard.html')


# -------------------------------------- CREATE TASK ----------------------------------------- #
# -------------------------------------------------------------------------------------------- #

@login_required(login_url="login")
def createTask(request):

    form = CreateTaskForm()

    if request.method == 'POST':

        form = CreateTaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.user = request.user

            task.save()

            return redirect('view-task')
        
    context = {'form' : form}

    return render(request, 'profile/create-task.html', context=context)


# -------------------------------------- READ TASK ------------------------------------------- #
# -------------------------------------------------------------------------------------------- #

@login_required(login_url="login")
def viewTask(request):

    current_user = request.user.id

    task = Task.objects.all().filter(user=current_user)

    context = {'task' : task}

    return render(request, 'profile/view-task.html', context=context)


# ------------------------------------- UPDATE TASK ------------------------------------------ #
# -------------------------------------------------------------------------------------------- #

@login_required(login_url="login")
def updateTask(request, pk, title):

    task = Task.objects.get(id=pk, title=title)

    form = CreateTaskForm(instance=task)

    if request.method == 'POST':

        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('view-task')
        
    context = {'form' : form}

    return render(request, 'profile/update-task.html', context=context)


# ------------------------------------- DELETE TASK ------------------------------------------ #
# -------------------------------------------------------------------------------------------- #

@login_required(login_url='login')
def deleteTask(request, pk, title):

    task = Task.objects.get(id=pk, title=title)

    if request.method == 'POST':

        task.delete()

        return redirect('view-task')
    
    return render(request, 'profile/delete-task.html')


# -------------------------------------- User Logout ----------------------------------------- #
# -------------------------------------------------------------------------------------------- #

def logout(request):

    auth.logout(request)

    return redirect("")