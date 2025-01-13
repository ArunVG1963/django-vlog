"""
URL configuration for arunproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from vlog import views as views_vlog

urlpatterns = [
    path('', views_vlog.main, name='home'),
    path('admin/', admin.site.urls,name='admin'),
    path('camera', views_vlog.camera, name='camera'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views_vlog.register, name='register'),
    path('upload', views_vlog.upload_media, name='upload'),
    path('video-entry/',views_vlog.video_entry, name='video_entry'),
    path('process-video-entry/',views_vlog.process_video_entry, name='process_video_entry'),
    path('show/',views_vlog.video_list, name="video_list"),
    path('edit/<str:pk>/',views_vlog.edit_video,name="edit_video"),
    path('delete/<str:pk>/',views_vlog.remove_video,name="remove_video")

]

