from rest_framework.serializers import ModelSerializer

from apps.v1.client_side.our_services.models import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

