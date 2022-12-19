from rest_framework.serializers import ModelSerializer

from apps.v1.client_side.our_projects.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
