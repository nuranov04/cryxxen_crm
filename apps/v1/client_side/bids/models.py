from django.db import models

from utils.models import BaseRequest


class Bid(BaseRequest):
    class InterestTypeChoice(models.TextChoices):
        partner = "partner"
        internship = "internship"
        order_project = "order project"

    stars = None

    type = models.CharField(
        max_length=256,
        choices=InterestTypeChoice.choices,
        verbose_name="request type"
    )

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Bid"
        verbose_name_plural = "Bids"
        ordering = ("-created_at",)
