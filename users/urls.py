from atexit import register
from django.urls import path
from . import views



urlpatterns = [
    path('',views.home),
    path('home',views.home,name = 'home'),
    path('register',views.register,name ='register')
]
