from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.internship.homeworks_answers_comments.models import Comment
from apps.internship.homeworks_answers_comments.serializers import CommentSerializer


class CommentApiViewSet(GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
