from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, UserLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

            return HttpResponse("User was registered successfully")
        
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

    return render(request, 'dashboard.html')


# -------------------------------------- User Logout ----------------------------------------- #
# -------------------------------------------------------------------------------------------- #

def logout(request):

    auth.logout(request)

    return redirect("")