from django.contrib import admin

from apps.main.directions.models import Direction
from apps.internship.groups.admin import BunchInline


@admin.register(Direction)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
    inlines = [
        BunchInline
    ]
