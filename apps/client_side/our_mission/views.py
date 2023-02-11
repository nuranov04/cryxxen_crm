from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.client_side.our_mission.models import OurMission
from apps.client_side.our_mission.serializers import OurMissionSerializer


class OurMissionApiViewSet(GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.UpdateModelMixin,
                           ):
    queryset = OurMission.objects.all()
    serializer_class = OurMissionSerializer
