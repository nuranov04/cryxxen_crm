from rest_framework.routers import DefaultRouter

from apps.client_side.our_team.views import TeamAPiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=TeamAPiViewSet
)

urlpatterns = router.urls
