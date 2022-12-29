from rest_framework.serializers import ModelSerializer

from apps.client_side.our_team.models import Team


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


