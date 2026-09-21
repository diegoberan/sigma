from rest_framework import serializers

from telemetry.models import Device, TelemetryReading


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("id", "external_id", "name", "topic", "latitude", "longitude", "active")


class TelemetryReadingSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(source="device.external_id", read_only=True)

    class Meta:
        model = TelemetryReading
        fields = (
            "id",
            "device_id",
            "topic",
            "payload_raw",
            "latitude",
            "longitude",
            "value_1",
            "value_2",
            "value_3",
            "received_at",
        )
