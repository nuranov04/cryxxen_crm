from rest_framework.routers import DefaultRouter

from .views import BoardApiViewSet, StatusApiViewSet, TaskApiViewSet

router = DefaultRouter()
router.register(
    prefix="board",
    viewset=BoardApiViewSet
)
router.register(
    prefix="status",
    viewset=StatusApiViewSet
)
router.register(
    prefix="task",
    viewset=TaskApiViewSet
)

urlpatterns = router.urls
