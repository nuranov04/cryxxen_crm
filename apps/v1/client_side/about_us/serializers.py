from rest_framework import serializers

from apps.v1.client_side.about_us.models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            "id",
            "content",
            "created_at",
            "updated_at",
        )
