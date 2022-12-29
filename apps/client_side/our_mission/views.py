from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.client_side.our_mission.models import OurMission
from apps.client_side.our_mission.serializers import OurMissionSerializer


class OurMissionApiViewSet(GenericViewSet,
                           ListModelMixin):
    queryset = OurMission.objects.all()
    serializer_class = OurMissionSerializer
