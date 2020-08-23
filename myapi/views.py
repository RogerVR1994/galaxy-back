from rest_framework import viewsets

from .serializers import ParticipantSerializer
from .models import Participant


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all().order_by('sid')
    serializer_class = ParticipantSerializer