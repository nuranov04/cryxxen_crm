from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.main.users.managers import CustomUserManager


class User(AbstractUser):
    class UserStatusChoice(models.TextChoices):
        admin = 1
        trainer = 2
        mentor = 3
        intern = 4
        guest = 5

    status = models.CharField(
        choices=UserStatusChoice.choices,
        default=UserStatusChoice.guest,
        max_length=256
    )
    email = models.EmailField(
        unique=True
    )
    username = None
    first_name = models.CharField(
        max_length=256
    )
    last_name = models.CharField(
        max_length=256
    )
    rating = models.PositiveSmallIntegerField(
        default=10
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
