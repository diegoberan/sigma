from decimal import Decimal

from telemetry.models import Device, TelemetryReading


class TelemetryRepository:
    @staticmethod
    def create_reading(
        *,
        device: Device,
        topic: str,
        payload_raw: str,
        latitude: Decimal,
        longitude: Decimal,
        value_1: str,
        value_2: str,
        value_3: str,
    ) -> TelemetryReading:
        return TelemetryReading.objects.create(
            device=device,
            topic=topic,
            payload_raw=payload_raw,
            latitude=latitude,
            longitude=longitude,
            value_1=value_1,
            value_2=value_2,
            value_3=value_3,
        )
