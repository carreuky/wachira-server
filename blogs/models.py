from django.db import models
from django.conf import settings
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    featured_image = models.URLField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
