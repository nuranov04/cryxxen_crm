from django.contrib import admin

from apps.v1.client_side.partners.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "image",
        "ordering",
    )
