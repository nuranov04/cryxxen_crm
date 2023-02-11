import uuid

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата последнего изменения"
    )

    class Meta:
        abstract = True
        ordering = ("-created_at",)


class BaseRequest(BaseModel):
    stars = models.FloatField(
        verbose_name="stars count"
    )
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
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="created at"
    )

    class Meta:
        abstract = True


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
