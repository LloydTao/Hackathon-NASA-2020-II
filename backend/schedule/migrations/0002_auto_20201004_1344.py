# Generated by Django 3.1.1 on 2020-10-04 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("program", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="schedule",
            name="title",
        ),
        migrations.AddField(
            model_name="schedule",
            name="end_date",
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name="schedule",
            name="program",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="program.program",
            ),
        ),
        migrations.AddField(
            model_name="schedule",
            name="start_date",
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name="schedule",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
