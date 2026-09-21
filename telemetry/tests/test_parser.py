from decimal import Decimal

import pytest

from telemetry.domain.parser import PayloadParseError, parse_payload


def test_parse_payload_maps_confirmed_telemetry_values():
    parsed = parse_payload("EM-Campinas-001;-22.807222;-47.075556;39865;19.8;63.0")

    assert parsed.device_id == "EM-Campinas-001"
    assert parsed.latitude == Decimal("-22.807222")
    assert parsed.longitude == Decimal("-47.075556")
    assert parsed.uptime_seconds == 39865
    assert parsed.temperature_c == Decimal("19.8")
    assert parsed.humidity_percent == Decimal("63.0")


def test_parse_payload_rejects_wrong_field_count():
    with pytest.raises(PayloadParseError):
        parse_payload("device;1;2")
