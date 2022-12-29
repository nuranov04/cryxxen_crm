from django.contrib import admin

from apps.client_side.partners.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "image",
        "ordering",
    )
