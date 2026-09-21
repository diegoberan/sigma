from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from telemetry.api.serializers import DeviceSerializer, TelemetryReadingSerializer
from telemetry.models import Device, TelemetryReading


class HealthView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"status": "ok", "service": "sigma"})


class DeviceListView(generics.ListAPIView):
    queryset = Device.objects.filter(active=True)
    serializer_class = DeviceSerializer
    permission_classes = [permissions.AllowAny]


class TelemetryReadingListView(generics.ListAPIView):
    queryset = TelemetryReading.objects.select_related("device").all()[:100]
    serializer_class = TelemetryReadingSerializer
    permission_classes = [permissions.AllowAny]
