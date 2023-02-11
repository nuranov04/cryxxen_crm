from django.db import models

from utils.models import BaseModel, SingletonModel


class AboutUs(BaseModel, SingletonModel):
    content = models.TextField(
        verbose_name="content"
    )
    image = models.FileField(
        upload_to="images/about_us/"
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "About Us",
        verbose_name_plural = "About Us"


class AboutInternship(BaseModel, SingletonModel):
    content = models.TextField(
        verbose_name="content"
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "About Internship"
        verbose_name_plural = "About Internship"
