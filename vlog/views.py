from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Video, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

# register user
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

# function to access main.html
def main(request):
    return render(request,'vlog/index.html')

# test function
def my_vlog(request):
    return HttpResponse("<h1>Hello, World!</h1>")

# upload media
def upload_media(request):
    return render(request, 'vlog/upload_media.html')  

# Camera functionality
def camera(request):
    return render(request,'vlog/camera.html')

# create video list for main webpage
# @login_required

def video_list(request):
    """
    View to display a list of all videos
    """
    videos = Video.objects.all()
    return render(request, 'vlog/show.html', {'videos': videos})

def video_entry(request):
    return render(request, 'vlog/create.html')

def process_video_entry(request):
    """
    View to create a new video
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_file = request.POST.get('video_file')
        video = Video(title=title, description=description, video_file=video_file, user=request.user)
        video.save()
        return render(request,'vlog/index.html')
    else:
        return HttpResponse("Invalid request method.")    


def edit_video(request,pk):
    videos = Video.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            videos.title = request.POST['title']
            videos.description = request.POST['description']
            videos.video_file = request.POST['video_file']
            videos.save()   
            return redirect('video_list')
    context = {
        'videos': videos,
    }

    return render(request,'vlog/edit.html',context)

def remove_video(request, pk):
   videos = Video.objects.get(id=pk)
   
   if request.method == 'POST':
       videos.delete()
       return redirect('video_list')

   context = {
        'videos': videos,
    }

   return render(request, 'vlog/delete.html', context)

def get_involved(request):
   return render(request,'vlog/getinvolved.html') 