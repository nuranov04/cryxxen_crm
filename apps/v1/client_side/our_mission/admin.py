from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.v1.client_side.our_mission.models import OurMission


class OurMissionAdmin(TranslatableAdmin):
    list_display = (
        "id",
        "content"
    )
    fieldsets = (
        (None, {
            "fields": ("content",)
        }),
    )


admin.site.register(OurMission, OurMissionAdmin)
