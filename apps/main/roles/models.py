from django.db import models


class Role(models.Model):
    ROLE_CHOICES = (
        (1, "admin",),
        (2, "trainer"),
        (3, "mentor"),
        (4, "intern"),
        (5, "guest"),
    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ("id",)
