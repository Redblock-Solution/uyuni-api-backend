from django.db import models

from playlists.models import Playlist
from django.contrib.auth.models import User

class Link(models.Model):
    playlists_id = models.ForeignKey(Playlist, related_name='links', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(max_length=255)
    view_player = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
