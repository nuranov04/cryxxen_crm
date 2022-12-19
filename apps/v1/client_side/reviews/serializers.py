from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.v1.client_side.reviews.models import Review


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        read_only_fields = ("id",)
        fields = "__all__"

    def get_total_stars(self):
        objects = Review.objects.value("stars").all()
        print(sum([ins.start for ins in objects]))
        return sum([ins.start for ins in objects])
