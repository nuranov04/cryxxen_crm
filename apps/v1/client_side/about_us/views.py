from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.v1.client_side.about_us.models import AboutUs
from apps.v1.client_side.about_us.serializers import AboutUsSerializer


class AboutUsApiViewSet(GenericViewSet,
                        ListModelMixin):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

