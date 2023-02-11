from rest_framework.routers import DefaultRouter

from .views import DirectionApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=DirectionApiViewSet
)

urlpatterns = router.urls
