from django.urls import path
from . import views

urlpatterns = [
    path('/', views.main, name='main'),
    path('upload-media/', views.upload_media, name='upload_media'),
    path('camera/', views.camera, name='camera'),
]