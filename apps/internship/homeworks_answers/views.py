from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.internship.homeworks_answers.models import Answer, AnswerUrl
from apps.internship.homeworks_answers.serializers import AnswerSerializer, AnswerUrlSerializer


class AnswerApiViewSet(GenericViewSet,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       ):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerUrlsApiViewSet(GenericViewSet,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin
                           ):
    queryset = AnswerUrl.objects.all()
    serializer_class = AnswerUrlSerializer
