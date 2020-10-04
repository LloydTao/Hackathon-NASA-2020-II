from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing events.
    """

    def get_queryset(self):
        if self.request.data.get("schedule") is not None:
            return Event.objects.filter(schedule=self.request.data.get("schedule"))
        return Event.objects.none()

    serializer_class = EventSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
