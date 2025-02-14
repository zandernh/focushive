
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register', views.register),
    path('my-login', views.my_login),


    # Crud Operations


    # Create Task
    path('create-task', views.createTask),

    # Read Task
    path('view-tasks', views.viewTask, name="view-tasks"),
]











