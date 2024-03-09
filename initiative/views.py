from rest_framework import generics
from .models import DNDInitiative
from .serializers import DNDInitiativeSerializer
from PP5_Q20.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class DNDInitiativeListView(generics.ListCreateAPIView):
    """Views list and creating DND initiatives."""
    queryset = DNDInitiative.objects.all()
    serializer_class = DNDInitiativeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return DNDInitiative.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Save the owner of the initiative as the current user!"""
        serializer.save(owner=self.request.user)


class DNDInitiativeDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a DND initiative."""
    queryset = DNDInitiative.objects.all()
    serializer_class = DNDInitiativeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return DNDInitiative.objects.filter(owner=user)
