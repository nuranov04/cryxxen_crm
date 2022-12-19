from rest_framework.routers import DefaultRouter

from apps.v1.client_side.about_us.views import AboutUsApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=AboutUsApiViewSet
)

urlpatterns = router.urls
