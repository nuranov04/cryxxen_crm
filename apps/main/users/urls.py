from rest_framework.routers import DefaultRouter

from .views import UserApiViewSet

router = DefaultRouter()
router.register(
    prefix="users",
    viewset=UserApiViewSet
)

urlpatterns = router.urls
