from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin

from apps.internship.homeworks_answers.models import Answer, AnswerUrl
from apps.internship.homeworks_answers.serializers import AnswerSerializer, AnswerUrlSerializer


class AnswerApiViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerUrlApiViewSet(GenericViewSet,
                          CreateModelMixin):
    queryset = AnswerUrl.objects.all()
    serializer_class = AnswerUrlSerializer
