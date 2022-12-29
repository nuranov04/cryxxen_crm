from django.contrib import admin

from apps.client_side.our_team.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "position",
        "first_name",
        "last_name",
        "age",
        "image",
        "created_at",
        "updated_at",
    )
