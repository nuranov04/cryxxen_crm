from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.client_side.partners.models import Partner
from apps.client_side.partners.serializers import PartnerSerializer


class PartnerApiViewSet(GenericViewSet,
                        ListModelMixin):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
