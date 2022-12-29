from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Report(models.Model):
    intern = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="reports"
    )
    content = models.TextField(
        max_length=256
    )
    date = models.DateField(
        auto_now_add=True,
    )
    is_accept = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.content

