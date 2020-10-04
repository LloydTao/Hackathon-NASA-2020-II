import json

from django.test import TestCase
from django.urls import reverse

from .models import Event
from .serializers import EventSerializer

from rest_framework import status
from rest_framework.test import APIClient


class GetEventsTestCase(TestCase):

    client = APIClient()

    def setUp(self):
        Event.objects.create(
            title="Space Mission Alpha",
        )
        Event.objects.create(
            title="Mission 2: Electric Boogaloo",
        )
        Event.objects.create(
            title="Space: Episode III - Revenge of the Sith",
        )

    def test_get_events(self):
        """
        Test that the user-list route returns a list of events.
        """
        # Setup.
        url = reverse("event-list")
        # Run.
        response = self.client.get(url, format="json")
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            [
                {
                    "url": "http://testserver/api/events/1/",
                    "id": 1,
                    "title": "Space Mission Alpha",
                },
                {
                    "url": "http://testserver/api/events/2/",
                    "id": 2,
                    "title": "Mission 2: Electric Boogaloo",
                },
                {
                    "url": "http://testserver/api/events/3/",
                    "id": 3,
                    "title": "Space: Episode III - Revenge of the Sith",
                },
            ],
        )
