from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.client_side.our_services.models import Service
from apps.client_side.our_services.serializers import ServiceSerializer


class ServiceApiViewSet(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        ):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
