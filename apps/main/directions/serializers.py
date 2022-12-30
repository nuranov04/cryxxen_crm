from rest_framework.serializers import ModelSerializer

from apps.main.directions.models import Direction


class DirectionSerializer(ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"
