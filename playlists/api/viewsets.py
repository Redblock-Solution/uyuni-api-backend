from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from playlists.api.serializers import PlaylistSerializer
from playlists.models import Playlist


class PlaylistsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
