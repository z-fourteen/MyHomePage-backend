from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ThoughtEntry, MessageEntry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )
        return user

class ThoughtEntrySerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = ThoughtEntry
        fields = ['id', 'title', 'date', 'content', 'author_name', 'is_public']
        read_only_fields = ['author_name']

class MessageEntrySerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = MessageEntry
        fields = ['id', 'sender', 'sender_username', 'content', 'timestamp', 'is_public']
        read_only_fields = ['sender', 'sender_username', 'timestamp']