from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.main.users.managers import CustomUserManager


class User(AbstractUser):

    status = models.ManyToManyField(
        "Role",
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
        default=100
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


