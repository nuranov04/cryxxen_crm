from django.db import models

from utils.models import BaseModel


class OurMission(BaseModel):
    content = models.TextField(
        verbose_name="Our Mission"
    )

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if OurMission.objects.all().count() < 1:
            return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Our Mission"
        verbose_name_plural = "Our Mission"
