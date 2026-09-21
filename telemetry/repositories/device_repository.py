from decimal import Decimal

from telemetry.models import Device


class DeviceRepository:
    @staticmethod
    def get_or_create_from_telemetry(
        *, external_id: str, topic: str, latitude: Decimal, longitude: Decimal
    ) -> Device:
        device, _ = Device.objects.get_or_create(
            external_id=external_id,
            defaults={
                "name": external_id,
                "topic": topic,
                "latitude": latitude,
                "longitude": longitude,
            },
        )
        return device
