from rest_framework.serializers import ModelSerializer

from apps.internship.homeworks_types.models import HomeworkType


class HomeworkTypeSerializer(ModelSerializer):
    class Meta:
        model = HomeworkType
        fields = "__all__"
