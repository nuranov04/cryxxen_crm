from rest_framework.routers import DefaultRouter

from apps.client_side.our_mission.views import OurMissionApiViewSet

router = DefaultRouter()

router.register(
    prefix="",
    viewset=OurMissionApiViewSet
)

urlpatterns = router.urls
