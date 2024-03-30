from rest_framework.serializers import ModelSerializer
from links.models import Link
from links_process.api.serializers import LinkProcessSerializer


class LinkSerializer(ModelSerializer):
    link_process = LinkProcessSerializer(read_only=True)

    class Meta:
        model = Link
        fields = '__all__'
