from django.db import models


class Direction(models.Model):
    title = models.CharField(
        max_length=256
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Direction"
        verbose_name_plural = "Directions"

    def save(self, *args, **kwargs):
        if Course.objects.filter(title=self.title).count() > 1:
            raise "You can't create two similar objects"
        return super().save(*args, **kwargs)
