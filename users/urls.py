from atexit import register
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('',views.home),
    path('home',views.home,name = 'home'),
    path('register',views.register,name ='register'),
    path('login',auth_view.LoginView.as_view(template_name = 'users/login.html'))
]
