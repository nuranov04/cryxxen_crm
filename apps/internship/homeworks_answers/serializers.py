from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.internship.homeworks_answers.models import Answer, AnswerUrl
from apps.internship.homeworks_answers_comments.models import Comment
from apps.internship.homeworks_answers_comments.serializers import CommentSerializer


class AnswerUrlSerializer(ModelSerializer):
    class Meta:
        model = AnswerUrl
        fields = "__all__"


class AnswerRetrieveSerializer(ModelSerializer):
    urls = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Answer
        fields = (
            "id",
            "intern",
            "description",
            "urls",
            "comments",
        )

    def get_comments(self, obj):
        queryset = Comment.objects.filter(answer_id=obj.id).all()
        return CommentSerializer(queryset, many=True).data

    def get_urls(self, obj):
        queryset = AnswerUrl.objects.filter(answer_id=obj.id)
        return AnswerUrlSerializer(queryset, many=True).data


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
