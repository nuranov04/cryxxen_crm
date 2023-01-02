from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action

from utils.permissions import IsIntern
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
    permission_classes = [IsIntern]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BunchRetrieveSerializer
        return BunchSerializer

    @action(
        detail=False, methods=["get"]
    )
    def get_user_groups(self, request):
        return Bunch.objects.filter(members_in=request.user)
