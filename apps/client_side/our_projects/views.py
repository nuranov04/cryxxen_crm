from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.client_side.our_projects.models import Project
from apps.client_side.our_projects.serializers import ProjectSerializer


class ProjectApiViewSet(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        ):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
