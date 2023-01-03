from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.internship.homeworks_answers_comments.models import Comment
from apps.internship.homeworks_answers_comments.serializers import CommentSerializer
from utils.permissions import GrInter


class CommentApiViewSet(GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [GrInter]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
