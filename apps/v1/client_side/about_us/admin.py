from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.v1.client_side.about_us.models import AboutUs


class AboutUsAdmin(TranslatableAdmin):
    list_display = (
        "id",
        "created_at",
        "content"
    )
    fieldsets = (
        (None, {
            'fields': ('content', "type"),
        }),
    )


admin.site.register(AboutUs, AboutUsAdmin)
