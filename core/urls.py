from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CRYXXEN CRM API",
        default_version='',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="artnyr2004@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

auth_urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

client_side_api_urlpatterns_v1 = [
    # client side
    path("about_us/", include("apps.client_side.about_us.urls")),
    path("achievements/", include("apps.client_side.achievements.urls")),
    path("projects/", include("apps.client_side.our_projects.urls")),
    path("team/", include("apps.client_side.our_team.urls")),
    path("services/", include("apps.client_side.our_services.urls")),
    path("mission/", include("apps.client_side.our_mission.urls")),
    path("requests/", include("apps.client_side.bids.urls")),
    path("reviews/", include("apps.client_side.reviews.urls")),
    path("partners/", include("apps.client_side.partners.urls")),

    # internship side
    path("groups/", include("apps.internship.groups.urls")),
    path("", include("apps.internship.homeworks.urls")),

    # main side
    path("", include("apps.main.users.urls")),

    # docs
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc"
    ),

    # auth
    path("", include(auth_urlpatterns))
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/v1/", include(client_side_api_urlpatterns_v1)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
