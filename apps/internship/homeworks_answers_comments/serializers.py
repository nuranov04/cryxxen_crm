from rest_framework.serializers import ModelSerializer

from apps.internship.homeworks_answers_comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields = ("intern", "created_at",)
        fields = (
            "answer",
            "comment",
        )
