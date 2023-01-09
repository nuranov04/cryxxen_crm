from django.contrib.auth import get_user_model
from django.db import models

from apps.development.statuses.models import Status
from utils.models import BaseModel
from apps.development.boards.models import Board

User = get_user_model()


class Task(BaseModel):
    title = models.CharField(
        max_length=256
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING,
        related_name="status_tasks"
    )
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name="board_tasks"
    )
    members = models.ManyToManyField(
        User,
        related_name="task_members"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Board Task"
        verbose_name_plural = "Boards Tasks"
