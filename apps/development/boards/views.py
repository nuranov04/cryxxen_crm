from rest_framework import viewsets, permissions

from .models import Board, Task, Status
from .serializers import BoardSerializer, BoardRetrieveSerializer, StatusSerializer, TaskSerializer


class BoardApiViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BoardRetrieveSerializer
        return BoardSerializer

    def get_queryset(self):
        return Board.objects.prefetch_related("members").filter(members__id=self.request.user.id).all()


class TaskApiViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class StatusApiViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
