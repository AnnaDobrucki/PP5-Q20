from rest_framework import serializers
from .models import DNDInitiative


class DNDInitiativeSerializer(serializers.ModelSerializer):
    """Serializer for DND Initiative model."""

    class Meta:
        model = DNDInitiative
        fields = ['id', 'name', 'initiative']
