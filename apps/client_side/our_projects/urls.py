from rest_framework.routers import DefaultRouter

from apps.client_side.our_projects.views import ProjectApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=ProjectApiViewSet
)

urlpatterns = router.urls
