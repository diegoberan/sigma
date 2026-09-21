from django.db import transaction

from telemetry.domain.parser import parse_payload
from telemetry.repositories.device_repository import DeviceRepository
from telemetry.repositories.telemetry_repository import TelemetryRepository


class TelemetryIngestionService:
    @staticmethod
    @transaction.atomic
    def ingest(*, topic: str, raw_payload: str):
        parsed = parse_payload(raw_payload)
        device = DeviceRepository.get_or_create_from_telemetry(
            external_id=parsed.device_id,
            topic=topic,
            latitude=parsed.latitude,
            longitude=parsed.longitude,
        )
        return TelemetryRepository.create_reading(
            device=device,
            topic=topic,
            payload_raw=raw_payload,
            latitude=parsed.latitude,
            longitude=parsed.longitude,
            uptime_seconds=parsed.uptime_seconds,
            temperature_c=parsed.temperature_c,
            humidity_percent=parsed.humidity_percent,
        )
