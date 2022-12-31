from django.contrib import admin

from apps.internship.homeworks_answers.models import Answer
from apps.internship.homeworks_answers_comments.admin import CommentInline


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "homework",
        "description",
    )
    inlines = [
        CommentInline
    ]
