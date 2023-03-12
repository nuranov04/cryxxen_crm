import logging

from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.conf import settings

from celery import shared_task

from apps.internship.groups.models import Bunch

User = get_user_model()


@shared_task
def send_notification_to_email(group_id, homework_title, deadline, homework_url):
    try:
        members_query = Bunch.objects.get(id=group_id).members.all()
        message = "Hi {first_name} {last_name}, you have new homework!\nDeadline is {deadline}"
        for member in members_query:
            mail = EmailMessage(
                subject=homework_title,
                body=message.format(
                    first_name=member.first_name,
                    last_name=member.last_name,
                    homework_url=homework_url,
                    deadline=deadline
                ),
                to=[member.email],
                from_email=settings.EMAIL_HOST_USER
            )
            mail.send()
    except Bunch.DoesNotExist:
        logging.debug(f"Группы {group_id} не существует")
