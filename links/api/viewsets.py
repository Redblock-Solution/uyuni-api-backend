from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from pytube import YouTube

from links.api.serializers import LinkSerializer
from links.models import Link
from links_process.models import LinksProcess
from playlists.models import Playlist


class LinkViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get_queryset(self):
        id = self.request.user.id
        validate_link = Playlist.objects.filter(user_id=id)
        if validate_link == False:
            return []
        
        return Link.objects.filter()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.validated_data.get('url')

        try:
            yt = YouTube(url)

            link_process_data = {
                'title': yt.title,
                'views': yt.views,
                'length': yt.length,
                'channel': yt.author,
                'channel_url': yt.channel_url,
                'video_id': yt.video_id,
                'thumbnail_url': yt.thumbnail_url
            }

            self.perform_create(serializer)
            link_instance = serializer.instance
            LinksProcess.objects.create(link_id=link_instance, **link_process_data)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)