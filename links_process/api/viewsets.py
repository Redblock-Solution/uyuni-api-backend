from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from links_process.api.serializers import LinkProcessSerializer
from links_process.models import LinksProcess


class LinksProcessViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LinksProcess.objects.all()
    serializer_class = LinkProcessSerializer

    def get_queryset(self):
        id = self.request.user.id
        return LinksProcess.objects.filter(user_id=id)