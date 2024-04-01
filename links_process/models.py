from django.db import models
from django.contrib.auth.models import User

class LinksProcess(models.Model):
    link_id = models.OneToOneField('links.Link', on_delete=models.CASCADE, related_name='link_process')
    title = models.CharField(max_length=255)
    views = models.IntegerField()
    length = models.IntegerField()
    channel = models.CharField(max_length=255)
    channel_url = models.CharField(max_length=255)
    video_id = models.CharField(max_length=255)
    thumbnail_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title