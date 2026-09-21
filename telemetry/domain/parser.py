from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


class PayloadParseError(ValueError):
    """Raised when an MQTT payload does not follow the current contract."""


@dataclass(frozen=True, slots=True)
class ParsedTelemetry:
    device_id: str
    latitude: Decimal
    longitude: Decimal
    uptime_seconds: int
    temperature_c: Decimal
    humidity_percent: Decimal


def parse_payload(raw_payload: str) -> ParsedTelemetry:
    fields = [field.strip() for field in raw_payload.strip().split(";")]
    if len(fields) != 6 or not fields[0]:
        raise PayloadParseError("expected six semicolon-delimited fields")

    try:
        latitude = Decimal(fields[1])
        longitude = Decimal(fields[2])
        uptime_seconds = int(fields[3])
        temperature_c = Decimal(fields[4])
        humidity_percent = Decimal(fields[5])
    except (InvalidOperation, ValueError) as exc:
        raise PayloadParseError("invalid numeric telemetry field") from exc

    if uptime_seconds < 0:
        raise PayloadParseError("uptime_seconds cannot be negative")

    return ParsedTelemetry(
        device_id=fields[0],
        latitude=latitude,
        longitude=longitude,
        uptime_seconds=uptime_seconds,
        temperature_c=temperature_c,
        humidity_percent=humidity_percent,
    )
