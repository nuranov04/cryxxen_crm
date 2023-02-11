from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.internship.groups.serializers import BunchShortInfoSerializer
from apps.internship.groups.models import Bunch
from apps.main.directions.models import Direction


class DirectionSerializer(ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class DirectionDetailSerializer(ModelSerializer):
    classes = SerializerMethodField(read_only=True)

    class Meta:
        model = Direction
        fields = "__all__"

    def get_classes(self, obj):
        queryset = Bunch.objects.filter(direction=obj).all()
        return BunchShortInfoSerializer(queryset, many=True).data
