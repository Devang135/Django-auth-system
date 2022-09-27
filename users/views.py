from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.urls import reverse




# Create your views here.
def home(request):
    return render(request,'users/home.html')

def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        username = form.cleaned_data.get('username')
        messages.success(request,f'Hi{username} Your account is created successfully')
        return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

def profile(request):
    return render(request,'users/profile.html')


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users/home.html'))