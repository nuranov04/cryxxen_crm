from rest_framework.viewsets import ModelViewSet

from utils.permissions import GrTrainer, IsAdmin
from .models import Direction
from .serializers import DirectionSerializer, DirectionDetailSerializer


class DirectionApiViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [GrTrainer]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DirectionDetailSerializer
        return DirectionSerializer

    def get_permissions(self):
        if self.action in ("create", "update", "destroy"):
            return [IsAdmin()]
        return [GrTrainer()]
