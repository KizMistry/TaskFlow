from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    project_owner = serializers.ReadOnlyField(source='project.owner.username')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'is_owner', 'project', 'project_owner',
            'created_at', 'updated_at', 'task', 'description', 'file',
            'task_priority', 'task_status',
        ]

class TaskDetailSerializer(TaskSerializer):
    project = serializers.ReadOnlyField(source='project.id')