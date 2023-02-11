from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.client_side.achievements.models import Achievement
from apps.client_side.achievements.serializers import AchievementsSerializer


class AchievementsApiViewSet(GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.UpdateModelMixin,
                             ):
    queryset = Achievement.objects.all()
    serializer_class = AchievementsSerializer
