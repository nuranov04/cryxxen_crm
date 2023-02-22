from django.core.mail import EmailMessage
from django.conf import settings

from celery import shared_task


@shared_task
def send_mail(first_name, last_name, mail, user_status):
    message = 'Привет, теперь ты являешься "{status}" нашего небольшого дружного коллектива CRYXXEN)\nЖелаем тебе больших результатов и терпения!'

    email = EmailMessage(
        subject=f" Hello {first_name} {last_name} your status is changed",
        body=message.format(status=user_status),
        to=[mail],
        from_email=settings.EMAIL_HOST_USER
    )
    email.send()
