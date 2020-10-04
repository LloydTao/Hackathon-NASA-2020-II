import json

from django.test import TestCase
from django.urls import reverse

from .models import Schedule
from .serializers import ScheduleSerializer

from rest_framework import status

from django.contrib.auth import get_user_model
from datetime import datetime, timezone, timedelta
from django.utils.timezone import make_aware, utc
from django_session_jwt.test import Client


class GetSchedulesTestCase(TestCase):

    client = Client()

    def setUp(self):
        User = get_user_model()

        user1 = User.objects.create_user(username="matt", password="matthewd")
        user2 = User.objects.create_user(username="lewis", password="lewislloyd")

        Schedule.objects.create(
            user=user1,
            start_date=make_aware(datetime(year=2020, month=9, day=1, hour=14), utc),
            end_date=make_aware(datetime(year=2020, month=10, day=1, hour=14), utc),
        )

        Schedule.objects.create(
            user=user2,
            start_date=datetime(year=2020, month=9, day=1, hour=14),
            end_date=datetime(year=2020, month=10, day=1, hour=14),
        )

    def test_get_schedules(self):
        """
        Test that the schedule-list route returns a list of schedules.
        """
        # Setup.
        self.client.post(
            reverse("login"),
            {"username": "matt", "password": "matthewd"},
            format="json",
        )
        url = reverse("schedule-list")
        # Run.
        response = self.client.get(url, format="json")
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            [
                {
                    "url": "http://testserver/api/schedules/1/",
                    "id": 1,
                    "user": "http://testserver/api/users/1/",
                    "program": None,
                    "start_date": "2020-09-01T14:00:00Z",
                    "end_date": "2020-10-01T14:00:00Z",
                },
            ],
        )
