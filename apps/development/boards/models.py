from django.contrib.auth import get_user_model
from django.db import models

from utils.models import BaseModel

User = get_user_model()


class Board(BaseModel):
    title = models.CharField(
        unique=True,
        max_length=256
    )
    is_completed = models.BooleanField(
        default=False
    )
    members = models.ManyToManyField(
        User,
        related_name="developers"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"


class Status(models.Model):
    title = models.CharField(
        max_length=256
    )
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name="statuses"
    )
    color = models.CharField(
        max_length=256,
        default="#fff"  # white color
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Board status"
        verbose_name_plural = "Board statuses"


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
