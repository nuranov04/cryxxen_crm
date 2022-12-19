from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from apps.v1.client_side.bids.models import Bid
from apps.v1.client_side.bids.serializers import BidSerializer


class BidApiViewSet(GenericViewSet,
                    CreateModelMixin):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

