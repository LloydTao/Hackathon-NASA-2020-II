from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing events.
    """

    queryset = Event.objects.all()

    serializer_class = EventSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
