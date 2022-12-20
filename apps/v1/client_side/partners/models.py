from django.db import models

from utils.models import BaseModel


class Partner(BaseModel):
    title = models.CharField(
        max_length=256,
        verbose_name="company's title"
    )
    ordering = models.PositiveSmallIntegerField(
        verbose_name="ordering"
    )
    image = models.FileField(
        verbose_name="logo"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
        ordering = ("ordering",)
