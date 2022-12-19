from django.db import models

from utils.models import BaseModel


class Service(BaseModel):
    icon = models.URLField(
        verbose_name="icon"
    )
    title = models.CharField(
        max_length=256,
        verbose_name="title"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Our Services"
        verbose_name_plural = "Our Services"
