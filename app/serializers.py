from rest_framework import serializers
from .models import UserProfile, Note
from django.contrib.auth.models import User

class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    note = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Note` instance, given the validated data.
        """
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Note` instance, given the validated data.
        """
        instance.note = validated_data.get('note', instance.note)
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class ProfileSerializer(serializers.Serializer):
    user = UserSerializer()
    bio = serializers.CharField(max_length=200)