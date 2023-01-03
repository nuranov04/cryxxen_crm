from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.internship.reports.models import Report
from apps.internship.reports.serializers import ReportSerializer
from utils.permissions import IsIntern


class ReportApiViewSet(GenericViewSet,
                       mixins.CreateModelMixin):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsIntern]

    def perform_create(self, serializer):
        return serializer.save(intern=self.request.user)
