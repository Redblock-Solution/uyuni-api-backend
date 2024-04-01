from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from playlists.api.serializers import PlaylistSerializer
from playlists.models import Playlist


class PlaylistsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        id = self.request.user.id
        return Playlist.objects.filter(user_id=id)



        
