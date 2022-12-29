from django.contrib import admin

from .models import Homework, HomeworkUrl
from apps.internship.homeworks_answers.admin import AnswerInline


class HomeworkUrlInline(admin.TabularInline):
    model = HomeworkUrl
    extra = 1


@admin.register(Homework)
class HomeWorkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "deadline",
    )
    inlines = [
        HomeworkUrlInline,
        AnswerInline,
    ]


class HomeworkInline(admin.TabularInline):
    model = Homework
    extra = 1
