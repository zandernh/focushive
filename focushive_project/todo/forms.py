from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from . models import Task


# ---------------- Register a User ---------------- #
# ------------------------------------------------- #

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


# ---------------- Login a User ------------------- #
# ------------------------------------------------- #

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# ---------------- Create a Task ------------------ #
# ------------------------------------------------- #

class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'content',]
        exclude = ['user',]

