from rest_framework import serializers

from apps.client_side.about_us.models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = "__all__"
