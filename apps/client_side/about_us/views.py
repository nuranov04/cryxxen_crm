from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.client_side.about_us.models import AboutUs
from apps.client_side.about_us.serializers import AboutUsSerializer


class AboutUsApiViewSet(GenericViewSet,
                        ListModelMixin):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

