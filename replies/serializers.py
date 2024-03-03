from rest_framework import serializers
from .models import Replies
from django.db import IntegrityError


class RepliesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Replies model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Replies
        fields = ['id', 'created_at', 'owner', 'dnd_event',]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
