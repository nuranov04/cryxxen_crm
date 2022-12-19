from django.db import models

from utils.models import BaseModel


class Bid(BaseModel):
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
    stars = models.PositiveSmallIntegerField(
        verbose_name="stars count"
    )

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Bid"
        verbose_name_plural = "Bids"
        ordering = ("-created_at",)
