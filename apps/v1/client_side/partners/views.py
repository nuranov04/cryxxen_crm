from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.v1.client_side.partners.models import Partner
from apps.v1.client_side.partners.serializers import PartnerSerializer


class PartnerApiViewSet(GenericViewSet,
                        ListModelMixin):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
