from django.contrib import admin

# from apps.internship.homeworks_types.admin import HomeworkTypeInline
from apps.internship.homeworks.admin import HomeworkInline
from apps.internship.groups.models import Bunch


@admin.register(Bunch)
class BunchAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "direction",
    )
    inlines = [
        # HomeworkTypeInline,
        HomeworkInline,
    ]


class BunchInline(admin.TabularInline):
    model = Bunch
    extra = 1
