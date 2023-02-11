from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.client_side.partners.models import Partner
from apps.client_side.partners.serializers import PartnerSerializer


class PartnerApiViewSet(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        ):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
