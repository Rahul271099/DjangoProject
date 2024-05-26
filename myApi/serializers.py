from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_by', 'created_at', 'updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.client_name')
    created_by = serializers.ReadOnlyField(source= "created_by.username")
    users = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_by', 'created_at', 'updated_at']

class UserProjectSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.client_name')
    created_by = serializers.ReadOnlyField(source= "created_by.username")

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'created_by', 'created_at', 'updated_at']
