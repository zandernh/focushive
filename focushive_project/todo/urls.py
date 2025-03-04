
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

    # ------------------- User Logout ------------------- #
    # --------------------------------------------------- # 

    path('user-logout', views.logout, name='user-logout'),

]







