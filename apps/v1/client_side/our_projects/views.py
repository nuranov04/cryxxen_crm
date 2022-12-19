from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.v1.client_side.our_projects.models import Project
from apps.v1.client_side.our_projects.serializers import ProjectSerializer


class ProjectApiViewSet(GenericViewSet,
                        ListModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
