from rest_framework import serializers
from .models import User, Task, Team, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'date_joined', 'username')
        read_only_fields = ('username',)#tupla musi miec przecinek po pierwszym elemencie,inaczej jest stringiem


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'created', 'creator', 'finished', 'teams', 'description')
        read_only_fields = ('name',)#tupla musi miec przecinek po pierwszym elemencie,inaczej jest stringiem


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'created', 'creator', 'name', 'users')
        read_only_fields = ('name',) #tupla musi miec przecinek po pierwszym elemencie,inaczej jest stringiem


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'commentator', 'commented')
        read_only_fields = ('commentator',)#tupla musi miec przecinek po pierwszym elemencie,inaczej jest stringiem



