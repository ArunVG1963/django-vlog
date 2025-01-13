from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('camera/', views.camera, name='camera'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views_vlog.register, name='register'),
    path('upload', views_vlog.upload_media, name='upload'),
    
]