from rest_framework import serializers
from .models import User, Task, Team, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('date_joined', 'username')
        read_only_fields = ('id', 'date_joined',)#tupla musi miec przecinek po pierwszym elemencie,inaczej jest stringiem


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'created', 'creator', 'finished', 'teams', 'description')
        read_only_fields = ('name', 'created', 'creator', 'finished', 'teams', 'description',)#tupla musi miec przecinek po pierwszym elemencie,inaczej jest stringiem


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('created', 'creator', 'name', 'users')
        read_only_fields = ('id', 'created', 'creator',) #tupla musi miec przecinek po pierwszym elemencie,inaczej jest stringiem


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'creator', 'whencommented', 'whatcommented')
        read_only_fields = ('id', 'creator', 'commented',)#tupla musi miec przecinek po pierwszym elemencie,inaczej jest stringiem



