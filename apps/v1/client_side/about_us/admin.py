from django.contrib import admin

from apps.v1.client_side.about_us.models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "content"
    )
