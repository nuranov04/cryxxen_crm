from django.contrib.auth import get_user_model
from django.db import models

from apps.internship.groups.models import Bunch

User = get_user_model()


class Homework(models.Model):
    title = models.CharField(
        max_length=256
    )
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="creator"
    )
    group = models.ForeignKey(
        Bunch,
        on_delete=models.CASCADE,
        related_name="homeworks"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Homework"
        verbose_name_plural = "Homeworks"
        ordering = ("-created_at",)


class HomeworkUrl(models.Model):
    homework = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE,
        related_name="links"
    )
    link = models.URLField()

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = "Homework Url"
        verbose_name_plural = "Homework Urls"
