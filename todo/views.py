from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm

from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Task, Profile

from django.contrib import messages

# ------------------------------------- #
# --- --- --- --- VIEWS --- --- --- --- #
# ------------------------------------- #

# ---------------------------- #
# --- --- --- Home --- --- --- #

def home(request):
    return render(request, 'index.html')


# --------------------------------------- #
# --- --- --- Register A User --- --- --- #

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False)


            form.save()

            profile = Profile.objects.create(user=current_user)

            messages.success(request, "User registration successful")
            return redirect("login")

    
    context = {'form' : form}

    return render(request, 'register.html', context=context)


# ------------------------------------ #
# --- --- --- Login A User --- --- --- #

def login(request):
    
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)
                messages.success(request, "Login successful")
                return redirect('dashboard')
    
    context = {'form' : form}

    return render(request, 'login.html', context=context)


# --------------------------------- #
# --- --- --- Dashboard --- --- --- #

@login_required(login_url='login')
def dashboard(request):

    profile_pic = Profile.objects.get(user=request.user)
    
    context = {'profile' : profile_pic}

    return render(request, 'profile/dashboard.html', context=context)


# ------------------------------------------ #
# --- --- --- Profile Management --- --- --- #

@login_required(login_url='login')
def profile_management(request):

    user_form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)

    # form_2 = UpdateProfilePictureForm(instance=profile)

    if request.method == 'POST':
        
        user_form = UpdateUserForm(request.POST, instance=request.user)
        # form_2 = UpdateProfilePictureForm(request.POST, request.FILES, instance=profile)


        if user_form.is_valid():

            user_form.save()
            messages.success(request, "Profile information updated")
            return redirect('dashboard')
        
        # if form_2.is_valid():

        #     form_2.save()
        #     return redirect('dashboard')
        
    context = {'user_form': user_form}

    return render(request, 'profile/profile-management.html', context=context)


# -------------------------------------- #
# --- --- --- Delete Account --- --- --- #

@login_required(login_url='login')
def delete_account(request):
    
    if request.method == 'POST':

        delete_user = User.objects.get(username=request.user)

        logout(request)
        delete_user.delete()
        return redirect('')
    
    return render(request, 'profile/delete-account.html')


# ------------------------------------------------------ #
# --- --- --- CRUD OPERATIONS OF APPLICATION --- --- --- #
# ------------------------------------------------------ #


# ----------------------------------- #
# --- --- --- Create Task --- --- --- #

@login_required(login_url='login')
def createTask(request):

    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)
            task.user = request.user

            task.save()
            return redirect('view-tasks')
    
    context = {'form' : form}

    return render(request, 'profile/create-task.html', context=context)


# --------------------------------- #
# --- --- --- Read Task --- --- --- #

@login_required(login_url='login')
def viewTasks(request):
    
    current_user = request.user.id

    task = Task.objects.all().filter(user=current_user)

    context = {'task': task}

    return render(request, 'profile/view-tasks.html', context=context)


# ----------------------------------- #
# --- --- --- Update Task --- --- --- #

@login_required(login_url='login')
def updateTask(request, pk, title):
    
    task = Task.objects.get(id=pk, title=title)

    form = CreateTaskForm(instance=task)

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, "Task updated")
            return redirect('view-tasks')
        
    context = {'form' : form}

    return render(request, 'profile/update-task.html', context=context)
    

# ----------------------------------- #
# --- --- --- Delete Task --- --- --- #

@login_required(login_url='login')
def deleteTask(request, pk, title):

    task = Task.objects.get(id=pk, title=title)

    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted")
        return redirect('view-tasks')

    return render(request, 'profile/delete-task.html')

# ------------------------------------------------------ #
# ------------------------------------------------------ #
# ------------------------------------------------------ #

# ------------------------------------- #
# --- --- --- Logout A User --- --- --- #

def logout(request):
    
    auth.logout(request)

    return redirect('')