from rest_framework.routers import DefaultRouter

from apps.internship.groups.views import BunchApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=BunchApiViewSet
)

urlpatterns = router.urls
