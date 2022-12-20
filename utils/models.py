import uuid

from django.db import models


class BaseModel(models.Model):
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


class BaseRequest(BaseModel):
    stars = models.FloatField(
        verbose_name="stars count"
    )
    first_name = models.CharField(
        max_length=256,
        verbose_name="first name"
    )
    last_name = models.CharField(
        max_length=256,
        verbose_name="last name"
    )
    phone_number = models.CharField(
        max_length=256,
        verbose_name="phone number"
    )
    email = models.EmailField(
        verbose_name="email"
    )
    message = models.TextField(
        verbose_name="message"
    )

    class Meta:
        abstract = True
