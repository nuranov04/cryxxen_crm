from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.v1.client_side.our_services.models import Service
from apps.v1.client_side.our_services.serializers import ServiceSerializer

class ServiceApiViewSet(GenericViewSet,
                        ListModelMixin):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
