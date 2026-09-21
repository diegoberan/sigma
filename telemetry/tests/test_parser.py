from decimal import Decimal

import pytest

from telemetry.domain.parser import PayloadParseError, parse_payload


def test_parse_payload_preserves_generic_measurement_values():
    parsed = parse_payload("EM-Campinas-001;-22.807222;-47.075556;39865;19.8;63.0")

    assert parsed.device_id == "EM-Campinas-001"
    assert parsed.latitude == Decimal("-22.807222")
    assert parsed.longitude == Decimal("-47.075556")
    assert (parsed.value_1, parsed.value_2, parsed.value_3) == ("39865", "19.8", "63.0")


def test_parse_payload_rejects_wrong_field_count():
    with pytest.raises(PayloadParseError):
        parse_payload("device;1;2")
