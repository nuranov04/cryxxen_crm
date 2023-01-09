from django.contrib import admin

from apps.development.tasks.models import Task

admin.site.register(Task)

