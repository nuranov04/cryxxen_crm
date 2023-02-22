from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.internship.homeworks.models import Homework
from apps.internship.homeworks.tasks import send_notification_to_email


@receiver(post_save, sender=Homework)
def send_notification(sender, instance, created, *args, **kwargs):
    if created:
        deadline = instance.deadline.strftime("%Y.%m.%d")
        pass
        send_notification_to_email.delay(
            # members_query=instance.group.members.all(),
            group_id=instance.group.id,
            homework_title=instance.title,
            deadline=str(deadline),
            homework_url="youtube.com"
        )
