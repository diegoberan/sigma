from django.contrib import admin
from django.urls import include, path

from core.views import placeholder

urlpatterns = [
    path("", placeholder, name="placeholder"),
    path("admin/", admin.site.urls),
    path("api/", include("telemetry.api.urls")),
]
