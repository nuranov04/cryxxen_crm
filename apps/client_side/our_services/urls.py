from rest_framework.routers import DefaultRouter

from apps.client_side.our_services.views import ServiceApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=ServiceApiViewSet
)

urlpatterns = router.urls
