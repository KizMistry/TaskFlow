from rest_framework import serializers
from notes.models import Note

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Note
        fields =[
            'id', 'owner', 'is_owner', 'project', 'content',
            'created_at', 'updated_at', 'task', 'profile_id',
            'profile_image',
        ]


class NoteDetailSerializer(NoteSerializer):
    project = serializers.ReadOnlyField(source='project.id')
    task = serializers.ReadOnlyField(source='task.id')