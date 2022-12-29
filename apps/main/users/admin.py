from django.contrib import admin

from apps.main.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "rating",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
        "rating"
    )
    list_filter = (
        "id",
        "created_at",
        "email",
        "first_name",
        "last_name",
        "rating",
    )
