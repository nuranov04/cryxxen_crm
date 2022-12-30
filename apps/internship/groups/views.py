from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from utils.permissions import IsIntern
from apps.internship.groups.models import Bunch
from apps.internship.groups.serializers import BunchSerializer, BunchRetrieveSerializer


class BunchApiViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Bunch.objects.all().select_related("direction").prefetch_related("members")
    serializer_class = BunchSerializer
    permission_classes = [IsAuthenticated, IsIntern]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BunchRetrieveSerializer
        return BunchSerializer
