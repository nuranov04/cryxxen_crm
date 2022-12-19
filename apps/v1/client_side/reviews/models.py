from django.db import models

from utils.models import BaseRequest


class Review(BaseRequest):
    some_field = models.CharField(
        max_length=256,
        verbose_name="some field"
    )

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ("-created_at",)

