from django.db import models
from django.conf import settings
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    featured_image= models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Changed to ImageField
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
