from django.urls import path

from telemetry.api.views import DeviceListView, HealthView, TelemetryReadingListView

urlpatterns = [
    path("health/", HealthView.as_view(), name="health"),
    path("devices/", DeviceListView.as_view(), name="device-list"),
    path("telemetry/", TelemetryReadingListView.as_view(), name="telemetry-list"),
]
