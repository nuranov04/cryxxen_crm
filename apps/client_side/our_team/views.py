from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.client_side.our_team.serializers import TeamSerializer
from apps.client_side.our_team.models import Team


class TeamAPiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     ):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
