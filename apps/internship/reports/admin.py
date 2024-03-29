from django.contrib import admin

from apps.internship.reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "intern",
        "content",
        "date",
        "is_accept",
    )
