from django.db import models

from utils.models import BaseModel


class AboutUs(BaseModel):
    content = models.TextField(verbose_name="content")
    image = models.FileField()

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if AboutUs.objects.all().count() < 1:
            return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "About Us",
        verbose_name_plural = "About Us"
