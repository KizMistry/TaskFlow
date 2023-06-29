from django.db import IntegrityError
from rest_framework import serializers
from collaborators.models import Collaborator


class CollaboratorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Collaborator
        field = [
            'id', 'owner', 'followed', 'created_at', 'followed_name',
        ]

    def create(self, validation_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail':'possible duplicate'
            })