from rest_framework import serializers

from apps.internship.reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        read_only_fields = ('intern',)
        fields = (
            'content',
            'date',
            'is_accept'
        )
