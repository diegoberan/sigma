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
        uptime_seconds: int,
        temperature_c: Decimal,
        humidity_percent: Decimal,
    ) -> TelemetryReading:
        return TelemetryReading.objects.create(
            device=device,
            topic=topic,
            payload_raw=payload_raw,
            latitude=latitude,
            longitude=longitude,
            uptime_seconds=uptime_seconds,
            temperature_c=temperature_c,
            humidity_percent=humidity_percent,
        )
