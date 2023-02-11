import datetime

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response

from apps.internship.reports.models import Report
from apps.internship.reports.serializers import ReportSerializer
from utils.permissions import IsIntern


class ReportApiViewSet(GenericViewSet,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin
                       ):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsIntern]

    def perform_create(self, serializer):
        return serializer.save(intern=self.request.user)

    def create(self, request, *args, **kwargs):
        reviews = Report.objects.filter(intern=request.user, date=datetime.date.today()).all().count()
        if reviews >= 1:
            return Response(data={"error": "you can't create two reports a day"})
        return super().create(request, *args, **kwargs)

