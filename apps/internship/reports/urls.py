from rest_framework.routers import DefaultRouter

from apps.internship.reports.views import ReportApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=ReportApiViewSet
)

urlpatterns = router.urls
