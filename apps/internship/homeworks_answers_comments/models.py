from django.contrib.auth import get_user_model
from django.db import models

from apps.internship.homeworks_answers.models import Answer

User = get_user_model()


class Comment(models.Model):
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    comment = models.CharField(
        max_length=256,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Answer Comments"
        verbose_name_plural = "Answers Comments"
        ordering = ("-created_at",)
