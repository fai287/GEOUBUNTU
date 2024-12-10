from django.db import models

class LearningMaterial(models.Model):
    DOCUMENT = 'document'
    IMAGE = 'image'
    VIDEO = 'video'
    CONTENT_TYPE_CHOICES = [
        (DOCUMENT, 'Document'),
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='materials/files/')
    image = models.ImageField(upload_to='materials/images/', blank=True, null=True)
    video = models.FileField(upload_to='materials/videos/', blank=True, null=True)
    content_type = models.CharField(
        max_length=10,
        choices=CONTENT_TYPE_CHOICES,
        default=DOCUMENT,
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
