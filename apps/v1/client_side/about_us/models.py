from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields

from utils.models import BaseModel


class AboutUs(BaseModel):
    content = models.TextField(
        verbose_name="About Us"
    )
    image = models.FileField()

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if AboutUs.objects.all().count() < 1:
            return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("About Us", )
        verbose_name_plural = _("About Us", )
