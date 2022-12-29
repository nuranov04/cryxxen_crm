from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.client_side.achievements.models import Achievement
from apps.client_side.achievements.serializers import AchievementsSerializer


class AchievementsApiViewSet(GenericViewSet,
                             ListModelMixin):
    queryset = Achievement.objects.all()
    serializer_class = AchievementsSerializer