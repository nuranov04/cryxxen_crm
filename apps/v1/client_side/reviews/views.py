from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from apps.v1.client_side.reviews.models import Review
from apps.v1.client_side.reviews.serializers import ReviewSerializer


class ReviewApiViewSet(GenericViewSet,
                       ListModelMixin,
                       CreateModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    print(sum([ins.stars for ins in Review.objects.all()])/Review.objects.all().count())

