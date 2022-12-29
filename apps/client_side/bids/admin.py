from django.contrib import admin

from apps.client_side.bids.models import Bid


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "message",
        "type",
    )
