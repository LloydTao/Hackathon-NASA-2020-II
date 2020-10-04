from django.urls import path, include

from rest_framework import routers

from .viewsets import EventViewSet


# Take care when naming API routes.
# https://restfulapi.net/resource-naming/
router = routers.DefaultRouter()
router.register(r"events", EventViewSet)

urlpatterns = []
