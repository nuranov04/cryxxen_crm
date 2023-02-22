from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.internship.homeworks.models import Homework, HomeworkUrl
from apps.internship.homeworks_answers.serializers import AnswerRetrieveSerializer
from apps.internship.homeworks_answers.models import Answer


class HomeworkUrlSerializer(ModelSerializer):
    class Meta:
        model = HomeworkUrl
        fields = "__all__"


class HomeworkSerializer(ModelSerializer):
    class Meta:
        model = Homework
        fields = (
            "id",
            "group",
            "title",
            "creator",
            "description",
            "deadline",
            "created_at",
        )


class HomeworkDetailSerializer(ModelSerializer):
    links = HomeworkUrlSerializer(many=True, read_only=True)
    answers = SerializerMethodField()

    class Meta:
        model = Homework
        fields = "__all__"

    def get_answers(self, obj):
        queryset = Answer.objects.filter(homework_id=obj.id)
        return AnswerRetrieveSerializer(queryset, many=True).data
