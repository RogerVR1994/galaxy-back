from rest_framework import serializers

from .models import Participant

class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ('name', 'manager', 'type_of_participant', 'foundation_date')