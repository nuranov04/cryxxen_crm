from utils.models import BaseRequest


class Review(BaseRequest):
    pass

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ("-created_at",)

