from django.db import models
from django.contrib.auth.models import User
from dnd_events.models import DNDEvent


class Replies(models.Model):
    """
    Replies model, related to DNDEvent
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    dnd_event = models.ForeignKey(
        DNDEvent, on_delete=models.CASCADE, related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'dnd_event']

    def __str__(self):
        return f'{self.owner} {self.dnd_event}'
