from rest_framework import serializers
from .models import User, Task, Team, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'date_joined', 'username')
        read_only_fields = ('username')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'created', 'creator', 'finished')
        read_only_fields = ('name')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'created', 'creator', 'name', 'users')
        read_only_fields = ('name')


class CommentSerializer(serializers.ModelSerializer):
    def
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'commentator', 'commented')
        read_only_fields = ('commentator')



