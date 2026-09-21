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
            value_1=parsed.value_1,
            value_2=parsed.value_2,
            value_3=parsed.value_3,
        )
