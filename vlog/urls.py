from django.urls import path
from . import views

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
    path('edit/',views_vlog.edit_video,name="edit_video"),
    path('delete/',views_vlog.remove_video,name="remove_video")

]