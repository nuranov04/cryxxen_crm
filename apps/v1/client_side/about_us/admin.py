from django.contrib import admin

from apps.v1.client_side.about_us.models import AboutUs


class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
        "created_at",
    )

admin.site.register(AboutUs, AboutUsAdmin)
