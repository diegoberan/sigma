from django.contrib import admin

from telemetry.models import Device, TelemetryReading


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("external_id", "topic", "active", "updated_at")
    search_fields = ("external_id", "name", "topic")
    list_filter = ("active",)


@admin.register(TelemetryReading)
class TelemetryReadingAdmin(admin.ModelAdmin):
    list_display = ("device", "topic", "value_1", "value_2", "value_3", "received_at")
    search_fields = ("device__external_id", "topic", "payload_raw")
    list_filter = ("device",)
    readonly_fields = ("received_at",)
