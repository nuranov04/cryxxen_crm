from django.contrib.auth import get_user_model
from django.db import models

from apps.main.directions.models import Direction

User = get_user_model()


class Bunch(models.Model):
    title = models.CharField(
        max_length=256
    )
    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name="classes"
    )
    members = models.ManyToManyField(
        User,
        related_name="members",
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    # def save(self, *args, **kwargs):
    #     if Bunch.objects.filter(title=self.title).count() >= 1:
    #         raise Exception("You can't create two similar objects")
    #     return super().save(*args, **kwargs)
