from django.contrib import admin

from apps.client_side.reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "message",
        "created_at",
        "updated_at",
    )
