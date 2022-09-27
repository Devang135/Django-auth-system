from atexit import register
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('',views.home),
    path('home',views.home,name = 'home'),
    path('register',views.register,name ='register'),
    path('profile',views.profile,name ='profile'),
    path('login',auth_view.LoginView.as_view(template_name = 'users/login.html'),name= 'login'),
    path('logout',auth_view.LogoutView.as_view(template_name = 'users/logout.html'),name ='logout'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='passwords/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="passwords/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name='passwords/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", views.password_reset_request, name="password_reset")
]
