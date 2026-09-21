import logging
import uuid

import paho.mqtt.client as mqtt
from django.conf import settings
from django.core.management.base import BaseCommand

from telemetry.domain.parser import PayloadParseError
from telemetry.services.telemetry_ingestion_service import TelemetryIngestionService

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Subscribe to the configured MQTT topic and persist telemetry readings."

    def handle(self, *args, **options):
        client_id = f"{settings.MQTT_CLIENT_ID}-{uuid.uuid4().hex[:8]}"
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id)
        if settings.MQTT_USERNAME:
            client.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)

        def on_connect(mqtt_client, userdata, flags, reason_code, properties):
            if reason_code != 0:
                self.stderr.write(f"MQTT connection failed: {reason_code}")
                return
            mqtt_client.subscribe(settings.MQTT_TOPIC, qos=settings.MQTT_QOS)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Connected to {settings.MQTT_HOST}:{settings.MQTT_PORT}; "
                    f"subscribed to {settings.MQTT_TOPIC}"
                )
            )

        def on_message(mqtt_client, userdata, message):
            raw_payload = message.payload.decode("utf-8", errors="replace").strip()
            try:
                reading = TelemetryIngestionService.ingest(
                    topic=message.topic,
                    raw_payload=raw_payload,
                )
            except PayloadParseError as exc:
                self.stderr.write(f"Invalid payload on {message.topic}: {exc}")
                return
            self.stdout.write(f"Persisted telemetry reading {reading.pk}")

        client.on_connect = on_connect
        client.on_message = on_message
        client.reconnect_delay_set(min_delay=1, max_delay=30)
        client.connect(settings.MQTT_HOST, settings.MQTT_PORT, keepalive=60)
        client.loop_forever()
