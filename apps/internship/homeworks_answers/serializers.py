from rest_framework.serializers import ModelSerializer

from apps.internship.homeworks_answers.models import Answer, AnswerUrl


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class AnswerUrlSerializer(ModelSerializer):
    class Meta:
        model = AnswerUrl
        fields = "__all__"
