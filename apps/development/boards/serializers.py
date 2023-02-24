from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Board, Task, Status
from apps.main.users.serializers import UserShortInfoSerializer


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class StatusSerializer(ModelSerializer):
    status_tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Status
        fields = "__all__"

    def get_tasks(self, obj):
        data = Task.objects.filter(status=obj).all()
        return TaskSerializer(data, many=True).data


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class BoardRetrieveSerializer(ModelSerializer):
    statuses = SerializerMethodField(read_only=True)
    members = UserShortInfoSerializer(many=True)

    class Meta:
        model = Board
        fields = "__all__"

    def get_statuses(self, obj):
        data = Status.objects.filter(board_id=obj.id)
        return StatusSerializer(data, many=True).data
