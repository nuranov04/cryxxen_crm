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
