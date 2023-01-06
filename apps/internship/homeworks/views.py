from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.internship.homeworks.models import Homework, HomeworkUrl
from apps.internship.homeworks.serializers import HomeworkSerializer, HomeworkUrlSerializer, HomeworkDetailSerializer
from utils.permissions import GrMentor


class HomeWorkApiViewSet(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = Homework.objects.select_related("creator", "group").all()
    serializer_class = HomeworkSerializer
    permission_classes = [GrMentor]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return HomeworkDetailSerializer
        return HomeworkSerializer


class HomeworkUrlApiViewSet(GenericViewSet,
                            mixins.CreateModelMixin):
    queryset = HomeworkUrl.objects.all()
    serializer_class = HomeworkUrlSerializer
    permission_classes = [GrMentor]
