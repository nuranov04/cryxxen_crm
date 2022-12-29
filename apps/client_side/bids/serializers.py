from rest_framework.serializers import ModelSerializer

from apps.client_side.bids.models import Bid


class BidSerializer(ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"

