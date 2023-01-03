from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action

from utils import permissions
from apps.internship.groups.models import Bunch
from apps.internship.groups.serializers import BunchSerializer, BunchRetrieveSerializer


class BunchApiViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Bunch.objects.all().prefetch_related("members").select_related("direction")
    serializer_class = BunchSerializer
    permission_classes = [permissions.IsIntern]

    def get_permissions(self):
        if self.action == "list":
            return [permissions.AllowAny()]
        return [permissions.GrMentor()]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BunchRetrieveSerializer
        return BunchSerializer
