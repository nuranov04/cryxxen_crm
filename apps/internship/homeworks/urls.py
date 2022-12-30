from rest_framework.routers import DefaultRouter

from apps.internship.homeworks.views import HomeWorkApiViewSet, HomeworkUrlApiViewSet


router = DefaultRouter()
router.register(
    prefix="homeworks",
    viewset=HomeWorkApiViewSet
)
router.register(
    prefix="homeworks/urls/create",
    viewset=HomeworkUrlApiViewSet
)

urlpatterns = router.urls
