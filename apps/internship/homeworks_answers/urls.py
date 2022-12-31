from rest_framework.routers import DefaultRouter

from apps.internship.homeworks_answers.views import AnswerApiViewSet, AnswerUrlApiViewSet


router = DefaultRouter()
router.register(
    prefix="answers",
    viewset=AnswerApiViewSet
)

router.register(
    prefix="answers_urls",
    viewset=AnswerUrlApiViewSet
)

urlpatterns = router.urls
