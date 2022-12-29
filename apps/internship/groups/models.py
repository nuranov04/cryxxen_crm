from django.db import models

from apps.main.directions.models import Course


class Class(models.Model):
    title = models.CharField(
        max_length=256
    )
    duration = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="groups"
    )

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def save(self, *args, **kwargs):
        if Class.objects.filter(title=self.title).count() > 1:
            raise "You can't create two similar objects"
        return super().save(*args, **kwargs)
