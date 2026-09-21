from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("telemetry", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="telemetryreading",
            old_name="value_1",
            new_name="uptime_seconds",
        ),
        migrations.RenameField(
            model_name="telemetryreading",
            old_name="value_2",
            new_name="temperature_c",
        ),
        migrations.RenameField(
            model_name="telemetryreading",
            old_name="value_3",
            new_name="humidity_percent",
        ),
        migrations.AlterField(
            model_name="telemetryreading",
            name="uptime_seconds",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="telemetryreading",
            name="temperature_c",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name="telemetryreading",
            name="humidity_percent",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
