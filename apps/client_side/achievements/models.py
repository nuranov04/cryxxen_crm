from django.db import models

from utils.models import BaseModel


class Achievement(BaseModel):
    file = models.ImageField(
        verbose_name="file",
        upload_to="images/achievements/"
    )
    content = models.CharField(
        max_length=256,
        verbose_name="content"
    )

    def __str__(self):
        return str(self.id)
