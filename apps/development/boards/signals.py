from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.development.boards import models
from apps.development.boards.tasks import send_mail


@receiver(post_save, sender=models.Task)
def send_message_after_create(sender, instance: models.Task, created: list, *args, **kwargs):
    if created:
        send_mail.delay(instance.id)
