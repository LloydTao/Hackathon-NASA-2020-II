from django.db import models
from django.utils.timezone import now

from schedule.models import Schedule


class Event(models.Model):
    schedule = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, null=True, blank=False
    )
    start_time = models.DateTimeField(default=now, null=True, blank=False)
    end_time = models.DateTimeField(default=now, null=True, blank=False)
