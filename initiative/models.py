from django.db import models
from django.contrib.auth.models import User


class DNDInitiative(models.Model):
    """
    Model for DND initiative counter.
    """
    name = models.CharField(max_length=255)
    initiative = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-initiative']