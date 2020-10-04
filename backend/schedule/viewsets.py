from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing schedules.
    """

    # queryset = Schedule.objects.all()

    serializer_class = ScheduleSerializer

    def get_queryset(self):
        user = self.request.user
        if user is None:
            return Schedule.objects.none()
        return Schedule.objects.filter(user=user)

    permission_classes = [IsAuthenticatedOrReadOnly]
