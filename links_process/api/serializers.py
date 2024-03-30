from rest_framework.serializers import ModelSerializer
from links_process.models import LinksProcess


class LinkProcessSerializer(ModelSerializer):
    class Meta:
        model = LinksProcess
        fields = '__all__'
