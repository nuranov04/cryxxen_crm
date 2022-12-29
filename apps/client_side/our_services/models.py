from django.db import models

from utils.models import BaseModel


class Service(BaseModel):
    icon = models.FileField(
        verbose_name="icon",
        upload_to="icons/"
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
