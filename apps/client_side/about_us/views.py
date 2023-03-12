from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.client_side.about_us.models import AboutUs
from apps.client_side.about_us.serializers import AboutUsSerializer


class AboutUsApiViewSet(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin
                        ):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    # @action()
