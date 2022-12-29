from django.contrib import admin

from apps.client_side.our_projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "image",
        "created_at",
        "updated_at",
    )
