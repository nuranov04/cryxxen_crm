from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.main.roles.models import Role
from apps.main.users.managers import CustomUserManager


class User(AbstractUser):
    status = models.ForeignKey(
        Role,
        on_delete=models.DO_NOTHING,
        related_name="users",
        blank=True, null=True,
        default=5,
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


