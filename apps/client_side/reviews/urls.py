from rest_framework.routers import DefaultRouter

from apps.client_side.reviews.views import ReviewApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=ReviewApiViewSet
)

urlpatterns = router.urls
