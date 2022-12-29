from rest_framework.serializers import ModelSerializer

from apps.client_side.partners.models import Partner


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"
