from rest_framework.serializers import ModelSerializer

from links.api.serializers import LinkSerializer
from playlists.models import Playlist


class PlaylistSerializer(ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = Playlist
        fields = '__all__'