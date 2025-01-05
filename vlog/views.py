from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def main(request):
    return render(request,'vlog/main.html')

def my_vlog(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def upload_media(request):
    return render(request, 'vlog/upload_media.html')  

def camera(request):
    return render(request,'vlog/camera.html')