from django.urls import path
from . import views

# ------------------------------------- #
# --- --- APPLICATION URL PATHS --- --- #
# ------------------------------------- #

urlpatterns = [

# -------------------------------- #
# --- --- --- HOMEPAGE --- --- --- #

    path('', views.home, name=''),

# --------------------------------------- #
# --- --- --- REGISTER A USER --- --- --- #

    path('register', views.register, name='register'),

# ----------------------------- #
# --- --- --- LOGIN --- --- --- #

    path('login', views.login, name='login'),

# --------------------------------- #
# --- --- --- DASHBOARD --- --- --- #

    path('dashboard', views.dashboard, name='dashboard'),

# ---------------------------------- #
# --- --- PROFILE MANAGEMENT --- --- #

    path('profile-management', views.profile_management, name='profile-management'),

# ------------------------------ #
# --- --- DELETE ACCOUNT --- --- #

    path('delete-account', views.delete_account, name='delete-account'),

# ---------------------------------------------- #
# --- --- CRUD OPERATIONS OF APPLICATION --- --- #
# ---------------------------------------------- #

# ---------------------------------- #
# --- --- --- CREATE TASK--- --- --- #

    path('create-task', views.createTask, name='create-task'),

# -------------------------------- #
# --- --- --- READ TASK--- --- --- #

    path('view-tasks', views.viewTasks, name='view-tasks'),

# ---------------------------------- #
# --- --- --- UPDATE TASK--- --- --- #

    path('update-task/<str:pk>/<str:title>/', views.updateTask, name='update-task'),

# ---------------------------------- #
# --- --- --- DELETE TASK--- --- --- #

    path('delete-task/<str:pk>/<str:title>/', views.deleteTask, name='delete-task'),

# ---------------------------------------------- #
# ---------------------------------------------- #
# ---------------------------------------------- #

# ------------------------------ #
# --- --- --- LOGOUT --- --- --- #

    path('logout', views.logout, name='logout'),

]