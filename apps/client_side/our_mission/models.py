from django.db import models

from utils.models import BaseModel, SingletonModel


class OurMission(BaseModel, SingletonModel):
    content = models.TextField(
        verbose_name="Our Mission"
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Our Mission"
        verbose_name_plural = "Our Mission"
