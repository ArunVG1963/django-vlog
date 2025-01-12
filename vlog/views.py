from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please check the form for errors.")
    else:
        form = UserCreationForm()
    return render(request, 'vlog/register.html', {'form': form})

# Create your views here.

def main(request):
    return render(request,'vlog/main.html')

def my_vlog(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def upload_media(request):
    return render(request, 'vlog/upload_media.html')  

def camera(request):
    return render(request,'vlog/camera.html')