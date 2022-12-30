from rest_framework.routers import DefaultRouter

from apps.main.users.views import UserApiViewSet

router = DefaultRouter()
router.register(
    prefix="users",
    viewset=UserApiViewSet
)

urlpatterns = router.urls
