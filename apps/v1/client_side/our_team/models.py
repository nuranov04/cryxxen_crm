from django.db import models

from utils.models import BaseModel


class Team(BaseModel):
    class PositionTypeChoice(models.TextChoices):
        front_end = "Front-end Developer"
        back_end = "Back-end Developer"
        designer = "Designer"
        android = "Android Developer"
        ios = "Ios Developer"
        tech_lead = "Tech Lead"
        ceo = "CEO"
        pm = "PM"

    first_name = models.CharField(
        verbose_name="first name",
        max_length=256
    )
    last_name = models.CharField(
        verbose_name="last name",
        max_length=256
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="age"
    )
    image = models.ImageField(
        verbose_name="image"
    )
    position = models.CharField(
        max_length=256,
        choices=PositionTypeChoice.choices,
        verbose_name="position"
    )

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"
        ordering = ("created_at",)
