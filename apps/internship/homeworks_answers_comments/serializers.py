from rest_framework.serializers import ModelSerializer

from apps.internship.homeworks_answers_comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
