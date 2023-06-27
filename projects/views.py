from django.db.models import Count
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer
from taskflow.permissions import IsOwnerOrReadOnly


class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Project.objects.annotate(
        tasks_count=Count('task', distinct=True),
        notes_count=Count('note', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'tasks_count',
        'notes_count',
        'tasks__created_at',
        'notes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.annotate(
        tasks_count=Count('task', distinct=True),
        notes_count=Count('note', distinct=True),
    ).order_by('-created_at')