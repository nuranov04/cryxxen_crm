from rest_framework.routers import DefaultRouter

from apps.internship.homeworks_answers.views import AnswerApiViewSet, AnswerUrlsApiViewSet


router = DefaultRouter()
router.register(
    prefix="answers",
    viewset=AnswerApiViewSet
)

router.register(
    prefix="answers_urls",
    viewset=AnswerUrlsApiViewSet
)

urlpatterns = router.urls
