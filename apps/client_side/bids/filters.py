from django_filters.rest_framework import FilterSet


from apps.client_side.bids.models import Bid


class BidFilter(FilterSet):
    class Meta:
        model = Bid
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "message",
            "type",
        ]
