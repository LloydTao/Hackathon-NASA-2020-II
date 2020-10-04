from django.db import models
from django.utils.timezone import now

from schedule.models import Schedule


class Event(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
    type = models.CharField(
        choices=(
            ("Sleep", "Sleep"),
            ("Eat", "Eat"),
            ("Exercise", "Exercise"),
            ("Nap", "Nap"),
            ("Leisure", "Leisure"),
            ("Other", "Other"),
        ),
        default="Sleep",
        max_length=20,
    )
    schedule = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, null=True, blank=False
    )
    start_time = models.DateTimeField(default=now, null=True, blank=False)
    end_time = models.DateTimeField(default=now, null=True, blank=False)

    def __str__(self):
        return str(self.title) + " >> " + str(self.schedule)
