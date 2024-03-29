from rest_framework.viewsets import ModelViewSet

from utils import permissions
from apps.internship.groups.models import Bunch
from apps.internship.groups.serializers import BunchSerializer, BunchRetrieveSerializer


class BunchApiViewSet(ModelViewSet):
    queryset = Bunch.objects.all().prefetch_related("members", "mentors").select_related("direction").all()
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
