from rest_framework.routers import DefaultRouter

from .views import CommentApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=CommentApiViewSet
)

urlpatterns = router.urls
