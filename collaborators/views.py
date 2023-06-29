from rest_framework import generics, permissions
from taskflow.permissions import IsOwnerOrReadOnly
from .models import Collaborator
from .serializers import CollaboratorSerializer


class CollaboratorList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CollaboratorSerializer
    queryset = Collaborator.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CollaboratorDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CollaboratorSerializer
    queryset = Collaborator.objects.all()