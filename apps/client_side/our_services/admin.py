from django.contrib import admin

from apps.client_side.our_services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "icon",
        "created_at",
    )
