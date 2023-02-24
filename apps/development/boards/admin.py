from django.contrib import admin

from apps.development.boards.models import Board, Task, Status

admin.site.register(Board)
admin.site.register(Task)
admin.site.register(Status)
