from django.db import models

from utils.models import BaseModel


class Project(BaseModel):
    image = models.FileField(
        verbose_name="project's logo"
    )
    title = models.CharField(
        verbose_name="project's title",
        max_length=256
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Our project"
        verbose_name_plural = "Our projects"
