from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from PP5_Q20.permissions import IsOwnerOrReadOnly
from .models import DNDEvent
from .serializers import DNDEventSerializer


class DNDEventList(generics.ListCreateAPIView):
    """
    Lists D&D related events or allows to create an event if authenticated.
    """
    serializer_class = DNDEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = DNDEvent.objects.all()order_by('created_at')
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        #'response_count',
        'responses__created_at',
        'owner__followed__owner__profile'
    ]
    search_fields = [
        'owner__username',
        'game_name',
        'game_description'
    ]
    filterset_fields = [
        'owner__profile',
        'owner__followed__owner__profile'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DNDEventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves a D&D related event,
    if authenticated and owning the event, you can modify or delete it.
    """
    serializer_class = DNDEventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = DNDEvent.objects.all()order_by('created_at')
