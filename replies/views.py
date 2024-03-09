from rest_framework import generics, permissions
from PP5_Q20.permissions import IsOwnerOrReadOnly
from .models import Replies
from .serializers import RepliesSerializer


class ReplyListView(generics.ListCreateAPIView):
    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReplyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]