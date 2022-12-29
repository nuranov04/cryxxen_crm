from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from apps.client_side.reviews.models import Review
from apps.client_side.reviews.serializers import ReviewSerializer


class ReviewApiViewSet(GenericViewSet,
                       ListModelMixin,
                       CreateModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

