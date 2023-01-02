from django.contrib import admin

from apps.internship.homeworks_answers.models import Answer, AnswerUrl
from apps.internship.homeworks_answers_comments.admin import CommentInline


class AnswerUrlInline(admin.TabularInline):
    model = AnswerUrl
    extra = 1


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
        CommentInline,
        AnswerUrlInline,
    ]
