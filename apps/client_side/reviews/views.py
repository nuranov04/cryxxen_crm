from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.client_side.reviews.models import Review
from apps.client_side.reviews.serializers import ReviewSerializer


class ReviewApiViewSet(GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       ):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

