from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms

from .models import Task, Profile


# --------------------------------------- #
# --- --- --- REGISTER A USER --- --- --- #

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]


# ----------------------------- #
# --- --- --- LOGIN --- --- --- #

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# ------------------------------------- #
# --- --- --- CREATE A TASK --- --- --- #

class CreateTaskForm(forms.ModelForm):

    class Meta:

        model = Task
        fields = ['title', 'content',]
        exclude = ['user',]


# ------------------------------------------- #
# --- --- --- UPDATE USER PROFILE --- --- --- #

class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
        exclude = ['password1', 'password2',]


# --------------------------------------------------- #
# --- --- --- UPDATE USER PROFILE PICTURE --- --- --- #

# class UpdateProfilePictureForm(forms.ModelForm):

#     profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

#     class Meta:
#         model = Profile
#         fields = ['profile_pic']
