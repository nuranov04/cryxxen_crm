from django.contrib import admin

from apps.internship.homeworks_answers_comments.models import Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2
