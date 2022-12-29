from django.db import models


class Homework(models.Model):
    title = models.CharField(
        max_length=256
    )
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    creator = models.ForeignKey(
        "User",
        on_delete=models.DO_NOTHING,
        related_name="creator"
    )
    type = models.ForeignKey(
        "HomeworkType",
        on_delete=models.SET_NULL,
        related_name="homework_type"
    )
    group = models.ForeignKey(
        "Class",
        on_delete=models.CASCADE,
        related_name="group_homeworks"
    )

    def __str__(self):
        return self.id, self.title

    class Meta:
        verbose_name = "Homework"
        verbose_name_plural = "Homeworks"
        ordering = ("-created_at",)


class HomeworkUrl(models.Model):
    homework = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE,
        related_name="links"
    )
    link = models.URLField()

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = "Homework Url"
        verbose_name_plural = "Homework Urls"

