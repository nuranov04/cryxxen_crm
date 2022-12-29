from rest_framework.serializers import ModelSerializer

from apps.client_side.our_mission.models import OurMission


class OurMissionSerializer(ModelSerializer):
    class Meta:
        model = OurMission
        fields = "__all__"
