from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.v1.client_side.our_team.serializers import TeamSerializer
from apps.v1.client_side.our_team.models import Team


class TeamAPiViewSet(GenericViewSet,
                     ListModelMixin):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
