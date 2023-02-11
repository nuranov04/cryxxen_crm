from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters

from apps.client_side.bids.models import Bid
from apps.client_side.bids.filters import BidFilter
from apps.client_side.bids.serializers import BidSerializer


class BidApiViewSet(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    ):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_class = BidFilter
    ordering_fields = [
        "created_at",
    ]
