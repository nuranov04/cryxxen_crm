from django.db import models

from apps.development.boards.models import Board


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
