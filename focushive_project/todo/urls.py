
from django.urls import path
from . import views

urlpatterns = [

    # ------------------- Homepage ------------------------- #
    # ------------------------------------------------------ #

    path('', views.home, name=""),

    # ------------------- User Registration ------------------- #
    # --------------------------------------------------------- #

    path('register', views.register, name="register"),

    # ------------------- User Login ------------------- #
    # -------------------------------------------------- #  

    path('login', views.login, name='login'),

    # ------------------- User Dashboard ------------------- #
    # ------------------------------------------------------ # 

    path('dashboard', views.dashboard, name='dashboard'),

    # ------------------- CREATE TASK ---------------------- #
    # ------------------------------------------------------ # 

    path('create-task', views.createTask, name='create-task'),

    # --------------------- READ TASK ---------------------- #
    # ------------------------------------------------------ # 

    path('view-task', views.viewTask, name='view-task'),

    # --------------------- UPDATE TASK -------------------- #
    # ------------------------------------------------------ #

    path('update-task/<str:pk>/<str:title>/', views.updateTask, name='update-task'),
    
    # --------------------- DELETE TASK -------------------- #
    # ------------------------------------------------------ #

    path('delete-task/<str:pk>/<str:title>/', views.deleteTask, name='delete-task'),

    # ------------------- User Logout ------------------- #
    # --------------------------------------------------- # 

    path('user-logout', views.logout, name='user-logout'),

]







