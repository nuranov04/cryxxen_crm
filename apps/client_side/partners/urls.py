from rest_framework.routers import DefaultRouter

from apps.client_side.partners.views import PartnerApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=PartnerApiViewSet
)

urlpatterns = router.urls
