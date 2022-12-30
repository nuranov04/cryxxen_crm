from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Homework, HomeworkUrl
from .serializers import HomeworkSerializer, HomeworkUrlSerializer, HomeworkDetailSerializer


class HomeWorkApiViewSet(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = Homework.objects.select_related("creator", "type", "group").all()
    serializer_class = HomeworkSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return HomeworkDetailSerializer
        return HomeworkSerializer


class HomeworkUrlApiViewSet(GenericViewSet,
                            mixins.CreateModelMixin):
    queryset = HomeworkUrl.objects.all()
    serializer_class = HomeworkUrlSerializer

