from django.db import models

from apps.main.directions.models import Direction


class Bunch(models.Model):
    title = models.CharField(
        max_length=256
    )
    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name="classes"
    )

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Class"

    def save(self, *args, **kwargs):
        if Bunch.objects.filter(title=self.title).count() > 1:
            raise "You can't create two similar objects"
        return super().save(*args, **kwargs)
