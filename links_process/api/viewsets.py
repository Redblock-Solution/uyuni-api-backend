from rest_framework.viewsets import ModelViewSet

from links_process.api.serializers import LinkProcessSerializer
from links_process.models import LinksProcess


class LinksProcessViewSet(ModelViewSet):
    queryset = LinksProcess.objects.all()
    serializer_class = LinkProcessSerializer
