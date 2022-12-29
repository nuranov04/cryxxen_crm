from django.db import models

from apps.internship.groups.models import Class


class HomeworkType(models.Model):
    title = models.CharField(
        max_length=256
    )
    group = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="group_homeworks_types"
    )

    def __str__(self):
        return self.title, self.group.title

    class Meta:
        verbose_name = "Типы Домашних заданий"
        verbose_name_plural = "Типы Домашних заданий"
        ordering = ("title",)
