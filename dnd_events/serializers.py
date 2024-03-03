from rest_framework import serializers
from .models import DNDEvent
from datetime import time

class CustomizedTimeField(serializers.TimeField):
    def to_representation(self, value):
        if value is None:
            return None
        return value.strftime('%H:%M:%S')

class DNDEventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()
    event_start = CustomizedTimeField(default=time.min)
    event_end = CustomizedTimeField(default=time.min)
    replies_id = serializers.SerializerMethodField()
    replies_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size exceeds 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width exceeds 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height exceeds 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = DNDEvent
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'event_start',
            'event_end', 'image', 'game_name', 'game_description',
            'is_owner', 'date', 'replies_id', 'replies_count',
            'event_end', 'event_location', 'game_master', 'contact','profile_id','profile_image'
        ]
