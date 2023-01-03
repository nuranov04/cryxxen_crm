from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.internship.groups.models import Bunch
from apps.internship.homeworks.models import Homework
from apps.main.directions.serializers import DirectionSerializer
from apps.internship.homeworks.serializers import HomeworkSerializer
from apps.main.users.serializers import UserShortInfoSerializer


class BunchSerializer(ModelSerializer):
    direction = DirectionSerializer()
    total_members = SerializerMethodField()

    class Meta:
        model = Bunch
        fields = (
            "id",
            "title",
            "direction",
            "total_members",
        )

    def get_total_members(self, obj):
        return obj.members.all().count()


class BunchRetrieveSerializer(ModelSerializer):
    direction = DirectionSerializer()
    homeworks = SerializerMethodField(read_only=True)
    members = SerializerMethodField(read_only=True)

    class Meta:
        model = Bunch
        fields = "__all__"

    def get_members(self, obj):
        serializer = UserShortInfoSerializer(obj.members, many=True)
        return serializer.data

    def get_homeworks(self, obj):
        data = Homework.objects.filter(group__id=obj.id).all()
        serializer = HomeworkSerializer(data, many=True)
        return serializer.data


class BunchShortInfoSerializer(ModelSerializer):
    class Meta:
        model = Bunch
        fields = (
            "id",
            "title",
            "direction",
        )
