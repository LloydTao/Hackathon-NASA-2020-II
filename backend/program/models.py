from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
