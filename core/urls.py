"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
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

client_side_api_urlpatterns_v1 = [
    path("about_us/", include("apps.v1.client_side.about_us.urls")),
    path("achievements/", include("apps.v1.client_side.achievements.urls")),
    path("projects/", include("apps.v1.client_side.our_projects.urls")),
    path("team/", include("apps.v1.client_side.our_team.urls")),
    path("services/", include("apps.v1.client_side.our_services.urls")),
    path("mission/", include("apps.v1.client_side.our_mission.urls")),
    path("requests/", include("apps.v1.client_side.bids.urls")),
    path("reviews/", include("apps.v1.client_side.reviews.urls")),
    path("partners/", include("apps.v1.client_side.partners.urls")),
]


docs_api_urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

auth_urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/v1_client/", include(client_side_api_urlpatterns_v1)),

    # docs
    path("api/", include(docs_api_urlpatterns)),

    # jwt auth
    path("api/", include(auth_urlpatterns)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)