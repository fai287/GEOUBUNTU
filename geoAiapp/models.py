from django.db import models
from django.contrib.auth.models import User  # Import the default User model
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, null=True, blank=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

### is the class for the comment section 

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.created_at}"