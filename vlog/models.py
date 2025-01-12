from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Video(models.Model):
    """
    Model for a video.
    """
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.title} | written by {self.user}"

class Comment(models.Model):
    """
    Model for a comment on a video.
    """
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"

