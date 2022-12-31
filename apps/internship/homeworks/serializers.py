from rest_framework.serializers import ModelSerializer

from apps.internship.homeworks.models import Homework, HomeworkUrl
from apps.internship.homeworks_answers.serializers import AnswerSerializer


class HomeworkUrlSerializer(ModelSerializer):
    class Meta:
        model = HomeworkUrl
        fields = "__all__"


class HomeworkSerializer(ModelSerializer):
    class Meta:
        model = Homework
        fields = (
            "id",
            "title",
            "description",
            "deadline",
            "created_at",
            "type",
        )


class HomeworkDetailSerializer(ModelSerializer):
    links = HomeworkUrlSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Homework
        fields = "__all__"



