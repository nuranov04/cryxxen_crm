from rest_framework.routers import DefaultRouter

from apps.client_side.achievements.views import AchievementsApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=AchievementsApiViewSet
)

urlpatterns = router.urls
