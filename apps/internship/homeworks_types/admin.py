from django.contrib import admin

from apps.internship.homeworks_types.models import HomeworkType


@admin.register(HomeworkType)
class HomeworkTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "group",
    )


class HomeworkTypeInline(admin.TabularInline):
    model = HomeworkType
    extra = 1
