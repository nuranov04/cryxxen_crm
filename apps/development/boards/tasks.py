from django.core.mail import EmailMessage
from django.conf import settings

from celery import shared_task

from apps.development.boards.models import Task


@shared_task
def send_mail(task_id):
    try:
        # Получение задачи с id task_id, с выборкой связанной модели Board и загрузкой всех участников задачи
        task = Task.objects.select_related("board").prefetch_related("members").get(id=task_id)

        # Получение всех участников задачи
        members = task.members.all()

        # Получение заголовка доски, на которой находится задача
        board_title = task.board.title  # get board title

        # Формирование списка электронных адресов всех участников задачи
        members_emails_list = [member.email for member in members]

        # Формирование сообщения, которое будет отправлено на электронную почту участникам задачи
        message = f'Привет, у тебя новый таск в проекте "{board_title}" '

        # Создание объекта EmailMessage для отправки сообщения
        email = EmailMessage(
            subject=f"{board_title}---{task.title}",
            body=message,
            to=members_emails_list,
            from_email=settings.EMAIL_HOST_USER
        )
        email.send()
    except Task.DoesNotExist:
        print("Такого таска нет в базе данных")
