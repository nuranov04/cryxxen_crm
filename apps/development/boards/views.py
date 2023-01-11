from rest_framework import viewsets, mixins

from utils.permissions import IsTrainer
from .models import Board, Task, Status
from .serializers import BoardSerializer, BoardRetrieveSerializer, StatusSerializer, TaskSerializer


class BoardApiViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsTrainer]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BoardRetrieveSerializer
        return BoardSerializer

    def get_queryset(self):
        return Board.objects.prefetch_related("members").filter(members=self.request.user).all()


class TaskApiViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class StatusApiViewSet(viewsets.GenericViewSet,
                       mixins.CreateModelMixin):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
