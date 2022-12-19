from rest_framework import serializers

from apps.v1.client_side.achievements.models import Achievement


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"
