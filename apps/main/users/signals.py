from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.main.users.tasks import send_mail

User = get_user_model()


@receiver(post_save, sender=User)
def send_message_after_change_status(sender, instance, created, *args, **kwargs):
    user_status_dict = {
        1: "admin",
        2: "trainer",
        3: "mentor",
        4: "intern",
        5: "guest",
    }
    if not created:
        send_mail.delay(
            mail=instance.email,
            first_name=instance.first_name,
            last_name=instance.last_name,
            user_status=user_status_dict[int(instance.status)]
        )
