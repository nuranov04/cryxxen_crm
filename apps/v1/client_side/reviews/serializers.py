from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.v1.client_side.reviews.models import Review


class ReviewSerializer(ModelSerializer):
    total_stars = SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        read_only_fields = ("id",)
        fields = (
            "id",
            "total_stars",
            "stars",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "message",
        )

    def get_total_stars(self, *args, **kwargs):
        objects = Review.objects.values("stars")
        return round(sum([ins["stars"] for ins in objects]) / len(objects), 2)
