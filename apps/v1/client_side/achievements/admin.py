from django.contrib import admin

from apps.v1.client_side.achievements.models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
    )
