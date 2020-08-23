from rest_framework import serializers

from .models import Participant

class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ('sid', 'name', 'manager', 'type_of_participant', 'foundation_date')

    def update(self, instance, validated_data):
        instance.title = validated_data['sid']
        instance.save()
        return instance