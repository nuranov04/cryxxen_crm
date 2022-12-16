import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4(),
        max_length=7,
        unique=True,
        primary_key=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата последнего изменения"
    )

    class Meta:
        abstract = True
        ordering = ("-created_at",)

