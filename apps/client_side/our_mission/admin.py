from django.contrib import admin

from apps.client_side.our_mission.models import OurMission


@admin.register(OurMission)
class OurMissionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
    )



