import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .serializers import UserSerializer

from rest_framework import status
from rest_framework.test import APIClient
from django_session_jwt.test import Client


class RegisterUserTestCase(TestCase):
    client = Client()

    def test_create_user(self):
        url = reverse("user-list")

        username = "matt"
        password = "matthewd"
        email = "matt@matt.com"
        first_name = "Matthew"
        last_name = "Drayton"

        # Creating a new account
        response = self.client.post(
            url,
            {
                "username": username,
                "password": password,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Creating a duplicate account
        response = self.client.post(
            url,
            {
                "username": username,
                "password": password,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check user has been added to database
        User = get_user_model()
        user_exists = User.objects.filter(
            username=username, email=email, first_name=first_name, last_name=last_name
        ).exists()
        self.assertTrue(user_exists)

        # Check we can log in successfully
        logged_in = self.client.login(username=username, password=password)
        self.assertNotEqual(logged_in, None)


class GetUsersTestCase(TestCase):

    client = APIClient()

    def setUp(self):
        User = get_user_model()
        User.objects.create(
            username="casperBD",
            first_name="Casper",
            last_name="Bull Dog",
            email="black@dogs.co.uk",
        )
        User.objects.create(
            username="muffinG",
            first_name="Muffin",
            last_name="Gradane",
            email="brown@dogs.co.uk",
        )
        User.objects.create(
            username="ramboL",
            first_name="Rambo",
            last_name="Labrador",
            email="black@dogs.co.uk",
        )

    def test_get_users(self):
        """
        Test that the user-list route returns a list of users.
        """
        # Setup.
        url = reverse("user-list")
        # Run.
        response = self.client.get(url, format="json")
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            [
                {
                    "url": "http://testserver/api/users/1/",
                    "id": 1,
                    "username": "casperBD",
                    "first_name": "Casper",
                    "last_name": "Bull Dog",
                    "email": "black@dogs.co.uk",
                },
                {
                    "url": "http://testserver/api/users/2/",
                    "id": 2,
                    "username": "muffinG",
                    "first_name": "Muffin",
                    "last_name": "Gradane",
                    "email": "brown@dogs.co.uk",
                },
                {
                    "url": "http://testserver/api/users/3/",
                    "id": 3,
                    "username": "ramboL",
                    "first_name": "Rambo",
                    "last_name": "Labrador",
                    "email": "black@dogs.co.uk",
                },
            ],
        )
