from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


class PayloadParseError(ValueError):
    """Raised when an MQTT payload does not follow the current contract."""


@dataclass(frozen=True, slots=True)
class ParsedTelemetry:
    device_id: str
    latitude: Decimal
    longitude: Decimal
    value_1: str
    value_2: str
    value_3: str


def parse_payload(raw_payload: str) -> ParsedTelemetry:
    fields = [field.strip() for field in raw_payload.strip().split(";")]
    if len(fields) != 6 or not fields[0]:
        raise PayloadParseError("expected six semicolon-delimited fields")

    try:
        latitude = Decimal(fields[1])
        longitude = Decimal(fields[2])
    except InvalidOperation as exc:
        raise PayloadParseError("latitude and longitude must be decimal values") from exc

    return ParsedTelemetry(
        device_id=fields[0],
        latitude=latitude,
        longitude=longitude,
        value_1=fields[3],
        value_2=fields[4],
        value_3=fields[5],
    )
