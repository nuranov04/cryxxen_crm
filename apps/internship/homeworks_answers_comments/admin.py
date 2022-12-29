from django.contrib import admin

from .models import Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2
