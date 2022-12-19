from rest_framework.routers import DefaultRouter

from apps.v1.client_side.bids.views import BidApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=BidApiViewSet
)

urlpatterns = router.urls
