from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.internship.groups.models import Bunch
from apps.internship.homeworks.models import Homework
from apps.internship.homeworks.serializers import HomeworkSerializer
from apps.main.users.serializers import UserShortInfoSerializer


class BunchSerializer(ModelSerializer):
    total_members = SerializerMethodField()
    total_mentors = SerializerMethodField()

    class Meta:
        model = Bunch
        fields = (
            "id",
            "title",
            "direction",
            "mentors",
            "members",
            "total_mentors",
            "total_members",
        )

    def get_total_members(self, obj):
        return obj.members.all().count()

    def get_total_mentors(self, obj):
        return obj.mentors.all().count()


class BunchRetrieveSerializer(BunchSerializer):
    homeworks = SerializerMethodField(read_only=True)
    members = SerializerMethodField(read_only=True)
    mentors = UserShortInfoSerializer(many=True, read_only=True)

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
    total_members = SerializerMethodField(read_only=True)
    total_mentors = SerializerMethodField(read_only=True)

    class Meta:
        model = Bunch
        fields = (
            "id",
            "title",
            "mentors",
            "total_members",
            "total_mentors",
            "members",
        )

    def get_total_members(self, obj):
        return obj.members.all().count()

    def get_total_mentors(self, obj):
        return obj.mentors.all().count()

