from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Bunch
from apps.main.directions.serializers import DirectionSerializer
from apps.internship.homeworks.serializers import HomeworkSerializer


class BunchSerializer(ModelSerializer):
    direction = DirectionSerializer()
    total_members = SerializerMethodField()

    class Meta:
        model = Bunch
        fields = (
            "id",
            "title",
            "direction",
            "members",
            "total_members",
        )

    def get_total_members(self, obj):
        return obj.members.all().count()


class BunchRetrieveSerializer(ModelSerializer):
    direction = DirectionSerializer()
    homeworks = HomeworkSerializer(many=True)

    class Meta:
        model = Bunch
        fields = "__all__"


class BunchShortInfoSerializer(ModelSerializer):
    class Meta:
        model = Bunch
        fields = (
            "id",
            "title",
            "direction",
        )

