from django.db import models
from django.contrib.auth import get_user_model

from apps.internship.homeworks.models import Homework

User = get_user_model()


class Answer(models.Model):
    homework = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    intern = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="intern"
    )
    description = models.CharField(
        max_length=256
    )

    def __str__(self):
        return f"{self.id} -- {self.description}"

    class Meta:
        verbose_name = "Homework Answers"
        verbose_name_plural = "Homework Answers"
