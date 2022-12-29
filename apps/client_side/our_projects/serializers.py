from rest_framework.serializers import ModelSerializer

from apps.client_side.our_projects.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
