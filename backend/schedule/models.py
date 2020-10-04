from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

from program.models import Program


class Schedule(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=False
    )
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=True, blank=False
    )
    start_date = models.DateTimeField(default=now, null=True, blank=False)
    end_date = models.DateTimeField(default=now, null=True, blank=False)
