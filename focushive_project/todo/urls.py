
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),

    # ------------------- CRUD Operations ------------------- #
    # ------------------------------------------------------- #


    # - CREATE Task
    path('create-task', views.createTask, name="create-task"),

    # - READ Task
    path('view-tasks', views.viewTask, name="view-tasks"),

    # - UPDATE Task
    path('update-task/<str:pk>/', views.updateTask, name="update-task"),

    # - DELETE Task
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),


    # ------------------- User Registration ------------------- #
    # --------------------------------------------------------- #


    path('register', views.register, name="register"),


    # ------------------- User Login ------------------- #
    # -------------------------------------------------- #  


    path('login', views.login, name='login'),


    # ------------------- User Dashboard ------------------- #
    # ------------------------------------------------------ # 

    path('dashboard', views.dashboard, name='dashboard'),


    # ------------------- User Logout ------------------- #
    # --------------------------------------------------- # 

    path('user-logout', views.logout, name='user-logout'),

]







