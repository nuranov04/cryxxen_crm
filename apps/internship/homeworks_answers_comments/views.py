from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Comment
from .serializers import CommentSerializer


class CommentApiViewSet(GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
