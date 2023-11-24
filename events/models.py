from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    image_poster = models.URLField(max_length=500)
    image_event = models.URLField(max_length=500)
    entry = models.CharField(max_length=50)
    summary = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title
