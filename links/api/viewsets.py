from rest_framework.viewsets import ModelViewSet

from links.api.serializers import LinkSerializer
from links.models import Link


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
