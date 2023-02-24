from rest_framework import mixins, viewsets

from apps.internship.homeworks.models import Homework, HomeworkUrl
from apps.internship.homeworks.serializers import HomeworkSerializer, HomeworkUrlSerializer, HomeworkDetailSerializer
from utils.permissions import GrMentor


class HomeWorkApiViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.select_related("creator", "group").all()
    serializer_class = HomeworkSerializer
    permission_classes = [GrMentor]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return HomeworkDetailSerializer
        return HomeworkSerializer

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)


class HomeworkUrlApiViewSet(viewsets.GenericViewSet,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            ):
    queryset = HomeworkUrl.objects.all()
    serializer_class = HomeworkUrlSerializer
    permission_classes = [GrMentor]
