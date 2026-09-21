from django.db import models


class Device(models.Model):
    external_id = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=160, blank=True)
    topic = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["external_id"]

    def __str__(self) -> str:
        return self.name or self.external_id


class TelemetryReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="readings")
    topic = models.CharField(max_length=255)
    payload_raw = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    uptime_seconds = models.PositiveIntegerField()
    temperature_c = models.DecimalField(max_digits=6, decimal_places=2)
    humidity_percent = models.DecimalField(max_digits=6, decimal_places=2)
    received_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-received_at"]
        indexes = [
            models.Index(fields=["device", "-received_at"]),
            models.Index(fields=["-received_at"]),
        ]

    def __str__(self) -> str:
        return f"{self.device.external_id} @ {self.received_at.isoformat()}"
