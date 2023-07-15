from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from taskflow.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.annotate(
        notes_count=Count('note', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'project',
        'owner'
    ]
    search_fields = [
        'project',
        'owner'
    ]
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Task.objects.annotate(
        notes_count=Count('note', distinct=True),
    ).order_by('-created_at').filter(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.annotate(
        notes_count=Count('note', distinct=True),
    ).order_by('-created_at')