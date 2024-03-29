from rest_framework.viewsets import ModelViewSet

from playlists.api.serializers import PlaylistSerializer
from playlists.models import Playlist


class PlaylistsViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
